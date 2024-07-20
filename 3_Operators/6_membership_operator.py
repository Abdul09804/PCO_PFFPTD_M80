# membership operator
"""
-> It is an operator which is used to check whether a value is present in the collection
-> 1) in operator
   2) not in operator
"""

# 1) in operator
"""
-> It is an operator which gives the result as True if value is present in the collection
-> Syntax:
            Val in collection
"""

# print(5 in 656)     # TypeError

# print(5 in '656')       # TypeError

print(5 in [6, 5, 6])       # True

print('5' in '656')     # True

print('6' in 'apple')       # False

print(10 in [10, 20, 30])       # True

print(30 in [[10, 20], 30])     # True

print(10 in [[10, 20], 30])     # False

print(10 in [[10, 20], 30][0])      # 10 in [10, 20] -> True

print([[10, 20], 30][0])        # [10, 20]

print('a' in 'alex')            # True

print('a' in ['alex'])          # False

print('a' in ['alex', 'joseph'][0])     # True

print('c' in {'c': 30, 'f': 40})    # True

print(30 in {'c': 30, 'f': 40})     # False

######################################################################################

# 2) not in operator

print(7 not in [10, 20, 40])    # True

print(10 not in [10, 20, 30])   # False

########################################################################################


