

# Letter Tools
[![Downloads](https://pepy.tech/badge/letter-tools/month)](https://pepy.tech/project/letter-tools)

- [Letter Tools](#letter-tools)
- [Intro](#intro)
- [Installing](#installing)
- [Examples](#examples)
- [Usage](#usage)


# Intro

This is a collection of tools for doing stuff with letters.

With a randint for letters and a range for letters and more.

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

Now an example for word score.

```py
# Find the score of a word a=1, b=2 and add up the numbers for all the letters

>>> from letter_tools import word_score
>>> print(word_score("hi")) 
17
>>> print(word_score("letter"))       
80
>>> print(word_score("hi", opt="")) 
37  
>>> print(word_score("letter", opt="")) 
82  
```

Here we will use the scrabble score, it does almost the same thing as word score but it uses scrabble scoring rules.  a: 1, b: 3, c: 3, d: 2, e: 1, f: 4, g: 2, h: 4, i: 1, j: 8, k: 5, l: 1, m: 3, n: 1, o: 1, p: 3, q: 10, r: 1, s: 1, t: 1, u: 1, v: 4, w: 4, x: 8, y: 4, z: 10
```py
>>> from letter_tools import scrabble_score
>>> print(scrabble_score("hi")) 
5   
>>> print(scrabble_score("letter")) 
6   
```

Now for the derandomize and randomize functions.

```py
>>> # For this we will use a word 'welcome' and randomize it.
>>> from letter_tools import randomize
>>> randomize("welcome") 
'mlcoeew'
>>> # Now we will derandomize 'mlcoeew' 
>>> from letter_tools import derandomize
>>> derandomize("mlcoeew") 
['welcome']
```

# Usage

Word score could help you with making a game to find certain scored words. Here is an example for 100 scored words. This will not eliminate invalid words.

```py
from letter_tools import word_score

while True:
    word = input("Could you give me some words that add up to 100 exactly?\na=1, b=2 and so on\n")
    if word_score(word) == 100:
        print(f"{word} is a 100 letter word correct!!!")
        break
    else:
        print(f"{word} is a {word_score(word)} not a 100 letter word wrong.")
```

We could also make a script to find 100 scored words.
For this we will use the requests library and using [Dwyl's english word set](https://github.com/dwyl/english-words) I generated a json you could use for this.

This is the code:

```py
from letter_tools import word_score
import requests

words = requests.get("https://raw.githubusercontent.com/hostedposted/letter-tools/master/words.json").json()
for i in words:
    try:
        if word_score(i) == 100:
            print(i)
    except KeyError:
        pass
```