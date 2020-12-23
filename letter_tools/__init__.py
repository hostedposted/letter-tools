import random

def letter(a = 1, b = 1):
    re = """
abcdefghijklmnopqrstuvwxyz
"""
    if b == 1:
        b = a
        a = 1
    letter_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    n = 0
    for i in letter_list:
        n += 1
        if i == b:
            b = n
        if i == a:
            a = n
    if a > 26:
        raise Exception(str(a)+" is more then 26 and is invalid")
    if b > 26:
        raise Exception(str(b)+" is more then 26 and is invalid")
    full = "".join(re.split())
    full = full[0:]
    b = int(b)
    if a != 1:
        return full[a - 1:b]
    return  full[a - 1:b]

def randlet(a = 1, b = 1):
    re = """
abcdefghijklmnopqrstuvwxyz
"""
    if b == 1:
        b = a
        a = 1
    letter_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    n = 0
    for i in letter_list:
        n += 1
        if i == b:
            b = n
        if i == a:
            a = n
    if a > 26:
        raise Exception(str(a)+" is more then 26 and is invalid")
    if b > 26:
        raise Exception(str(b)+" is more then 26 and is invalid")
    full = "".join(re.split())
    full = full[0:]
    b = int(b)
    a -= 1
    b -= 1
    print(full[random.randint(a, b)])
