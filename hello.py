import re


def validate(password):
    good_length = 7 < len(password) < 21
    good_capital = re.search(r"[A-Z]", password)
    good_small = re.search(r"[a-z]", password)
    good_digit = re.search(r"[0-9]", password)
    good_1 = good_length
    good_2 = good_capital and good_digit and good_small

    if not good_1 and not good_2:
        print("Password length must be between 8 and 20 symbols. "
              "Password must contain at least one capital letter,"
              " at least one small letter and at least one digit")
    elif not good_1:
        print("Password length must be between 8 and 20 symbols")
    elif not good_2:
        print("Password must contain at least one capital letter, at least one small letter and at least one digit")
    else:
        print("Password is correct")
        return True

    return False


def test():
    r = validate('Abc12345')
    print("test 1 is", 'OK' if r else 'Fail')

    r = validate('Pass1')
    print("test 2 is", 'OK' if not r else 'Fail')

    r = validate('12345678')
    print("test 3 is", 'OK' if not r else 'Fail')

    r = validate('abc')
    print("test 4 is", 'OK' if not r else 'Fail')


def main():
    while True:
        pas = input("Enter a password: ")
        if validate(pas):
            break


#test()
main()