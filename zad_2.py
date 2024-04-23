def forall(pred, iterable):
    for i in iterable:
        if not pred(i): return False
    return True


def exist(pred, iterable):
    for i in iterable:
        if pred(i): return True
    return False


def atleast(n, pred, iterable):
    k = 0;
    for i in iterable:
        if pred(i):
            k += 1
            if k >= n: return True
    return False


def atmost(n, pred, iterable):
    k = 0;
    for i in iterable:
        if pred(i):
            k += 1
            if k >= n: return False
    return False
