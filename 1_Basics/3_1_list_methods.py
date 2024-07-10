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

# li = [1, 8.6, False, [1, 2], '7', '9', 79]
# print(li.pop())     # 79
# print(li)       # [1, 8.6, False, [1, 2], '7', '9']
#
# print(li.pop(1))        # 8.6
# print(li)       # [1, False, [1, 2], '7', '9']
#
# # print(li.pop(10))   # IndexError

#################################################################################

# 5) remove
"""
-> It is used to remove the specified value from the list
-> Syntax:
        Var.remove(Val)
-> If there are value is present multiple times then, the first occurrence of 
   value will be removed
-> If the value is not present then, remove will throw ValueError 
"""

# l = [10, 6.75, 8+6j, 'hai', 10, 6.75, 'hello', 1, 4]
# print(l.remove(1))      # NOne
# print(l)    # [10, 6.75, (8+6j), 'hai', 10, 6.75, 'hello', 4]

# l.remove(10)
# print(l)        # [6.75, (8+6j), 'hai', 10, 6.75, 'hello', 1, 4]

# l.remove(25)    # ValueError: list.remove(x): x not in list

##############################################################################

# 6) clear
"""
-> It is used to remove all the values from the list
-> Syntax:
            Var.clear()
-> The return type of clear is None
"""

# l = [10, 6.75, 8+6j, 'hai', 10, 6.75, 'hello', 1, 4]
# print(l.clear())    # None
# print(l)    # []

###############################################################################

# 7) index -> same as that of index of string datatype

#############################################################################

# 8) count
"""
-> It is used to count the number of occurrence of given value in a list
-> Syntax:
        Var.count(Val)
-> The return type of count is integer 
-> If the value is not present count will return 0
"""
l = [10, 6.75, 8+6j, 'hai', 10, 6.75, 'hello', 1, 4, 10, 'hai', 10, 10]

print(l.count(10))  # 5

print(l.count('python'))    # 0

##############################################################################

# 9) reverse
"""
-> It is used to reverse the given list
-> Syntax:
            Var.reverse()
-> The return type of reverse is None
"""

# l = [10, 'python', 10.5, [1, 2, 3]]
# print(l.reverse())      # NOne
# print(l)        # [[1, 2, 3], 10.5, 'python', 10]

#############################################################################

# 10) sort
"""
-> It is used to sort the values of list
-> Syntax: 
            Var.sort()  # sort in ascending order
            Var.sort(reverse=True)  # sort in descending order
-> The return type of sort is None
"""

l = [1, 85, 29, 27, 12, 8, 38, 234, 94]
# print(l.sort())     # None
# print(l)        # [1, 8, 12, 27, 29, 38, 85, 94, 234]
#
# l.reverse()
# print(l)        # [234, 94, 85, 38, 29, 27, 12, 8, 1]

l.sort(reverse=True)
print(l)    # [234, 94, 85, 38, 29, 27, 12, 8, 1]


names = ['eve', 'steve', 'alex', 'bob', 'john', 'jenny']
# names.sort()
# print(names)        # ['alex', 'bob', 'eve', 'jenny', 'john', 'steve']

# names.sort(reverse=True)
# print(names)        # ['steve', 'john', 'jenny', 'eve', 'bob', 'alex']


