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
-> We get an error because the variable is accessed before even creating it
"""

"""
-> To access and modify the global variable inside teh function we make use of a keyword 
   called 'global'
-> global has to be the first argument inside the function area
-> global has to be followed by the variables which has to modified
-> address of global variable will be stored in function area
"""
#
# a = 10
# def outer():
#     global a
#     print(a)
#     a = 20
#     print(a)
# print(a)
# outer()
# print(a)
"""
10
10
20
20
"""


# p = 10
# q = 20
#
# def outer():
#     global p
#     p = 11          # modifies global variable
#     q = 12          # local variable
#     print(p, q)
#
# print(p, q)
# outer()
# print(p, q)
"""
10 20
11 12
11 20
"""


# p = 10
# q = 20
# def outer():
#     global p, q
#     p = 11          # modifies global variable
#     q = 12          # local variable
#     print(p, q)
#
# print(p, q)
# outer()
# print(p, q)
"""
10 20
11 12
11 12
"""

m = 1                   # global var
def outer():
    # m = 2               # local var for outer
    def inner():
        # m = 3           # local var for inner
        print(m)
    print(m)
    inner()
    print(m)

outer()
print(m)
"""
2
3
2
1
"""


