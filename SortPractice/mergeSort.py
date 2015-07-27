__author__ = 'WEI'


def merge_sort(a, n):
    if n == 1:
        return a
    else:
        b = a[0:int(n/2)]
        c = a[int(n/2):n]
        d = merge_sort(b, int(n/2))
        e = merge_sort(c, len(c))
        f = merge(d, e)
        return f


def merge(b, c):
    len_b = len(b)
    len_c = len(c)
    f = []
    i = 0
    j = 0

    for k in range(len_b + len_c):
        if i < len_b and j < len_c:
            if b[i] < c[j]:
                f.append(b[i])
                i += 1
            else:
                f.append(c[j])
                j += 1
        if i >= len_b and j < len_c:
            f.append(c[j])
            j = j + 1
        if j >= len_c and i < len_b:
            f.append(b[i])
            i += 1
        if i >= len_b and j > len_c:
            raise ValueError('index out of range during merge function.')

    return f