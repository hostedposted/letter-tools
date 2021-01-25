"""
Module for doing stuff with letters.
"""
import random

def range(start = 1, stop = 1, step=1):
    """Find a range from one letter to another.
    
    Args:
        start: the start of the range,
        stop: the end of the range,
        step: each increment it goes up by
    
    Returns:
        the range from start to stop
    
    Raises:
        Exception: string start or string stop is above Z
        Exception: step is not integer and is thus invalid
        TypeError: str or int is required
    """
    if isinstance(step, int) == False:
        raise Exception(f"step is {type(step)} and is thus invalid.")
    if isinstance(start, int) == True:
        if stop == 1:
            stop = start
            start = 0
        if start == stop: 
            return start
        else: 
            res = []
            while start < stop + 1: 
                res.append(start) 
                start += 1
            return res[0:len(res):step]
    elif isinstance(start, str) == True:
        if stop == 1:
            stop = start
            start = 1
        re = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"""
        letter_list = list(re)
        n = 0
        for i in letter_list:
            n += 1
            if i == stop:
                stop = n
            if i == start:
                start = n
        if start > 52:
            raise Exception(str(start)+" is more then 52 and is invalid")
        if stop > 52:
            raise Exception(str(stop)+" is more then 52 and is invalid")
        full = "".join(re.split())
        full = full[0:]
        stop = int(stop)
        if start != 1:
            return full[start - 1:stop:step]
        return full[start - 1:stop:step]
    else:
        raise TypeError("int or str are required.")


def rand(a = 1, b = 1):
    """
    Randomly pick letters or numbers from a range. 
    Args:
        a: start letter/number in rand range
        b: start letter/number in rand range
    
    Returns:
        Randomly picked number from a to b
    
    Raises:
        Exception: a or b is more then Z

    """
    if isinstance(a, int) == True:
        return random.randint(a, b)
    else:
        re = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"""
        if b == 1:
            b = a
            a = 1
        letter_list = list(re)
        n = 0
        for i in letter_list:
            n += 1
            if i == b:
                b = n
            if i == a:
                a = n
        if a > 52:
            raise Exception(str(a)+" is more then 52 and is invalid")
        if b > 52:
            raise Exception(str(b)+" is more then 52 and is invalid")
        full = "".join(re.split())
        full = full[0:]
        b = int(b)
        a -= 1
        b -= 1
        return full[random.randint(a, b)]

def word_score(word):
    """
    Count up the score of a word. a=1, b=2, c=3
    Args:
        word: the word to get the score of
    Returns:
        The score of the word
    """
    arr = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    num = 0
    for i in list(word):
        num += arr[i]
    
    return num