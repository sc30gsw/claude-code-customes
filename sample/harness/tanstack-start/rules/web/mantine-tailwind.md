---
description: Mantine 9 + Tailwind v4 coexistence — default to Mantine, cn() for layout, theme tokens
globs: ["src/**/*.tsx", "src/lib/theme.ts"]
alwaysApply: true
---

# Mantine + Tailwind Coexistence

## Default: Mantine first

Use Mantine components and props before reaching for Tailwind utilities.

```tsx
// CORRECT: Mantine spacing/color props
<Button color="blue" mt="md" size="sm">
  送信
</Button>

// WRONG: Tailwind overriding Mantine props that already exist
<Button className="mt-4 text-blue-600 text-sm">
  送信
</Button>
```

## `cn()` boundary

Use `cn()` (from `~/lib/utils`) to compose Tailwind classes on **wrapper / layout elements** around Mantine components. Do NOT use Tailwind to override Mantine component internals via arbitrary selectors.

```tsx
import { cn } from "~/lib/utils";

// CORRECT: Tailwind for layout on a container, Mantine for the component itself
export function FormSection({ children, className }: { children: ReactNode; className?: string }) {
  return <section className={cn("flex flex-col gap-4", className)}>{children}</section>;
}

// WRONG: fighting Mantine internals with Tailwind
<Button className="[&_.mantine-Button-label]:text-red-500">...</Button>;
```

## Theme tokens

Prefer Mantine theme tokens over hardcoded values. `tailwind-preset-mantine` syncs Mantine's color scale into Tailwind:

```tsx
// CORRECT: consistent with design system
<div className="bg-primary-6 text-white">   // Tailwind class from Mantine's primary palette
<Box bg="blue.6" c="white">                 // Mantine prop equivalent

// WRONG: hardcoded values that bypass the design system
<div style={{ backgroundColor: '#228BE6' }}>
```

Access theme values in code via `useMantineTheme()` or `rem()`:

```tsx
import { rem, useMantineTheme } from "@mantine/core";

const theme = useMantineTheme();
const primaryColor = theme.colors[theme.primaryColor][6];
const spacing = rem(16);
```

## Related skills

- `mantine-custom-components` — building Mantine-based components
- `frontend-design` — design patterns for this admin UI
