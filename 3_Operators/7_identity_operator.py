# Identity Operator
"""
-> It is used to check whether 2 operands are pointing to the same address
-> 1) is operator
   2) is not operator
"""

# 1) is operator
"""
-> It is an operator which gives the result as True if both the operands are pointing to
   the same address.
"""

a = 10
b = 10
c = 20
d = c

print(a is c)       # False

print(c is d)       # True

print(d is not a)   # True

st = 'mister perfect'

print(st[3] is st[-1])      # True

li = [10, 20, [30, 40]]
gen_copy = li
shallow_copy = li.copy()
import copy
deep_copy = copy.deepcopy(li)


print(li is gen_copy)       # True

print(shallow_copy[2] is gen_copy[2])       # True

print(li[0] is not deep_copy[0])            # False

print(li is not deep_copy)          # True

print(gen_copy[2][0] is deep_copy[2][0])    # 30


