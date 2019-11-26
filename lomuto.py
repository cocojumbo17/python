def med3(A, low, high):
    mid = (low + high) // 2
    if A[low] < A[mid]:
        if A[mid] < A[high]:
            return mid
        elif A[low] < A[high]:
            return high
        else:
            return low
    elif A[mid] > A[high]:
        return mid
    elif A[low] < A[high]:
        return low
    else:
        return high

#def ninther_index(A, lo, hi):
#    A_cutted = A[lo : hi+1]
#    return A.index(med3([med3(A_cutted[ 0 : len(A_cutted)//3 ]), med3(A_cutted[ len(A_cutted)//3 : 2*len(A_cutted)//3 ]), med3(A_cutted[ 2*len(A_cutted)//3 : len(A_cutted) ])]))


def partition(A, low, high):
    ni = med3(A, low, high)
    pivot = A[ni]
    A[high], A[ni] = A[ni], A[high]
    i = low
    for j in range(low, high + 1):
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[high], A[i] = A[i], A[high]
    return i


def quicksort(A, low, high):
    if low<high:
        p = partition(A, low, high)
        quicksort(A, low, p-1)
        quicksort(A, p+1, high)

def convert_input(data_list):
    data_type = 0
    try:
        b = int(data_list[0])
        data_type = 1
    except ValueError:
        try:
            b = float(data_list[0])
            data_type = 2
        except ValueError:
            data_type = 0
    for i in range(len(data_list)):
        if data_type == 1:
            data_list[i] = int(data_list[i])
        elif data_type == 2:
            data_list[i] = float(data_list[i])

def main():
#    a = input().split()
#    convert_input(a)

    a1 = [10, 7, 20, 9,248, 5, 6, 4, 3, 2, 4, -3 , -44,7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,]
    a2 = [5, 4, 3, 2, 1]
    a3 = ['fuck', 'you', 'son', 'of', 'bitch']
    a1 = [0.0, 17.0, 2.0, 13.6, 12.3, 5.2, 1.5, 15.0]
    quicksort(a1, 0, len(a1)-1)
    for i in range(len(a1)):
        print(a1[i], end=' ')


main()
