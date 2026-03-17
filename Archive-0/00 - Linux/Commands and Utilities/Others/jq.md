---
tags: [linux,json]
---

</br>

`jq` is a powerful command-line tool for parsing, manipulating, and transforming JSON. 

> Beyond basic filtering, it supports advanced operations like joins, reductions, conditionals, and even streaming large JSON datasets.

</br>

#### Basic: Echo and Filter

```bash ln:False
echo '{"name": "Alice", "age": 30, "roles": ["admin", "dev"]}' | jq '.name'
```

*Output:*

```json ln:False
"Alice"
```

> [!note] 
> The flag <mark style="background: #D2B3FFA6;">-r</mark> (raw output) disables JSON quoting for **string output**:
> ```bash ln:False
> $ echo '{"name": "Alice"}' | jq -r '.name'
> Alice
> ```

</br>

## Examples

#### 1. Extract and Transform Nested Data

```bash ln:False
echo '{
  "users": [
    {"id": 1, "name": "Alice", "active": true},
    {"id": 2, "name": "Bob", "active": false},
    {"id": 3, "name": "Carol", "active": true}
  ]
}' | jq '.users[] | select(.active) | {user_id: .id, username: .name}'
```

*Output:*

```json ln:False
{
  "user_id": 1,
  "username": "Alice"
}
{
  "user_id": 3,
  "username": "Carol"
}
```

</br>

#### 2. Group by and Aggregate (Manual Grouping)

```bash ln:False
echo '[
  {"product": "A", "qty": 3},
  {"product": "B", "qty": 2},
  {"product": "A", "qty": 1}
]' | jq 'group_by(.product) | map({product: .[0].product, total: (map(.qty) | add)})'
```

*Output:*

```json ln:False
[
  {
    "product": "A",
    "total": 4
  },
  {
    "product": "B",
    "total": 2
  }
]
```

</br>

#### 3. Modify Keys and Values

```bash ln:False
echo '{"a": 1, "b": 2}' | jq 'with_entries({key: .key, value: (.value * 10)})'
```

*Output:*

```json ln:False
{
  "a": 10,
  "b": 20
}
```

</br>

#### 4. Convert to CSV

```bash ln:False
echo '[{"id":1,"name":"Alice"},{"id":2,"name":"Bob"}]' \
| jq -r '.[] | [.id, .name] | @csv'
```

*Output:*

```text ln:False
1,"Alice"
2,"Bob"
```

> [!info] To Raw CSV
> ```bash ln:False
> echo '[{"id":1,"name":"Alice"},{"id":2,"name":"Bob"}]' \
| jq -r '.[] | "\(.id),\(.name)"'
> ```
> ```text ln:False
> 1,Alice
> 2,Bob
> ```

</br>

#### 5. Use `--arg` to Pass Shell Variables

```bash ln:False
id=2
echo '[{"id":1,"name":"Alice"},{"id":2,"name":"Bob"}]' \
| jq --argjson id "$id" '.[] | select(.id == $id)'
```

*Output:*

```json ln:False
{
  "id": 2,
  "name": "Bob"
}
```

</br>

#### 6. Recursive Search for Keys

```bash ln:False
echo '{
  "a": 1,
  "b": {"id": 2},
  "c": {"nested": {"id": 3}}
}' | jq '.. | objects | select(has("id")) | .id'
```

*Output:*

```text ln:False
2
3
```

