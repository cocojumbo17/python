def main():
    n=0
    while(n>20 or n<2):
        n=int(input('N[2-20]='))
        for i in range(n+1):
            print()
            for j in range(n+1):
                if i == 0:
                    if j==0:
                        print('  |', end='')
                    elif j!=1:
                        print(f'{j:4}', end='')
                elif i==1:
                    if j==0:
                        print('----'*n, end='')
                else:
                    if j==0:
                        print(f'{i:2}|', end='')
                    elif j!=1:
                        print(f'{i*j:4}', end='')
if __name__=='__main__':main()