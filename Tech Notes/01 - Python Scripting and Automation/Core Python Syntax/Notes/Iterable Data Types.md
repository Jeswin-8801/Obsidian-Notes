
# Lists

- **Ordered** - They maintain the order of elements.
- **Mutable** - Items can be changed after creation.
- **Allow duplicates** - They can contain duplicate values.

```python
fruits = ['apple', 'banana', 'orange']
mixed_list = [42, 'hello', 3.14, [1, 2, 3]]
```

| Function                                                                          | Description                                                    |
| --------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| [append()](https://www.programiz.com/python-programming/methods/list/append)      | Adds an item to the end of the list                            |
| [extend(list2)](https://www.programiz.com/python-programming/methods/list/extend) | Adds items of lists and other iterables to the end of the list |
| [insert(index)](https://www.programiz.com/python-programming/methods/list/insert) | Inserts an item at the specified index                         |
| [remove(item)](https://www.programiz.com/python-programming/methods/list/remove)  | Removes the specified value from the list                      |
| [pop(index)](https://www.programiz.com/python-programming/methods/list/pop)       | Returns and removes item present at the given index            |
| [clear()](https://www.programiz.com/python-programming/methods/list/clear)        | Removes all items from the list                                |
| [index(item)](https://www.programiz.com/python-programming/methods/list/index)    | Returns the index of the first matched item                    |
| [count()](https://www.programiz.com/python-programming/methods/list/count)        | Returns the count of the specified item in the list            |
| [sort()](https://www.programiz.com/python-programming/methods/list/sort)          | Sorts the list in ascending/descending order                   |
| [reverse()](https://www.programiz.com/python-programming/methods/list/reverse)    | Reverses the item of the list                                  |
| [copy()](https://www.programiz.com/python-programming/methods/list/copy)          | Returns the shallow copy of the list                           |

- using the `list()` function
```python
>>> list(range(1, 4))
[1, 2, 3]
>>> list({1, 2, 2, 2, 3})
[1, 2, 3]
>>> list( (1, 2, 3) )
[1, 2, 3]
```

- delete from index
```python
>>> my_list = [1, 2, 3, 4, 5]
>>> del my_list[0]
>>> my_list
[2, 3, 4, 5]
```

- remove duplicates
```python
>>> my_list = [1, 2, 2, 3, 5]
>>> my_set = set(my_list)
>>> my_set
{1, 2, 3, 5}
```


---

# Tuples

- **Ordered** - They maintain the order of elements.
- **Immutable** - They cannot be changed after creation.
- **Allow duplicates** - They can contain duplicate values.

```python
numbers = (1, 2, -5, 1)
```

> No methods as it is immutable

```python
>>> list1 = [1, 2, 3]
>>> list2 = [4, 5, 6]
>>> t = (*list1, *list2)
>>> t
(1, 2, 3, 4, 5, 6)
```

> The leading `*` operator unpacks the lists into individual elements

- multiple assignment
```python
>>> person = ('Erik', 38, True)
>>> name, age, registered = person
>>> name
'Erik'
```


---

# Set

- **Unordered** - No indexing present.
- **Mutable** - Items can be changed after creation.
- **Allow duplicates** - They can contain duplicate values.

```python
student_id = {112, 114, 116, 118, 115}

# create an empty set
empty_set = set()
```

| Function                                                                               | Description                                                                                          |
| -------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| [all()](https://www.programiz.com/python-programming/methods/built-in/all)             | Returns `True` if all elements of the set are true (or if the set is empty).                         |
| [any()](https://www.programiz.com/python-programming/methods/built-in/any)             | Returns `True` if any element of the set is true. If the set is empty, returns `False`.              |
| [enumerate()](https://www.programiz.com/python-programming/methods/built-in/enumerate) | Returns an enumerate object. It contains the index and value for all the items of the set as a pair. |
| [len()](https://www.programiz.com/python-programming/methods/built-in/len)             | Returns the length (the number of items) in the set.                                                 |
| [max()](https://www.programiz.com/python-programming/methods/built-in/max)             | Returns the largest item in the set.                                                                 |
| [min()](https://www.programiz.com/python-programming/methods/built-in/min)             | Returns the smallest item in the set.                                                                |
| [sorted()](https://www.programiz.com/python-programming/methods/built-in/sorted)       | Returns a new sorted list from elements in the set(does not sort the set itself).                    |
| [sum()](https://www.programiz.com/python-programming/methods/built-in/sum)             | Returns the sum of all elements in the set.                                                          |

- difference
```python
A = { 1, 2, 3, 4, 5 }
B = { 3, 4, 5, 6, 7 }

print(A-B)
# {1, 2}

# And the reverse
print(B-A)
# {6, 7}
```

```python
A = { 1, 2, 3, 4, 5 }
B = { 3, 4, 5, 6, 7 }

# A + B - (A ∩ B)
print(A^B)
# {1, 2, 6, 7}

# A ∩ B
print(A & B)
# {3, 4, 5}

print(A|B)
# {1, 2, 3, 4, 5, 6, 7}
```

---

# Dictionary

```python
# creating a dictionary
country_capitals = {
  "Germany": "Berlin", 
  "Canada": "Ottawa", 
  "England": "London"
}

# tuple as a key
my_dict = {(1, 2): "one two", 3: "three"}
```

> Keys of a dictionary must be immutable
> Keys of a dictionary must be unique

|Function|Description|
|---|---|
|[pop()](https://www.programiz.com/python-programming/methods/dictionary/pop)|Removes the item with the specified key.|
|[update()](https://www.programiz.com/python-programming/methods/dictionary/update)|Adds or changes dictionary items.|
|[clear()](https://www.programiz.com/python-programming/methods/dictionary/clear)|Remove all the items from the dictionary.|
|[keys()](https://www.programiz.com/python-programming/methods/dictionary/keys)|Returns all the dictionary's keys.|
|[values()](https://www.programiz.com/python-programming/methods/dictionary/values)|Returns all the dictionary's values.|
|[get()](https://www.programiz.com/python-programming/methods/dictionary/get)|Returns the value of the specified key.|
|[popitem()](https://www.programiz.com/python-programming/methods/dictionary/popitem)|Returns the last inserted key and value as a tuple.|
|[copy()](https://www.programiz.com/python-programming/methods/dictionary/copy)|Returns a copy of the dictionary.|

```python
# print dictionary keys one by one
for country in country_capitals:
    print(country)

# print dictionary values one by one
for country in country_capitals:
    capital = country_capitals[country]
    print(capital)
```




