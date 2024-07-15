# Type Casting
"""
-> Converting one datatype to another datatype
-> Syntax:
            dest_var = dest_datatype(source_var)
"""


# 1) Typecasting integer to other datatypes

# num = 24
#
# print(float(num))       # 24.0
#
# print(complex(num))     # (24+0j)
#
# print(bool(num))        # True
#
# print(str(num))         # '24'
#
# # print(list(num))        # TypeError:
#
# # print(tuple(num))       # TypeError:
#
# # print(set(num))         # TypeError:
#
# # print(dict(num))        # TypeError:

#################################################################################

# 2) Typecasting float to other datatypes

# num = 92.23
#
# print(int(num))         # 92
# print(int(9.999999))    # 9
#
# print(complex(num))     # (92.23+0j)
#
# print(bool(num))        # True
#
# print(str(num))         # '92.23'
#
# # print(list(num))        # TypeError:

# print(tuple(num))       # TypeError:

# print(set(num))         # TypeError:

# print(dict(num))        # TypeError:

########################################################################################

# 3) Typecasting complex to other datatypes

# num = 3-8.3j
#
# # print(int(num))         # TypeError
#
# # print(float(num))       # TypeError
#
# # print(complex(num))     # (3-8.3j)
#
# print(bool(num))        # True
#
# print(str(num))         # '(3-8.3j)'

# print(list(num))        # TypeError

# print(tuple(num))       # TypeError

# print(set(num))         # TypeError

# print(dict(num))        # TypeError

##########################################################################################

# 4) Typecasting of boolean to other datatypes

# a = True
# b = False
#
# print(int(a), int(b))       # 1 0
#
# print(float(a), float(b))   # 1.0 0.0
#
# print(complex(a), complex(b))   # (1+0j) 0j
#
# print(str(a), str(b))       # 'True' 'False'
#
# # print(list(a))      # TypeError
#
# # print(tuple(a))     # TypeError
#
# # print(set(a))       # TypeError
#
# # print(dict(a))      # TypeError

########################################################################################

# 5) Typecasting of string to other datatypes

a = 'hello'
b = '12'

# print(int(a))       # ValueError
print(int(b))       # 12
# print(int('12.86'))     # ValueError


print(float(b))     # 12.0
print(float('12.85'))   # 12.85

print(complex('8+7j'))    # (8+7j)
print(complex('3.86'))      # (3.86+0j)
print(complex('8756'))      # (8756+0j)

print(bool(a))          # True
print(bool('12'))       # True
print(bool('True'))     # True
print(bool('False'))    # True
print(bool(''))         # False

print(list(a))          # ['h', 'e', 'l', 'l', 'o']

print(tuple(a))         # ('h', 'e', 'l', 'l', 'o')

print(set(a))           # {'e', 'l', 'o', 'h'}

# print(dict(a))          # ValueError

#######################################################################################

# 6) Typecasting of list to other datatypes

l = [1, 2, 3, 4]

# print(int(l))       # TypeError

# print(float(l))     # TypeError

# print(complex(l))       # TypeError

print(bool(l))          # True
print(bool([]))         # False

print(str(l))           # '[1, 2, 3, 4]'
print(len(str(l)))      # 12

print(tuple(l))         # (1, 2, 3, 4)

print(set(l))           # {1, 2, 3, 4}

# print(dict(l))          # TypeError

l = [('a', 1), ('b', 2), ('c', 3)]
print(dict(l))      # {'a': 1, 'b': 2, 'c': 3}

l = [['a', 1], ['b', 2], ['c', 3]]
print(dict(l))      # {'a': 1, 'b': 2, 'c': 3}

##########################################################################################

# 7) Typecasting of tuple to other datatypes
"""
-> Type casting of tuple is same as typecasting of list to other datatypes
"""

##########################################################################################

# 8) Typecasting of set to other datatypes
"""
-> Type casting of set is same as typecasting of list to other datatypes
"""

#########################################################################################

# 9) Typecasting of dictionary to other datatypes
"""

"""
d = {'a': 1, 'b': 2, 'c': 3}

# print(int(d))       # TypeError

# print(float(d))     # TypeError

# print(complex(d))     # TypeError

print(bool(d))      # True
print(bool({}))     # False

print(str(d))       # '{'a': 1, 'b': 2, 'c': 3}'
print(len(str(d)))  # 24

print(list(d))              # ['a', 'b', 'c']
print(list(d.keys()))       # ['a', 'b', 'c']
print(list(d.values()))     # [1, 2, 3]
print(list(d.items()))      # [('a', 1), ('b', 2), ('c', 3)]

print(tuple(d))             # ('a', 'b', 'c')
print(tuple(d.keys()))      # ('a', 'b', 'c')
print(tuple(d.values()))    # (1, 2, 3)
print(tuple(d.items()))     # (('a', 1), ('b', 2), ('c', 3))

print(set(d))               # {'a', 'b', 'c'}
print(set(d.keys()))        # {'b', 'a', 'c'}
print(set(d.values()))      # {1, 2, 3}
print(set(d.items()))       # {('a', 1), ('c', 3), ('b', 2)}

