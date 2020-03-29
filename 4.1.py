import math


def getDict(s):
    char_dict = {}
    for char in s:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def getFreqOfFreq(dictionary):
    count_dict = {}
    for char, value in dictionary.items():
        if value in count_dict:
            count_dict[value] += 1
        else:
            count_dict[value] = 1
    return count_dict


def getMinMaxFreq(dictionary):
    min_count = list(dictionary.values())[0]
    max_count = list(dictionary.values())[0]
    for char, value in dictionary.items():
        if value < min_count:
            min_count = value
        if value > max_count:
            max_count = value
    return min_count, max_count


def isValid(dictionary):
    count_dict = getFreqOfFreq(dictionary)
    min_count, max_count = getMinMaxFreq(dictionary)
    if len(count_dict) == 1:
        return 'YES'
    elif len(count_dict) == 2:
        if count_dict[max_count] == 1 and max_count - min_count == 1:
            return 'YES'
        elif count_dict[min_count] == 1 and min_count == 1:
            return 'YES'
    return 'NO'


def main():
    s = input()
    dictionary = getDict(s)
    result = isValid(dictionary)
    print(result)



main()