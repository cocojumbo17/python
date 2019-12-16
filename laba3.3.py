def median3a(A, begin, mid, end):
    if A[begin] < A[mid]:
        if A[mid]< A[end]:
            return mid
        elif A[begin]<A[end]:
            return end
        else:
            return begin
    else:
        if A[end]<A[mid]:
            return mid
        elif A[end]<A[begin]:
            return end
        else:
            return begin


def tukeysNinther(A, low, high):
    if low<high:
        N = high-low+1
        delta = N//6
        mediana_1 = median3a(A, low, low+delta, low+2*delta)
        mediana_2 = median3a(A, low+2*delta, low+3*delta, low+4*delta)
        mediana_3 = median3a(A, high-2*delta, high-delta, high)
        mediana = median3a(A, mediana_1, mediana_2, mediana_3)
        return mediana
    else:
        return high

def partition(A, low, high):
    pivot = A[tukeysNinther(A, low, high)]
    L=[]
    R=[]
    M=[]
    for j in range(low, high):
        if A[j] < pivot:
            L.append(A[j])
        elif A[j] == pivot:
            M.append(A[j])
        else:
            R.append(A[j])
    A = L+M+R
    return len(L)

def quicksort(A):
    if len(A) > 1:
        pivot = A[tukeysNinther(A, 0, len(A)-1)]
        L = []
        R = []
        M = []
        for j in range(len(A)):
            if A[j] < pivot:
                L.append(A[j])
            elif A[j] == pivot:
                M.append(A[j])
            else:
                R.append(A[j])
        quicksort(L)
        quicksort(R)
        k=0
        for x in L + M + R:
            A[k] = x
            k+=1

def main():
    a = input().split()
    a = [int(j) for j in a]
    quicksort(a)
    for j in a:
        print(j, end=' ')

main()