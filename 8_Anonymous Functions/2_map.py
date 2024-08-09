# maps

nums = [10, 20, 30, 40]

square = lambda num: num**2
res = []
for num in nums:
    res.append(square(num))
print(res)

"""
-> Syntax:
        map_object = map(func_name, iterable)
-> each value from the iterable will be given as a input to the function
-> The return from the function will be stored in map object
-> map doesn't have a proper structure to display the outputso we make use of typecasting
"""

_res = map(square, nums)
print(_res)     # <map object at 0x00000188803893F0>
print(list(_res))   # [100, 400, 900, 1600]
print(type(_res))   # <class 'map'>

_res2 = map(lambda num: num**2, nums)
print(list(_res2))  # [100, 400, 900, 1600]

# square and cube of all the numbers from 1 to 10
sq_cube = lambda num: (num**2, num**3)
res1 = map(sq_cube, range(1, 11))
print(list(res1))

res2 = map(lambda num: (num**2, num**3), range(1, 11))
print(list(res2))

#########################################################################################


l1 = [1, 2, 3, 4]
l2 = ['a', 'b', 'c', 'd']
# o/p = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

p = lambda item1, item2: (item1, item2)
print(p(1, 'a'))    # (1, 'a')

res = map(lambda item1, item2: (item1, item2), l1, l2)
print(list(res))        # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

l1 = [1, 2, 3, 4]
l2 = ['a', 'b', 'c']
res = map(lambda item1, item2: (item1, item2), l1, l2)
print(list(res))    # [(1, 'a'), (2, 'b'), (3, 'c')]

##########################################################################################

# WAP to print the list of numbers and its factorial between the range 1 to 10

from math import factorial
num_fact = map(lambda num: (num, factorial(num)), range(1, 11))
print(list(num_fact))

# WAP to get the factorial of numbers from 1 to 10

fact = map(factorial, range(1, 11))
print(list(fact))

# WAP to get the following output
words = ['hello', 'good', 'morning']
# o/p1 = [5, 4, 7]
# o/p2 = ['HELLO', 'GOOD', 'MORNING']

out1 = map(len, words)
print(list(out1))       # [5, 4, 7]

out2 = map(str.upper, words)
print(list(out2))       # ['HELLO', 'GOOD', 'MORNING']

nums = [3, -78, -65, 978, -64, 765, -7]
#o/p = [3, 78, 65, 978, 64, 765, 7]
out = map(abs, nums)
print(list(out))        # [3, 78, 65, 978, 64, 765, 7]






