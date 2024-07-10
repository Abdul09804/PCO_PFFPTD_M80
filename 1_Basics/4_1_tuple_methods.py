# Tuple Methods

# 1) Index
"""
-> It is used to get the index number of a specified value in the tuple
-> Syntax:
            Var.index(Val)
-> The return type of index is integer
-> If the value is not present index wil throw ValueError
"""
# t = (10, 6.75, 8+6j, 'hai', 10, 6.75, 'hello', 1, 4, 10, 'hai', 10, 10)
#
# print(t.index(8+6j))    # 2

# print(t.index('python'))        # ValueError: tuple.index(x): x not in tuple

###############################################################################

# 2) count
"""
-> It is used to get teh number of occurrences of a given value in the tuple
-> Syntax:
            Var.count(Val)
-> The return type of count is integer
-> If the value is not present, count will return 0
"""

# t = (10, 6.75, 8+6j, 'hai', 10, 6.75, 'hello', 1, 4, 10, 'hai', 10, 10)
#
# print(t.count('hai'))       # 2
#
# print(t.count('data'))      # 0

################################################################################