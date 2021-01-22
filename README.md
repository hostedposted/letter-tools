# Letter Tools
[![Downloads](https://pepy.tech/badge/letter-tools/month)](https://pepy.tech/project/letter-tools)
This is a very simple module that allows you to randomly get letters and make letter for loops.

# Installing
To install use this command:
```shell
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
>>> from letter_tools import range
>>> for i in range("i"):
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

>>> for i in range("d", "g"):
...     print(i)
...
d
e
f
g

>>> for i in range(1, 5):
...     print(i)
...
1
2
3
4
5

#Using step

>>> for i in range(1, 5, 3):
...     print(i)
...
1
4

>>> for i in range("d", "g", 3):
...     print(i)
...
d
g
```