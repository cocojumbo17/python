n = int(input('Введіть число від 1 до 20: '))
if n > 20 or n < 1:
    print("число не є вірним")
else:
    for row in range(1, n+1):
        for col in range(1, n+1):
            print(row * col, end='\t')
        print(" ")