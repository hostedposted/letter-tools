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
>>> from letter_tools import rand
>>> rand("a", "h")
c
>>> rand("a", "h")
g
>>> rand(1, 10)
5
>>> rand(1, 10)
7
```
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
>>> from letter_tools import Range
>>> for i in Range("i"):
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

>>> for i in Range("d", "g"):
...     print(i)
...
d
e
f
g

>>> for i in Range(1, 5):
...     print(i)
...
1
2
3
4
```