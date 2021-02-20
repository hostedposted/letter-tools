"""Module for doing stuff with letters."""
import random
import requests

def range(start = 1, stop = 1, step = 1):
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
        raise Exception("step is {} and is thus invalid.".format(type(step)))
    if isinstance(start, int) == True:
        if start == 1 and stop == 1:
            return [1]
        else:
            if stop == 1:
                stop = start
                start = 0
            if start == stop:
                return [start]
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
    """Randomly pick letters or numbers from a range. 
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

def word_score(word, opt=None):
    """
    Count up the score of a word. a=1, b=2, c=3
    Args:
        word: the word to get the score of
        opt: if opt does not equal None z will be 1 and a will be 26
    Returns:
        The score of the word
    
    Raises:
        KeyError: character is invalid
    """
    if opt == None:
        arr = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
        score = 0
        for i in list(word):
            score += arr[i]
        
        return score
    else:
        arr = {'a': 26, 'b': 25, 'c': 24, 'd': 23, 'e': 22, 'f': 21, 'g': 20, 'h': 19, 'i': 18, 'j': 17, 'k': 16, 'l': 15, 'm': 14, 'n': 13, 'o': 12, 'p': 11, 'q': 10, 'r': 9, 's': 8, 't': 7, 'u': 6, 'v': 5, 'w': 4, 'x': 3, 'y': 2, 'z': 1}
        score = 0
        for i in list(word):
            score += arr[i]
        
        return score

def scrabble_score(word):
    """
    Count up the score of a word in scrabble points.
    
    Args:
        word: the word to get the score of
    Returns:
        The score of the word in scrabble points

    Raises:
        KeyError: character is invalid
    """
    arr = {'a': 1,'b': 3,'c': 3,'d': 2,'e': 1,'f': 4,'g': 2,'h': 4,'i': 1,'j': 8,'k': 5,'l': 1,'m': 3,'n': 1,'o': 1,'p': 3,'q': 10,'r': 1,'s': 1,'t': 1,'u': 1,'v': 4,'w': 4,'x': 8,'y': 4,'z': 10}
    score = 0
    for i in list(word):
        score += arr[i]
    
    return score

def randomize(word):
    """
    Mix up the letters in a word.
    Args:
        word: the word to be changed
    Results:
        The word in a different order
    """

    letters = list(word)
    return "".join(random.sample(letters,len(letters)))


def derandomize(Word):
    """
    Show all possible words that Word can be.
    Args:
        Word: the word to be derandomized
    Results:
        All valid words with the same letters
    """
    Word = list(Word)
    words = requests.get("https://raw.githubusercontent.com/hostedposted/letter-tools/master/words.json").json()
    arr = []
    for word in words:
        flag = 1
        chars = []
        charsd = {}
        for i in word:
            charsd[i] = charsd.get(i, 0) + 1
            chars.append(i)
        # The commented code is still in beta.
        #count = -1
        for key in chars:
            #count += 1
            if flag == 0:
                break
            if key not in Word:
                flag = 0
            else:
                if Word.count(key) != charsd[key]:
                    flag = 0
            #if "?" in Word:
                #word_indice = [i for i, x in enumerate(Word) if x == '?']
                #if count in word_indice:
                    #flag = 1
        if len(word) != len(Word):
            flag = 0
        if flag == 1:
            arr.append(word)
    return arr

def custom_score(word, opt):
    """Make your custom word score. Just put in a dictionary each letter being assigned a score.
    Args:
        word: the word to get the score of
        opt: the options to use.
    Retuns:
        The word in the score opt gave.
    Raises:
        Exception: if opt is not a dict
    """
    if isinstance(opt, dict) == False:
        raise Exception("options are not a dict.")
    score = 0
    for i in list(word):
        score += opt[i]
        
    return score