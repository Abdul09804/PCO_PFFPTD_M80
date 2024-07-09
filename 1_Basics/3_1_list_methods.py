# list methods

# 1) append
"""
-> It is used to add the value to the last index position of the list
-> Syntax:
            Var.append(Val)
-> The return type of append is None
-> The original list is modified
"""

# li = [10, 'hai', (4, 5), 7-8.3j]
# print(id(li))   # 1865184988672
# print(li.append(43))    # None
# print(li)       # [10, 'hai', (4, 5), (7-8.3j), 43]
# print(id(li))   # 1865184988672
#
# li.append('hello')
# print(li)       # [10, 'hai', (4, 5), (7-8.3j), 43, 'hello']

################################################################################

# 2) insert
"""
-> It is used to add a value to the specified index position
-> Syntax:
            Var.insert(index, value)
-> The return type of insert is None
"""

# li = [1, 8.6, False, [1, 2]]
# print(li.insert(1, 100))    # None
# print(li)   # [1, 100, 8.6, False, [1, 2]]

# li.insert(-1, 34)       # li.insert(3, 34)
# print(li)   # [1, 8.6, False, 34, [1, 2]]

# li.insert(4, 75)
# print(li)       # [1, 8.6, False, [1, 2], 75]

#################################################################################

# 3) extend
"""
-> It is used to extend the list by the values of the iterable
-> Syntax:
            Var.extend(iterable)
-> The return type of extend is None
"""

# li = [1, 8.6, False, [1, 2]]
# print(li.extend(7))     # TypeError

# print(li.extend('abc'))     # None
# print(li)       # [1, 8.6, False, [1, 2], 'a', 'b', 'c']

# print(li.extend([10, 20, 30]))      #
# print(li)   # [1, 8.6, False, [1, 2], 10, 20, 30]

# li.append([10, 20, 30])
# print(li)   # [1, 8.6, False, [1, 2], [10, 20, 30]]

# li.extend(79)   # TypeError

# print(li.extend('79'))  #
# print(li)   # [1, 8.6, False, [1, 2], '7', '9']

# print(li.extend([79]))
# print(li)       # [1, 8.6, False, [1, 2], '7', '9', 79]

#################################################################################

# 4) pop
"""
-> It is used to remove the last value from the list
-> Syntax:
            Var.pop()       # removes last value
            Var.pop(index_no)   # removes value present at specified index
-> If the index is not present, control will throw IndexError
-> pop returns the value which has been removed       
"""

li = [1, 8.6, False, [1, 2], '7', '9', 79]
print(li.pop())     # 79
print(li)       # [1, 8.6, False, [1, 2], '7', '9']

print(li.pop(1))        # 8.6
print(li)       # [1, False, [1, 2], '7', '9']

# print(li.pop(10))   # IndexError


