
def fractation(x):
    """find all fractations of number
    :param x: positive integer number
    :return: none
    """
    dev=2
    while x>1:
        if x%dev == 0:
            x //= dev
            print(f"{dev}", end=' ')
        else:
            dev += 1

def main():
    x=int(input('X='))
    fractation(x)
    return 0
    n=int(input('Enter number in 10-system: '))
    base=int(input('Enter base of system to convert this number: '))
    res=''
    while n>0:
        digit = n%base
        if digit >= 10:
            digit = chr(ord('A')+digit-10)
        res += str(digit)
        n //= base
    print(f'{res[::-1]}')




if __name__=='__main__':main()