
def main():
    a = float(input("перше число ="))
    b = float(input("друге число ="))
    if a == b:
        print(f'a=b, перемножаєм числа ={a*a}')
    else:
        print(f'сума ={a+b}')
if __name__ == '__main__': main()