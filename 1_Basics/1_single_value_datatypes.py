# Datatypes
"""
-> It specifies the size and type of the value
1) Single Value Datatype/ Individual Datatype
-> It is a kind of Datatype where in a single value is stored in a variable
-> a) Numeric Datatype
        i) Integer(int)
        ii) Float(float)
        iii) Complex(complex)
   b) Boolean

2) Multi-value Datatype/ Collection
-> It is a kind of datatype where in multiple values are stored in a variable
-> a) Sequential Datatype
        i) String(str)
        ii) List(list)
        iii) Tuple(tuple)
   b) Non-Sequential Datatype
        i) Set(set)
        ii) Dictionary(dict)
"""

# Integer(int)
"""
-> It is a real number without decimal values
-> The default value of integer is 0 which is internally equal to False
-> We make use of default values to initialise a variable with specified datatype
"""

a = 1
print(a)        # 1
print(type(a))  # <class 'int'>
print(bool(a))  # True

b = -78
print(b)        # -78
print(type(b))  # <class 'int'>
print(bool(b))  # True

c = 0
print(c)        # 0
print(type(c))  # <class 'int'>
print(bool(c))  # False

##############################################################################

# Float(float)
"""
-> It is a real number with decimal values
-> The default value of float is 0.0 which is internally equal to False
"""

p = 8.97
print(p)        # 8.97
print(type(p))  # <class 'float'>
print(bool(p))  # True

q = 0.0
print(q)        # 0.0
print(type(q))  # <class 'float'>
print(bool(q))  # False

##############################################################################

# complex (complex)
"""
-> A number in the form of a+-bj is a complex number
-> 'a' is the real part and 'bj' is the imaginary part
-> the value of 'j' is square root of -1
-> the value of 'a' and 'b' can be either integer or float
-> The default value of complex number is 0j
"""

x = 7.8-4j
print(x)        # (7.8-4j)
print(type(x))  # <class 'complex'>
print(bool(x))  # True

y = 0j
print(y)        # 0j
print(type(y))  # <class 'complex'>
print(bool(y))  # False

##############################################################################

# 4) Boolean(bool)
"""
-> It has only 2 values, True and False
-> False is the default value whereas True is the non-default value
-> We make use of boolean in 2 cases, 
    1) To assign as a value to any variable
    2) As a resultant to check the condition
"""

a = True
b = False

print(a)
print(type(a))  # <class 'bool'>

print(b)    # False
print(type(b))  # <class 'bool'>

print(4 > 3)    # True

print(6 == 9)   # False

"""
bool    int     float       complex
False    0       0.0          0j
True     1       1.0         1+0j
"""
print(int(True))
print(complex(True))

