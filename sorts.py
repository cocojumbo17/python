def sort_insert(A):
    """insert sort"""
    N = len(A)
    #    print(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k - 1] > A[k]:
            A[k - 1], A[k] = A[k], A[k - 1]
            k -= 1


#            print(top, ":", A, end="")
#            print()

def sort_choice(A):
    """choice sort"""
    N = len(A)
    #    print(A)
    for top in range(0, N - 1):
        for k in range(top + 1, N):
            if A[top] > A[k]:
                A[top], A[k] = A[k], A[top]


#            print(top, ":", A, end="")
#            print()

def sort_bubble(A):
    """bubble sort"""
    N = len(A)
    #    print(A)
    for bypass in range(1, N):
        for k in range(0, N - bypass):
            if A[k] > A[k + 1]:
                A[k + 1], A[k] = A[k], A[k + 1]


#            print(k, ":", A, end="")
#            print()

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


if __name__ == '__main__' : test()

