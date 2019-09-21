def factoriaal(num):
    if num == 1:
        return 1
    else:
        return num*factoriaal(num-1)
print(factoriaal(10))