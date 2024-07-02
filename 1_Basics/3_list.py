# List(list)
"""
-> It is a homogenous or heterogeneous collection of data-items enclosed between []
-> Syntax:
        Var = [Val1, Val2, ............., Valn]
-> The values are separated by comma operator
-> Homogenous list - list which has the values that belong to same datatype
"""

nums = [1, 2, 3, 4, 5]
vals = [10, 'hai', [2, 3], 8+7j]

print(nums[2])      # 3
print(vals[1])      # 'hai'

print(vals[1][2])   # i
print(vals[2][0])   # 2

print(id(vals[2][0]))   #
print(id(nums[1]))

nums[2] = 22
print(nums)     # [1, 2, 22, 4, 5]

"""
-> We can modify the values of the lsit using index numbers
-> List is a mutable collection
"""

# vals[1][0] = 'H'    # TypeError
vals[1] = 'Hai'
print(vals)     # [10, 'Hai', [2, 3], (8+7j)]

li = []
print(type(li))     # <class 'list'>
print(bool(li))     # False
