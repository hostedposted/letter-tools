import random

def range(a = 1, b = 1, step=1):
    if isinstance(step, int) == False:
        raise Exception(f"step is {type(step)} and is thus invalid.")
    if isinstance(a, int) == True:
        if b == 1:
            b = a
            a = 0
        if a == b: 
            return a
        else: 
            res = []
            num1, num2 = a, b
            while(a < b+1): 
                res.append(a) 
                a += 1
            return res[num1 - 1:num2:step]
    elif isinstance(a, str) == True:
        if b == 1:
            b = a
            a = 1
        re = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"""
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
        if a != 1:
            return full[a - 1:b:step]
        return  full[a - 1:b:step]
    else:
        raise Exception("int or str are required.")


def rand(a = 1, b = 1):
    if isinstance(a, int) == True:
        print(random.randint(a, b))
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
