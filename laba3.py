#!/bin/python3

import math
import os
import random
import re
import sys

print("Введіть бажану кількість символів")
l = length = int(input().strip())
print("Введіть кількість слів від 1 до 100 в перший список")
a = first_list = input().rstrip().split()
print("Введіть кількість слів від 1 до 100 в другий список")
b = second_list = input().rstrip().split()
first = [s for s in a if len(s) == l and s not in b]
second = [s for s in b if len(s) == l and s not in a]
if 1 <= len(a) <= 100 and 1 <= len(b) <= 100:
    print(first + second)
else:
    print("Ви ввели не вірну кількість слів."
          "Введіть кількість слів від 1 до 100 в кожен стовпчик.")
