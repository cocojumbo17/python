
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


def selection_sort(a):
    size = len(a)
    for i in range(0, size-1):
        for j in range(i+1, size):
            if a[j] < a[i]:
                a[j], a[i] = a[i], a[j]

def main():
    array = input().split()
    convert_input(array)
    selection_sort(array)
    for i in range(len(array)):
        print(array[i], end=' ')


main()
