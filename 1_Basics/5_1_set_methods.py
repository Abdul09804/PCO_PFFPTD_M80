# Set methods

# 1) add
"""
-> It is used to add the values to a set
-> Syntax:
            Var.add(Val)
-> add method takes exactly one argument
-> The return type of add is None
"""

# s = {1, 2}
# print(s.add(3))     # None
# print(s)            # {1, 2, 3}

# s.add('hai')
# print(s)            # {'hai', 1, 2, 3}

# # s.add('hello', 89)      # TypeError: set.add() takes exactly one argument (2 given)
#
# s.add(('hello', 89))
# print(s)        # {'hai', 1, 2, 3, ('hello', 89)}
#
# # s.add([1, 2])   # TypeError: unhashable type: 'list'

################################################################################

# 2) update
"""
-> It is used to update the set with the values of iterable
-> Syntax:
            Var.update(iterable)
-> The return type of update is None
"""

# s1 = {1, 2, 3}
# s2 = {4, 5, 6}

# print(s1.update(s2))    # None
# print(s1)       # {1, 2, 3, 4, 5, 6}
# print(s2)       # {4, 5, 6}

# s1.update('hello')
# print(s1)       # {1, 2, 3, 'l', 'h', 'e', 'o'}

# s1.update([10, 20, 30])
# print(s1)       # {1, 2, 3, 10, 20, 30}

# s1.update({10, 20, 30})

# s1.update([[1, 2], 3, 4])       # TypeError: unhashable type: 'list'

##################################################################################

# 3) pop
"""
-> It is used to remove random values from the set
-> Syntax:
            Var.pop()
-> pop returns the value which has been removed
"""

# s = {10, 'hai', 9.86, 9+7j}
# print(s.pop())
# print(s)

# s = set()
# print(s.pop())      # KeyError: 'pop from an empty set'

#################################################################################

# 4) remove
"""
-> It is used to remove the specified element from a set
-> Syntax:
            Var.remove(Val)
-> The return type of remove is None
-> If the value is not present remove will throw KeyError
"""

s = {10, 'hai', 9.86, 9+7j}
# print(s.remove('hai'))      # None
# print(s)        # {9.86, 10, (9+7j)}

# s.remove('python')      # KeyError: 'python'

#################################################################################

# 5) discard
"""
-> discard is used to remove the value from the set
-> Syntax:
            Var.discard(Val)
-> Discard will not throw any error if the value is not present
-> The return type of discard is None
"""

# s = {10, 'hai', 20, 97, 9.75, 88}
# print(s.discard(88))    # None
# print(s)    # {97, 20, 9.75, 10, 'hai'}
#
# print(s.discard('data science'))   # None

###############################################################################

# 6) clear
"""
-> It is used to remove all the values from the set
-> Syntax:
            Var.clear()
-> The return type of clear is None
"""

# print(s.clear())    # None
# print(s)    # set()

#################################################################################

# 7) union
"""
-> It returns a set which has the values of set and an iterable
-> Syntax:
            Var.union(iterable)
-> The return type of union is a set
"""

# s1 = {10, 20, 30}
#
# print(s1.union({40, 50, 60}))   # {50, 20, 40, 10, 60, 30}
# print(s1.union('abc'))      # {'c', 10, 'a', 20, 'b', 30}
# print(s1)       # {10, 20, 30}
#
# print(s1.union(['apple', 'google', 'yahoo']))   # {10, 'google', 'yahoo', 20, 'apple', 30}

################################################################################

# 8) intersection
"""
-> It is used to get a set of common values present in set and iterable
-> The return type of intersection is a set
-> Syntax:
            Var.intersection(iterable)
"""
#
# s1 = {10, 20, 30}
# s2 = {30, 20, 87}
# print(s1.intersection(s2))      # {20, 30}
# print(s1)           # {10, 20, 30}
#
# print(s1.intersection([10, 30]))       # {10, 30}
#
# s1 = {'a', 'b', 'c'}
# print(s1.intersection('hai'))   # {'a'}

# s1 = {10, 20}
# print(s1.intersection({30, 40}))    # set()

################################################################################

# 9) difference
"""
-> It is used to get the values of set1 excluding the common elements in set1 and
   iterable
-> Syntax:
            Var.difference(iterable)
-> The return type of difference is a set
"""
#
s1 = {10, 20, 30}
s2 = {30, 20, 87}

print(s1.difference(s2))    # {10}
print(s2.difference({10, 33}))  # {20, 30, 87}

print(s1.difference([10]))  # {20, 30}

#################################################################################

# 10) difference_update
"""
-> It is a method which is used to update a set with value obtained from the
   method difference
-> Syntax:
            Var.difference-update(iterable)
"""
# s1 = {10, 20, 30}
# s2 = {30, 20, 87}
# print(s1.difference_update(s2))     # None
# print(s1)       # {10}
# print(s2)       # {20, 30, 87}

##################################################################################

# 11) intersection_update
"""
-> It is used to update the set with the values obtained by intersection
   method
-> Syntax:
            Var.intersection_update(iterable)
-> The return type of intersection_update is None
"""
s1 = {10, 20, 30}
s2 = {30, 20, 87}
print(s1.intersection(s2))      # {20, 30}
print(s1)           # {10, 20, 30}

print(s1.intersection_update(s2))   # NOne
print(s1)       # {20, 30}
print(s2)       # {20, 30, 87}

#############################################################################

