m = int(input('Введіть число від 1 до 20: '))
if m > 20 or m < 1:
    print("число не є вірним")
else:
    for row in range(1, m+1):
        for col in range(1, m+1):
            print(row * col, end='\t')
        print(" ")