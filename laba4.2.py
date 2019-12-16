def Input():
     temp, details = list(map(int, input('Num of machines and details to produce:').split()))
     speed = list(map(int, input('Speeds of machines:').split()))
     return [details, speed]


def findMax(l):
    m = l[0]
    for e in l:
        if e > m:
            m = e
    return m


def detailsOnNDay(n, speeds):
    total = 0
    for s in speeds:
        total += (n//s)
    return total


def binarySearch(goal, speeds):
    low_days = 0
    high_days = findMax(speeds)*goal
    days = 0
    while low_days <= high_days:
        mid_days = (high_days + low_days) // 2
        details_done = detailsOnNDay(mid_days, speeds)
        if details_done >= goal:
            high_days = mid_days-1
            days = mid_days
        else:
            low_days = mid_days+1
    return days

def main2():
    [goal, speeds] = Input()
    days = binarySearch(goal, speeds)
    print(f'{goal} details will be produced in {int(days)} days')
    for i in range(1, days+1):
        print(f'{i}: {detailsOnNDay(i, speeds)}')


# def main():
#     nGoal = input().split()
#     n = int(nGoal[0])
#     goal = int(nGoal[1])
#     machines = list(map(int, input().rstrip().split()))
#     low = 1
#     high = 1e18
#     while low <= high:
#         mid = (low + high) // 2
#         details_done = 0
#         for i in range(0, n):
#             details_done += mid // machines[i]
#             if details_done >= goal:
#                 break
#         if details_done >= goal:
#             high = mid - 1
#             days = mid
#         else:
#             low = mid + 1
#     print(int(days))

main2()
