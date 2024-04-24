def forall(pred, iterable):
    for i in iterable:
        if not pred(i): return False
    return True


def forall_all(pred, iterable):
    return all(pred(item) for item in iterable)


def exist(pred, iterable):
    for i in iterable:
        if pred(i): return True
    return False


def exist_any(pred, iterable):
    return any(pred(item) for item in iterable)


def atleast(n, pred, iterable):
    k = 0;
    for i in iterable:
        if pred(i):
            k += 1
            if k >= n: return True
    return False


def atleast_sum(n, pred, iterable):
    count = sum(1 for item in iterable if pred(item))
    return count >= n


def atmost(n, pred, iterable):
    k = 0;
    for i in iterable:
        if pred(i):
            k += 1
            if k >= n: return False
    return False

def atmost_sum(n, pred, iterable):
    count = sum(1 for item in iterable if pred(item))
    return count < n