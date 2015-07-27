__author__ = 'WEI'


def brute_force_sort(A):
    for p in range(len(A)):
        brute_force_sublist_sort(A, p)
    return A


def brute_force_sublist_sort(A, p):
    for i in range(p + 1, len(A)):
        if A[i] < A[p]:
            swap(A, i, p)


def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp