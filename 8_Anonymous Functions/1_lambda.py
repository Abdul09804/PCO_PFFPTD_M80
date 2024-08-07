# lambda
"""
-> Syntax:
            lambda arguments: expression
"""

def even(num):
    return num % 2 == 0


print(even(7))     # False
print(even(78))   # True

_even = lambda num: num % 2 == 0
print(_even(7))
print(_even(88))    # True

def square(num):
    return num ** 2

_square = lambda num: num **2
print(_square(6))   # 36

# square and cube of a number
sq_cube = lambda num: (num**2, num**3)
print(sq_cube(7))       # (49, 343)

# num and it's factorial

from math import factorial
fact = lambda num: (num, factorial(num))
print(fact(7))      # (7, 5040)

# lambda expression to check if a string is starting with a vowel
check = lambda st: st[0] in 'aeiouAEIOU'
print(check('arati'))       # True

# expression to check if a string is a palindrome
check = lambda st: st == st[::-1]
print(check('madam'))

# expression to check if a value is in collection
check = lambda val, coll: val in coll
print(check('s', 'mister'))
print(check(9, [10, 19, 91]))

# expression to return last value of the sequence
last_val = lambda seq: seq[-1]
print(last_val('python'))   # 'n'
print(last_val([10, 20, 30]))   # 30

# lambda expression to return square of a number if the number is even else return cube of a number
res = lambda num: num**2 if num % 2 == 0 else num**3
print(res(8))   # 64
print(res(7))   # 343



