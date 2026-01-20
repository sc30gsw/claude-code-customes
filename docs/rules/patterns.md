# 共通パターン

プロジェクトで使用する共通パターンです。

## APIレスポンスフォーマット

```typescript
interface ApiResponse<T> {
  success: boolean
  data?: T
  error?: string
  meta?: {
    total: number
    page: number
    limit: number
  }
}
```

### 使用例

```typescript
// 成功レスポンス
const response: ApiResponse<User> = {
  success: true,
  data: user,
  meta: { total: 100, page: 1, limit: 10 }
}

// エラーレスポンス
const errorResponse: ApiResponse<User> = {
  success: false,
  error: 'User not found'
}
```

## カスタムフックパターン

```typescript
export function useDebounce<T>(value: T, delay: number): T {
  const [debouncedValue, setDebouncedValue] = useState<T>(value)

  useEffect(() => {
    const handler = setTimeout(() => setDebouncedValue(value), delay)
    return () => clearTimeout(handler)
  }, [value, delay])

  return debouncedValue
}
```

### その他の汎用フック

```typescript
// ローカルストレージ
export function useLocalStorage<T>(key: string, initialValue: T) {
  const [value, setValue] = useState<T>(() => {
    const stored = localStorage.getItem(key)
    return stored ? JSON.parse(stored) : initialValue
  })

  useEffect(() => {
    localStorage.setItem(key, JSON.stringify(value))
  }, [key, value])

  return [value, setValue] as const
}

// メディアクエリ
export function useMediaQuery(query: string): boolean {
  const [matches, setMatches] = useState(false)

  useEffect(() => {
    const media = window.matchMedia(query)
    setMatches(media.matches)
    const listener = (e: MediaQueryListEvent) => setMatches(e.matches)
    media.addEventListener('change', listener)
    return () => media.removeEventListener('change', listener)
  }, [query])

  return matches
}
```

## リポジトリパターン

```typescript
interface Repository<T> {
  findAll(filters?: Filters): Promise<T[]>
  findById(id: string): Promise<T | null>
  create(data: CreateDto): Promise<T>
  update(id: string, data: UpdateDto): Promise<T>
  delete(id: string): Promise<void>
}
```

### 実装例

```typescript
class UserRepository implements Repository<User> {
  constructor(private db: Database) {}

  async findAll(filters?: UserFilters): Promise<User[]> {
    let query = this.db.from('users').select('*')
    if (filters?.role) {
      query = query.eq('role', filters.role)
    }
    const { data, error } = await query
    if (error) throw new Error(error.message)
    return data
  }

  async findById(id: string): Promise<User | null> {
    const { data, error } = await this.db
      .from('users')
      .select('*')
      .eq('id', id)
      .single()
    if (error) return null
    return data
  }

  // ... other methods
}
```

## スケルトンプロジェクト

新機能実装時:

1. 実績のあるスケルトンプロジェクトを検索
2. 並列エージェントでオプションを評価:
   - セキュリティ評価
   - 拡張性分析
   - 関連性スコアリング
   - 実装計画
3. 最適なマッチをクローン
4. 実績のある構造内で反復

## エラーハンドリングパターン

```typescript
// Result型パターン
type Result<T, E = Error> =
  | { success: true; data: T }
  | { success: false; error: E }

async function fetchUser(id: string): Promise<Result<User>> {
  try {
    const user = await db.users.findById(id)
    if (!user) {
      return { success: false, error: new Error('User not found') }
    }
    return { success: true, data: user }
  } catch (error) {
    return { success: false, error: error as Error }
  }
}
```

## 状態管理パターン

```typescript
// Reducer パターン
type Action =
  | { type: 'SET_LOADING'; payload: boolean }
  | { type: 'SET_DATA'; payload: User[] }
  | { type: 'SET_ERROR'; payload: string }

function reducer(state: State, action: Action): State {
  switch (action.type) {
    case 'SET_LOADING':
      return { ...state, loading: action.payload }
    case 'SET_DATA':
      return { ...state, data: action.payload, loading: false }
    case 'SET_ERROR':
      return { ...state, error: action.payload, loading: false }
    default:
      return state
  }
}
```
