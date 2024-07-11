# Set(set)
"""
-> Set is an unordered, non-duplicate collection of homogeneous or heterogeneous
   data-items enclosed between {}
-> Syntax:
            Var = {Val1, Val2,................, Valn}
            where, values are of immutable datatype
-> The default value of set is set()
-> Set is a mutable collection whereas, values present in set are immutable
-> We can not modify the values in set but can add or remove the values from set
"""

# s = {}
# print(bool(s))  # False
# print(type(s))  # <class 'dict'>

# s = set()
# print(bool(s))  # False
# print(type(s))  # <class 'set'>

s = {10, 9.75, 7+6j, False, 'hai', (1, 2, 3)}
print(s)        # {False, (7+6j), 9.75, 10, (1, 2, 3), 'hai'}

s = {10, 9.23, False, 0.0, 10+0j, 'hello'}
print(len(s))   # 4
print(s)        # {False, 9.23, 10, 'hello'}

s1 = {True, 1, 0, False}
print(s1)   # {0, True}

s1 = {False, True, 0, 1}
print(s1)   # {False, True}

# s2 = {8, [1,2], 9.87}       # TypeError: unhashable type: 'list'
# s3 = {8, {1,2}, 9.87}       # TypeError: unhashable type: 'set'

s1 = {10, 20, 30, 40}
s1.add(70)
print(s1)   # {70, 40, 10, 20, 30}
s1.remove(20)
print(s1)   # {70, 40, 10, 30}





