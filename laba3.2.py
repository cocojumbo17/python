
def merge(arr, start, mid, end, temp):
    start = min(len(arr), start)
    mid = min(len(arr), mid)
    end = min(len(arr), end)
    index_1 = start
    index_2 = mid
    while index_1 < mid and index_2 < end:
        if arr[index_1] < arr[index_2]:
            temp.append(arr[index_1])
            index_1 += 1
        else:
            temp.append(arr[index_2])
            index_2 += 1
    while index_1 < mid:
        temp.append(arr[index_1])
        index_1 += 1
    while index_2 < end:
        temp.append(arr[index_2])
        index_2 += 1


def merge_bottomup(arr):
    temp_arr = []
    width = 1
    while width < len(arr):
        for i in range(0, len(arr), 2 * width):
            start = i
            mid = i + width
            end = i + 2 * width
            merge(arr, start, mid, end, temp_arr)
        # copy from temporary array to our array
        for i in range(len(temp_arr)):
            arr[i] = temp_arr[i]
        temp_arr.clear()
        width *= 2

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
    a = input().split()
    convert_input(a)

    a1 = [10, 7, 20, 9,248, 5, 6, 4, 3, 2, 4, -3 , -44,7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,10, 7, 20, 9, 5, 6, 4, 3, 2, 4, 7, 0,]
    a2 = [5, 4, 3, 2, 1]
    a3 = ['fuck', 'you', 'son', 'of', 'bitch']
    a4 = [17.0, 2.0, 13.6, 12.3, 5.2, 1.5]
    merge_bottomup(a)
    for i in range(len(a)):
        print(a[i], end=' ')


main()
