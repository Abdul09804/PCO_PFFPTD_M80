# scope of a variable

# a = 10
# def sam():
#     print(a)
#
# sam()
# print(a)

# def sam():
#     a = 10
#     print(a)
#
# sam()
# print(a)        # NameError

# a = 10      # global variable
# def outer():
#     a = 20          # local variable
#     print(a)
# print(a)
# outer()
# print(a)
"""
10
20
10
"""

"""
Scope of a Variable
LEGB Rule -> Local, Enclosed, Global, Built-In
local variables -> these are the variables which are created inside the function area
                -> These can be accessed inside the function but not outside
global variable -> these are the variables which gets created in the main frame or global frame
                -> these can be accessed in the global frame also in local frame 
"""
# sum = 8
# print(sum([1, 2, 3]))       # TypeError


# a = 10
# def outer():
#     print(a)
#     a = 20
#     print(a)
# print(a)
# outer()
"""
10
UnboundLocalError
"""

