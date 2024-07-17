# 2) Relational Operator

# 1) Relational equal to operator (==)

print(4 == 4+0j)    # True

print(3+6j == (3.0+6.0j))   # True

print('abc' == 'abc')       # True

print('acb' == 'abc')       # False

print([1, 2, 3] == [1.0, 2, 3+0j])      # True

print((1, 2, 3) == (3, 2, 1))       # False

print({'a': 1, 'b': 2} == {'a': 1, 'b': 3})     # False

print({'a': 1, 'b': 2} == {'b': 2, 'a': 1})     # True

print({1, 2, 3} == {3, 2, 1})       # True

#########################################################################################

# 2) Relational not equal to operator

print(18 != 20)     # True

print('abc' != 'abc')   # False

#######################################################################################

# 3) Relational lesser than operator (<)

# print((3+3j) < (4+4j))      # TypeError

print('a' < 'A')        # False     # 97 < 65

print('A' < 'a')        # True      # 65 < 97

print(ord('A'))     # 65

print(ord('s'))     # 115

print(chr(116))     # t

print('python' < 'pythoN')      # False

print('P' < 'pqrst')        # True

print('pQRST' < 'p')        # False

"""
For string,
st1 < st2
if ord(st1[0]) < ord(st2[0]) -> True
if ord(st1[0]) > ord(st2[0]) -> False
if ord(st1[0]) == ord(st2[0]) -> compare ord(st1[1]) and ord(st2[1]) ...........
... if st1[-1] == st2[-1] -> False
"""

print([10, 2, 3] < [1, 90, 97])     # False

print([10, 20, 30] < [10, 20, 40])      # True

print([10, 20, 30] < [10, 20, 30])      # False

"""
for list, 
l1 < l2
if l1[0] < l2[0]    -> True
if l1[1] > l2[1]    -> False
if l1[0] == l2[0]   -> compares l1[1] and l2[1].............
if l1[-1] == l2[-1]  -> False 
"""

print({1, 2, 3} < {3, 2})       # False

print({3, 2} < {1, 2, 3})       # True

print({10, 20, 30} < {100, 200, 300})   # False

print({8+7j, 4, 3} < {8+7j, 3, 5, 4})   # True
"""
s1 < s2
True -> s1 is a subset of s2 or s2 is superset of s1
False -> s1 is not a subset of s2
"""

##########################################################################################

# 4) Relational Greater than operator

########################################################################################












