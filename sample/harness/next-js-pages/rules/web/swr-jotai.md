---
description: Server state via SWR (@aspida/swr), client state via Jotai, URL state via nuqs — boundary table, hook patterns, atom naming
globs: ['src/features/**/hooks/*.ts', 'src/features/**/stores/*.ts']
alwaysApply: true
---

# State Management: SWR + Jotai + nuqs

## State responsibility table

| State type   | Tool               | Location                                |
| ------------ | ------------------ | --------------------------------------- |
| Server state | SWR (useAspidaSWR) | `features/*/hooks/use-*.ts`             |
| Client state | Jotai              | `features/*/stores/*.ts`                |
| URL state    | nuqs               | `features/*/hooks/use-*-query-state.ts` |
| Form state   | @mantine/form      | `features/*/components/*-form.tsx`      |

**Do not duplicate server state in Jotai.**

## SWR: `useAspidaSWR` patterns

### Basic pattern (list fetch)

```typescript
// features/suppliers/hooks/use-suppliers.ts
import useAspidaSWR from '@aspida/swr'
import { apiClient } from '~/lib/api-client'

export function useSuppliers({
  filter,
  page,
}: Record<'filter', SuppliersFilter> & Record<'page', number>) {
  const { data, error, isLoading, mutate } = useAspidaSWR(apiClient.api.v1.suppliers, '$get', {
    keepPreviousData: true,
    query: {
      name: filter.name || undefined,
      page,
      // Convert empty strings to undefined to omit them from query params
    },
    revalidateOnFocus: false,
  })

  return {
    error,
    isLoading,
    pagination: data?.meta ?? DEFAULT_PAGINATION,
    refetch: mutate,
    suppliers: data?.suppliers ?? [],
  } as const
}
```

### Polling pattern (monitor in-progress status)

```typescript
// features/mail-groups/hooks/use-mail-groups.ts
const POLLING_INTERVAL_MS = 5000
const POLLING_DISABLED = 0

export function useMailGroups({ filter, page }: ...) {
  // ? SWR's refreshInterval(latestData) function form receives undefined before the first fetch,
  // ? so we use the onSuccess + state update pattern instead
  const [pollingInterval, setPollingInterval] = useState(POLLING_DISABLED)

  const { data, error, isLoading, mutate } = useAspidaSWR(apiClient.api.v1.mail_groups, '$get', {
    keepPreviousData: true,
    onSuccess: (responseData) => {
      const shouldPoll = responseData.mail_groups.some((mg) => isProcessing(mg.status))
      setPollingInterval(shouldPoll ? POLLING_INTERVAL_MS : POLLING_DISABLED)
    },
    query: { page, /* ...filter */ },
    refreshInterval: pollingInterval,
    revalidateOnFocus: false,
  })

  return {
    error,
    isLoading,
    mailGroups: (data?.mail_groups ?? []) as MailGroup[],
    pagination: data?.meta ?? DEFAULT_PAGINATION,
    refetch: mutate,
  } as const
}
```

## nuqs: URL state management

Put shareable UI state—filters, pagination, sorting—on the URL. Do not store it in Jotai.

```typescript
// features/mail-groups/hooks/use-mail-groups-query-state.ts
import { parseAsInteger, parseAsString, type SingleParserBuilder, useQueryStates } from 'nuqs'

const mailGroupsQueryParsers = {
  id: parseAsInteger,
  name: parseAsString.withDefault(''),
  page: parseAsInteger.withDefault(1),
  status: parseAsInteger,
} as const satisfies Record<
  keyof MailGroupsFilter | 'page',
  SingleParserBuilder<number> | SingleParserBuilder<string>
>

export function useMailGroupsQueryState() {
  const [queryState, setQueryState] = useQueryStates(mailGroupsQueryParsers, {
    history: 'push',
    shallow: true,
  })

  const setPage = (page: typeof queryState.page) => setQueryState({ page })

  // Normalize null to undefined to match the filter type
  const filter = {
    id: queryState.id ?? undefined,
    name: queryState.name,
    status: queryState.status ?? undefined,
  } as const satisfies MailGroupsFilter

  return { filter, page: queryState.page, setPage } as const
}
```

## Jotai: atom naming and placement

- **Naming**: `xxxAtom` suffix (e.g. `selectedUserIdAtom`, `sidebarOpenAtom`)
- **Placement**: feature-scoped atoms in `features/[feature]/stores/[name]-store.ts`; global atoms in `src/stores/[name]-store.ts`

### Basic atom

```typescript
// features/products/stores/product-store.ts
import { atom } from 'jotai'

export const selectedProductIdAtom = atom<string | null>(null)
```

### localStorage persistence pattern (table column settings)

```typescript
// features/mail-groups/stores/mail-groups-store.ts
import { createTableColumnSettingsAtoms } from '~/stores/table-column-settings'

// createTableColumnSettingsAtoms factory generates three atoms at once
export const { columnOrderAtom, columnSettingsModalOpenedAtom, visibleColumnsAtom } =
  createTableColumnSettingsAtoms<MailGroupTableColumnId>({
    allColumnIds: ALL_MAIL_GROUP_COLUMN_IDS,
    defaultVisibleColumns: DEFAULT_MAIL_GROUP_VISIBLE_COLUMNS,
    storageKeyPrefix: 'mail-groups', // prevents localStorage key collisions
  })
```

## Anti-pattern: do not duplicate server state in Jotai

```typescript
// WRONG: copying SWR-owned data into Jotai — causes sync issues
const [items, setItems] = useAtom(itemsAtom)
useEffect(() => {
  fetchItems().then(setItems)
}, [])

// CORRECT: let SWR own server state
const { data } = useAspidaSWR(apiClient.api.v1.items, '$get', { ... })
```

## Related rules

- [web/api-client-aspida.md](./api-client-aspida.md) — aspida + up-fetch patterns
- [typescript/project-structure.md](../typescript/project-structure.md) — feature structure
