def ruksak():
    mass = [1, 2, 1, 2, 1,3,2,4,3,3]
    val = [2, 2, 5, 3, 1,5,2,7,3,3]
    N = len(mass)
    mass_of_ruksak = 8
    F = [[0] * (N + 1) for i in range(mass_of_ruksak + 1)]
    Who = [[''] * (N + 1) for i in range(mass_of_ruksak + 1)]
    for curr_weight in range(1, mass_of_ruksak + 1):
        for i in range(1, N + 1):
            curr_item = i - 1
            if mass[curr_item] <= curr_weight:
                prev_value = F[curr_weight][i - 1]
                weight_without_us = curr_weight - mass[curr_item]
                value_without_us = F[weight_without_us][i - 1]
                new_value = val[curr_item] + value_without_us
                if new_value > prev_value:
                    F[curr_weight][i] = new_value
                    if value_without_us > 0:
                        new_who = Who[weight_without_us][i - 1] + ' ' + str(i)
                    else:
                        new_who = str(i)
                    Who[curr_weight][i] = new_who
                else:
                    F[curr_weight][i] = prev_value
                    Who[curr_weight][i] = Who[curr_weight][i - 1]
            else:
                F[curr_weight][i] = F[curr_weight][i - 1]
                Who[curr_weight][i] = Who[curr_weight][i - 1]
    #print(F)
    #print(Who)
    print('We should take', Who[mass_of_ruksak][N])
    print('In this case value will be', F[mass_of_ruksak][N])


ruksak()
