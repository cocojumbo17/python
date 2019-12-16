def getMins(heights):
    min_h = 1e10
    min_index = -1
    for i in range(len(heights)):
        if heights[i] < min_h:
            min_h = heights[i]
            min_index = i
    return min_h, min_index


def getMaxSquare(heights):
    num_buildings = len(heights)
    if num_buildings == 0:
        return 0
    min_height, min_index = getMins(heights)
    curr_square = num_buildings*min_height
    left_square = getMaxSquare(heights[0:min_index])
    right_square = getMaxSquare(heights[min_index+1:])
    return max(curr_square,left_square,right_square)

def main():
    num_buildings = int(input())
    building_heights = list(map(int, input().split()))
    if len(building_heights) != num_buildings:
        print('Incorrect input data. Exit.')
    max_square = getMaxSquare(building_heights)
    print(max_square)


main()