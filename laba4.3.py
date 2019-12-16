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


def main():
    years = int(input())
    prices = list(map(int, input().split()))

    sorted_prices = list(prices)
    merge_bottomup(sorted_prices)

    difference = 1e99
    for i in range(1, len(sorted_prices)):
        delta = sorted_prices[i]-sorted_prices[i-1]
        if delta <= difference:
            sell_year = prices.index(sorted_prices[i - 1])
            buy_year = prices.index(sorted_prices[i])
            if buy_year < sell_year:
                difference = delta
    print(difference)


main()
