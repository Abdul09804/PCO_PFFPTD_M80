# function over loading
# def add(a, b):
#     print(a + b)
#
#
# def add(a, b, c):
#     print(a + b + c)
#
# # add(1, 2)   # TypeError
# add(1, 2, 3)

"""
-> If we try to do over loading in python, over riding happens
-> we can still achieve overloading by giving default values
"""

def add(a=0, b=0, c=0):
    print(a + b + c)


add()
add(1)
add(1, 2)
add(1, 2, 3)
add(b=2, c=3)
add(1, c=3)

#################################################################################

"""
operator overloading
+ -> addition, concatenation
* -> multiplication, packing, unpacking, power
"""

# + -> __add__

a = 3
b = 4
print(a + b)
print(a.__add__(b))     # 7

print('hai'.__add__('hello'))

print(b.__sub__(a))

#####################################################################################

"""
ob1 + ob2               ob1.__add__(ob2)
ob1 - ob2               ob1.__sub__(ob2)
ob1 * ob2               ob1.__mul__(ob2)
ob1 / ob2               ob1.__truediv__(ob2)
ob1 // ob2              ob1.__floordiv__(ob2)
ob1 % ob2               ob1.__mod__(ob2)
ob1 ** ob2              ob1.__pow__(ob2)
ob1 < ob2               ob1.__lt__(ob2)
ob1 > ob2               ob1.__gt__(ob2)
ob1 <= ob2              ob1.__le__(ob2)
ob1 >= ob2              ob1.__ge__(ob2)
ob1 == ob2              ob1.__eq__(ob2)
ob1 != ob2              ob1.__ne__(ob2)
"""

class A:
    def __init__(self, a):
        self.a = a


a1 = A(2)
a2 = A(3)
# print(a1 + a2)      # TypeError

print(dir(A))

"""
-> __add__ is not present in the directory and hence ob1 + ob2 gives TypeError
-> We can make any operator work for user defined objects by implementing magic methods
"""



