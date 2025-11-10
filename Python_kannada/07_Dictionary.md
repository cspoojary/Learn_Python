## Dictionaries in Python

A **dictionary** in Python is a collection of key-value pairs. Each key
in a dictionary is associated with a value, and you can retrieve or
manipulate data using the key. Unlike lists and tuples, dictionaries are
**unordered** and **mutable** (changeable).

---
## 1. Creating a Dictionary

You can create a dictionary using curly braces `{}` or the `dict()`
function.

### Syntax:

``` python
my_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}
```

### Example:

Let's create a dictionary of famous cities in Karnataka and their
popular dishes.

``` python
karnataka_food = {
    "Bengaluru": "Bisi Bele Bath",
    "Mysuru": "Mysore Pak",
    "Mangaluru": "Neer Dosa"
}
```

------------------------------------------------------------------------

## 2. Accessing Dictionary Elements

To access the values stored in a dictionary, you use the key.

``` python
print(karnataka_food["Mysuru"])  # Output: Mysore Pak
```

You can also use the `get()` method to access values, which is safer
because it doesn't throw an error if the key doesn't exist.

``` python
print(karnataka_food.get("Mangaluru"))  # Output: Neer Dosa
print(karnataka_food.get("Shivamogga", "Not Found"))  # Output: Not Found
```

------------------------------------------------------------------------

## 3. Adding and Updating Dictionary Elements

You can add new key-value pairs or update existing values in a
dictionary.

### Adding an Item:

``` python
karnataka_food["Shivamogga"] = "Kadubu"
print(karnataka_food)
```

### Updating an Item:

``` python
karnataka_food["Bengaluru"] = "Ragi Mudde"
```

------------------------------------------------------------------------
