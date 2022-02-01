# Сортировка сегментами + json
import json
import random
import time


def cmp_passport(a: dict, b: dict):
    return a['passport_number'] - b['passport_number']
    

def cmp_weight(a: dict, b: dict):
    return a['weight'] - b['weight']


def cmp_workexp(a: dict, b: dict):
    return a['work_experience'] - b['work_experience']


def isSorted(l: list):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True


level = 0
maxlevel = 0
def bucket_sort(ls: list, cmp):
    global level
    if level >= 100:
        print("Level limit detected")
        return
    print("level", level)
    if len(ls) < 2:
        return
    
    # equality
    eq_flag = True
    for i in ls:
        if cmp(ls[0], i) != 0:
            eq_flag = False
    if eq_flag:
        return ls
    
    # separate
    lp = []
    rp = []
    psep = ls[int(len(ls)/2)]
    for i in ls:
        if cmp(i, psep):
            lp.append(i)
        else:
            rp.append(i)
    
    # sort parts
    level += 1
    bucket_sort(lp, cmp)
    bucket_sort(rp, cmp)
    level -= 1

    # merge parts
    for i in rp:
        lp.append(i)
    ls = lp

def avg(ls: list):
    l: list
    l = ls.copy()
    while len(l) > 2:
        min = l[0]
        max = l[0]
        for i in l:
            if i < min:
                min = i
            if i > max:
                max = i
        l.remove(min)
        l.remove(max)
    return l[0]

# def is_eq(a: list, b: list):
#     if len(a) != len(b):
#         return False
#     for i in range(len(a)):
#         if a[i] != b[i]:
#             return False
#     return True

def isRepetitive(ls: list):
    for i in ls:
        if ls[0] != i:
            return False
    return True

def buck_sort(ls: list):
    global level, maxlevel
    if level > maxlevel:
        maxlevel = level
    if len(ls) < 2 or isRepetitive(ls):
        return ls.copy()
    
    lp = []
    rp = []
    sep = avg(ls)
    if sep == max(ls):
        sep = min(ls)
    for i in ls:
        if i<=sep:
            lp.append(i)
        else:
            rp.append(i)
    level += 1
    lp = buck_sort(lp)
    rp = buck_sort(rp)
    level -= 1
    for i in rp:
        lp.append(i)
    return lp


if __name__ == '__main__':
    # data = json.load(open('output.txt'))
    ts = [random.randint(0,10000) for i in range(10000)]
    try:
        # bucket_sort(data, cmp_passport)
        ts = buck_sort(ts)
        if isSorted(ts):
            print("Sort is done right!")
        else:
            print("Something is not right!")
        print("maxlevel =", maxlevel)
    except Exception as e:
        print(type(e), e)
