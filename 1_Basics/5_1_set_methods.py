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

