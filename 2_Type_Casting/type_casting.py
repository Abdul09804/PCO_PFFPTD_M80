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

num = 92.23

print(int(num))         # 92
print(int(9.999999))    # 9

print(complex(num))     # (92.23+0j)

print(bool(num))        # True

print(str(num))         # '92.23'

# print(list(num))        # TypeError:

# print(tuple(num))       # TypeError:

# print(set(num))         # TypeError:

# print(dict(num))        # TypeError:

########################################################################################

# 3) Typecasting complex to other datatypes

num = 3-8.3j

# print(int(num))         # TypeError

# print(float(num))       # TypeError

# print(complex(num))     # (3-8.3j)

print(bool(num))        # True

print(str(num))         # '(3-8.3j)'

# print(list(num))        # TypeError

# print(tuple(num))       # TypeError

# print(set(num))         # TypeError

# print(dict(num))        # TypeError

##########################################################################################

# 4) Typecasting of boolean to other datatypes

a = True
b = False

print(int(a), int(b))       # 1 0

print(float(a), float(b))   # 1.0 0.0

print(complex(a), complex(b))   # (1+0j) 0j

print(str(a), str(b))       # 'True' 'False'

# print(list(a))      # TypeError

# print(tuple(a))     # TypeError

# print(set(a))       # TypeError

# print(dict(a))      # TypeError

