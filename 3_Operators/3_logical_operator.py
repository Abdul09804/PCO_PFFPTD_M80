# Logical Operator

# 1) Logical and operator

"""
-> It is an operator which gives the result as True only if all the operands are internally
   equal to True, if any one of the operand is internally equal to False, it gives the result
   as False
-> Truth Table
    op1     op2     o/p
    False   False   False
    False   True    False
    True    False   False
    True    True    True

-> The result of 'and' operator is the operand itself.
-> It gives the first default operand as output, if all the operands are non-default values,
   it gives the result as last operand
"""

print(True and False)       # False

print(True and True)        # True

print(4 and True)           # True

print(4 and False)          # False

print(4 and 6)              # 6

print(True and 10)          # 10

print('False' and 'True')   # 'True'

print(0 and 0.0)            # 0

print(False and [1, 2, 3] and {10, 20, 30})     # False

print('hai' and [])         # []

print('hello' and 'hello world')        # 'hello world'

"""
op1 and op2 and op3 and op4...................and opn 

True and True and True and False and False and True -> 
"""


print(True and True and True and False and False and True)      # False

print('hello' and 'hai' and 'python' and 'programming')     # programming

# check if a character is an uppercase character

ch = 'E'    # 'r', 'F'
print(ord(ch) >= 65 and ord(ch) <= 90)      # 69 >= 65 and 69 <= 90 -> True and True -> True

print(65 <= ord(ch) <= 90)      # 65 <= 69 <= 90    -> True

print('A' <= ch <= 'Z')         # 65 <= 69 <= 90    -> True

# check if a character is lowercase character

ch = 'x'

print('a'<=ch<='z')         # 97 <= 120 <= 122 -> True

# check if a character is a digit

ch = '6'
print('0' <= ch <= '9')     # True

########################################################################################

# 2) LOgical or operator
"""
-> 'or' is an operator which gives the result as True if any one of the operand is True,
    it gives the result as False only if all the operands are False
-> Truth Table
    op1     op2     o/p
    False   False   False
    False   True    True
    True    False   True
    True    True    True
-> The output will be the first non default operand, if all the operands are default values
   then the output will be the last operand
"""

print(6 or 7)       # 6

print('python' or 'java')       # python

print(0.0 or False)     # False

print(4>3 or 9>7)       # True or True -> True

print('a' > 'A' or 'a' > 'c')   # True

print(0 or False or [()] or ({}) or 87)     # [()]

# check if a character is an alphabet
ch = '8'
print('A'<=ch<='Z' or 'a'<=ch<='z')

#  check if char is an alphanumeric character
print('A'<=ch<='Z' or 'a'<=ch<='z' or '0'<=ch<='9')

print('0'<='8'<='9')    # True

####################################################################################

# 3) Logical not operator

"""
-> It is an operator which gives the result as True if the i/p is False and vice versa
-> The resultant of not is boolean
"""

print(not 8)    # False

print(not ())       # True

print(not 4==3)     # True

print(not [9, 8])       # False

ch = 'r'
print(not 'A'<=ch<='Z')


######################################################################################

