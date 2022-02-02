# Сортировка сегментами + json
import json
import random
from textwrap import indent
import time
from tqdm import tqdm


def cmp_passport(a: dict, b: dict):
    return a['passport_number'] - b['passport_number']


def cmp_weight(a: dict, b: dict):
    return a['weight'] - b['weight']


def cmp_workexp(a: dict, b: dict):
    return a['work_experience'] - b['work_experience']


level = 0
maxlevel = 0


def isSorted(l: list, cmp):
    """
    Проверка, отсортирован ли список
    """
    for i in range(len(l)-1):
        if cmp(l[i], l[i+1]) > 0:  # l[i] > l[i+1]:
            return False
    return True


def isRepetitive(ls: list, cmp):
    """
    Проверка, состоит ли список из одинаковых элементов
    """
    for i in ls:
        if cmp(i, ls[0]) != 0:  # ls[0] != i:
            return False
    return True


def Max(ls: list, cmp):
    """
    Поиск максимального элемента из списка
    """
    mval = ls[0]
    for i in ls:
        if cmp(i, mval) > 0:
            mval = i
    return mval


def Min(ls: list, cmp):
    """
    Поиск минимального элемента из списка
    """
    mval = ls[0]
    for i in ls:
        if cmp(i, mval) < 0:
            mval = i
    return mval


def find_median(l: list, k, cmp):
    """
    Поиск медианного элемента списка
    """
    if len(l) < 3:
        return l[0]
    iseq = True
    for i in l:
        if cmp(i, l[0]) != 0:
            iseq = False
    if iseq:
        return l[0]

    # selecting pivot
    piv = random.choice(l)
    while piv == Max(l, cmp):
        piv = random.choice(l)

    # separating
    lp = []
    rp = []
    for i in l:
        if cmp(i, piv) <= 0:  # i <= piv:
            lp.append(i)
        else:
            rp.append(i)
    if len(lp) >= k:
        res = find_median(lp, k, cmp)
    else:
        res = find_median(rp, k - len(lp), cmp)
    return res


# def buck_sort(ls: list):
#     """
#     Сортировка сегментами для целых чисел
#     """
#     if len(ls) < 2 or isRepetitive(ls):
#         return ls.copy()

#     lp = []
#     rp = []
#     sep = find_median(ls, len(ls)//2)
#     if sep == max(ls):
#         sep = min(ls)
#     for i in ls:
#         if i <= sep:
#             lp.append(i)
#         else:
#             rp.append(i)

#     lp = buck_sort(lp)
#     rp = buck_sort(rp)

#     for i in rp:
#         lp.append(i)
#     return lp

def bucket_sort(ls: list, cmp):
    """
    Сортировка сегментами для записей
    """
    if len(ls) < 2 or isRepetitive(ls, cmp):
        return ls.copy()

    lp = []
    rp = []
    sep = find_median(ls, len(ls)//2, cmp)
    if sep == Max(ls, cmp):
        sep = Min(ls, cmp)
    for i in ls:
        if cmp(i, sep) <= 0:  # i <= sep:
            lp.append(i)
        else:
            rp.append(i)

    lp = bucket_sort(lp, cmp)
    rp = bucket_sort(rp, cmp)

    for i in rp:
        lp.append(i)
    return lp


if __name__ == '__main__':
    try:
        data: list
        data = json.load(open("output.txt"))
        print("data loaded")
        t_s = time.monotonic()
        data = bucket_sort(data, cmp_weight)
        print("sorting time:", round(time.monotonic() - t_s, 3), "sec")
        print("Sorted", isSorted(data, cmp_weight))
        json.dump(data, open("main3_result.txt", 'w'),
                  ensure_ascii=False, indent=4)
        print("data dumped")
        # data = json.load(open("main3_result.txt"))
        # for i in range(20):
        #     print("weight", data[i]['weight'])
    except Exception as e:
        print(type(e), e)
