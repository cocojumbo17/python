def sort_insert(A):
    """insert sort"""
    N = len(A)
    iterations = 0;
    for top in range(1, N):
        k = top
        while k > 0 and A[k - 1] > A[k]:
            A[k - 1], A[k] = A[k], A[k - 1]
            k -= 1
            iterations += 1
    print('num of iteration=', iterations)


def sort_choice(A):
    """choice sort"""
    N = len(A)
    iterations = 0;
    for top in range(0, N - 1):
        for k in range(top + 1, N):
            if A[top] > A[k]:
                A[top], A[k] = A[k], A[top]
                iterations += 1
    print('num of iteration=', iterations)


def sort_bubble(A):
    """bubble sort"""
    N = len(A)
    iterations = 0;
    for bypass in range(1, N):
        for k in range(0, N - bypass):
            if A[k] > A[k + 1]:
                A[k + 1], A[k] = A[k], A[k + 1]
                iterations += 1
    print('num of iteration=', iterations)


def merge(a, b):
    """merge two sorted list into one"""
    new_size = len(a) + len(b)
    c = [0] * new_size
    ai = bi = ci = 0
    while ai < len(a) and bi < len(b):
        if a[ai] < b[bi]:
            c[ci] = a[ai]
            ci += 1
            ai += 1
        else:
            c[ci] = b[bi]
            ci += 1
            bi += 1
    while ai < len(a):
        c[ci] = a[ai]
        ci += 1
        ai += 1
    while bi < len(b):
        c[ci] = b[bi]
        ci += 1
        bi += 1
    return c

def sort_merge(a):
    """fast merge sort"""
    if (len(a)<=1):
        return
    middle = len(a)//2
    l=[a[i] for i in range(middle)]
    r=[a[i] for i in range(middle, len(a))]
    sort_merge(l)
    sort_merge(r)
    c = merge(l,r)
    for i in range(len(a)):
        a[i]=c[i]


def test_sort(method_sort):
    A = [4, 2, 5, 3, 1]
    A_sorted = [1, 2, 3, 4, 5]
    method_sort(A)
    print("test #1 of", method_sort.__doc__, end=" ")
    print("OK" if (A == A_sorted) else "FAIL")

    A = [4, 2, 2, 5, 4, 3, 1, 2]
    A_sorted = [1, 2, 2, 2, 3, 4, 4, 5]
    method_sort(A)
    print("test #2 of", method_sort.__doc__, end=" ")
    print("OK" if (A == A_sorted) else "FAIL")

    A = list(range(10, 20)) + list(range(10))
    A_sorted = list(range(20))
    method_sort(A)
    print("test #3 of", method_sort.__doc__, end=" ")
    print("OK" if (A == A_sorted) else "FAIL")

    A = []
    A_sorted = []
    method_sort(A)
    print("test #4 of", method_sort.__doc__, end=" ")
    print("OK" if (A == A_sorted) else "FAIL")

    A = [1]
    A_sorted = [1]
    method_sort(A)
    print("test #5 of", method_sort.__doc__, end=" ")
    print("OK" if (A == A_sorted) else "FAIL")


def test():
    test_sort(sort_insert)
    test_sort(sort_choice)
    test_sort(sort_bubble)
    test_sort(sort_merge)


if __name__ == '__main__': test()
