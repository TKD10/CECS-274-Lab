import random
import ArrayList

def linear_search(a : ArrayList.ArrayList, x):
    # todo
    for i in range(a.size()):
        if x == a[i]:  # if doesnt work use a.get(i)
            return i
    return -100


def binary_search(a : ArrayList.ArrayList, x):
    # todo
    l = 0
    r = len(a) - 1
    while l <= r:
        m = (l + r) // 2
        if a[m] == x:
            return m
        elif x < a[m]:
            r = m - 1
        elif x > a[m]:
            l = m + 1
    return -100


def _merge(a0 : ArrayList.ArrayList, a1 : ArrayList.ArrayList, a : ArrayList.ArrayList):
    # todo
    i0 = 0
    i1 = 0

    for i in range(len(a)):
        if i0 >= a0.size():
            a[i] = a1[i1]  # try a[i] = a1[i1] if not working
            i1 += 1
        elif i1 >= a1.size():
            a[i] = a0[i0]
            i0 += 1
        elif a0[i0] <= a1[i1]:
            a[i] = a0[i0]
            i0 += 1
        else:
            a[i] = a1[i1]
            i1 += 1

    pass

def merge_sort(a : ArrayList.ArrayList):
    # todo
    if len(a) <= 1:
        return
    m = len(a) // 2
    a0 = ArrayList.ArrayList()
    a1 = ArrayList.ArrayList()
    for i in range(m):
        a0.append(a.get(i))
    for i in range(m, len(a)):
        a1.append(a.get(i))
    merge_sort(a0)
    merge_sort(a1)
    _merge(a0, a1, a)
    return



def _partition_f(a : ArrayList, start, end):
    l = start + 1
    r = end
    p = a[start]
    overlap = False
    while not overlap:
        while l <= r and a[l] <= p:
            l += 1
        while r >= l and a[r] >= p:
            r -= 1
        if r < l:
            overlap = True
        else:
            temp = a[l]
            a[l] = a[r]
            a[r] = temp
    a[start] = a[r]
    a[r] = p
    return r


def _partition_r(a : ArrayList, start, end):
    index = random.randint(start,end)
    random_element = a[index]
    a[index] = a[start]
    a[start] = random_element
    l = start + 1
    r = end
    p = a[start]
    overlap = False
    while not overlap:
        while l <= r and a[l] <= p:
            l += 1
        while r >= l and a[r] >= p:
            r -= 1
        if r < l:
            overlap = True
        else:
            temp = a[l]
            a[l] = a[r]
            a[r] = temp
    a[start] = a[r]
    a[r] = p
    return r


def _quick_sort_f(a : ArrayList.ArrayList, start, end):
    # todo
    if start < end:
        p = _partition_f(a, start, end)
        _quick_sort_f(a, start, p - 1)
        _quick_sort_f(a, p + 1, end)


def _quick_sort_r(a : ArrayList.ArrayList, start, end):
    # todo
    if start < end:
        p = _partition_r(a, start, end)
        _quick_sort_r(a, start, p - 1)
        _quick_sort_r(a, p + 1, end)


def quick_sort(a : ArrayList.ArrayList, p=True):
    """
    sorts an ArrayList a using the quick sort algorithm.
    If parameter p is True, the quick sort algorithm uses a randomly chosen element from a as pivot.
    Otherwise, the quick sort algorithm uses the first element as pivot.
    """
    if p:
        _quick_sort_r(a, 0, a.size()-1)
    else:
        _quick_sort_f(a, 0, a.size()-1)


    
