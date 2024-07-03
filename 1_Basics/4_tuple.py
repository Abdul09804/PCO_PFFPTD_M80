# tuple
"""
-> It is a homogeneous or heterogeneous collection of data-items enclosed
   between ()
-> Syntax:
            Var = (Val1, Val2, .............., Valn)
                            or
            Var = Val1, Val2, ................, Valn
-> The default value of tuple is ()
-> Tuple is a immutable collection
"""

a = 1, 2, 3, 4, 5
print(a)        # (1, 2, 3, 4, 5)
print(type(a))  # <class 'tuple'>

t = ()
print(type(t))      # <class 'tuple'>
print(bool(t))      # False

l1 = [10]
t1 = (10)
print(type(l1))     # <class 'list'>
print(type(t1))     # <class 'int'>

l2 = ['hai']
t2 = ('hai')
print(type(l2))     # <class 'list'>
print(type(t2))     # <class 'str'>

"""
-> To store a single value inside a tuple directly is not possible so, we make 
   use of the syntax,
            Var = (Val,)
            Var = Val, 
"""

t3 = ('hai',)
t4 = 10,

print(type(t3))     # <class 'tuple'>
print(type(t4))     # <class 'tuple'>

t = (10, 9-5.4j, [1, 2], 'hai')
# t[0] = 11       # TypeError   -> tuple is immutable

t[2][0] = 11
print(t)        # (10, (9-5.4j), [11, 2], 'hai')


t = ('python', ['webtech', 'manual'], (12, 65))

# 'python'
# 65
# 'manual'
print(t[-1][-1])