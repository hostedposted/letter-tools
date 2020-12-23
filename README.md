# Letter Tools
This is a very simple module that allows you to randomly get letters and make letter for loops.

# Installing
To install use this command:
```
$ pip install letter-tools
```

# Examples
First an example for randomly picking a letter.
```py
>>> from letter_tools import randlet
>>> randlet("a", "h")
c
>>> randlet("a", "h")
g
```
as you can above see each time it randomly picks a letter from your range.
Another example for randomly picking a letter out of numbers.

```py
>>> from letter_tools import randlet
>>> randlet(4, 8)
h
>>> randlet(5, 7)
e
```

Next an example for ranges.

```py
>>> from letter_tools import letter
>>> for i in letter("i"):
...     print(i)
...
a
b
c
d
e
f
g
h
i

>>> for i in letter("d", "g"):
...     print(i)
...
d
e
f
g
```