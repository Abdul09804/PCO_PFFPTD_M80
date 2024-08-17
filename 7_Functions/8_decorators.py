# decorators

# def sam(some_val):
#     return some_val
#
#
# print(sam(18))      # 18
# print(sam("hello"))     # hello
#
# a = 'hello world'
# b = sam(a)
# print(b)
#
# def add(a, b):
#     return a + b
#
# print(add)      # <function add at 0x00000250A190AF20>
# print(add(3, 4))    # 7
#
# a = sam(add)
# print(a)        # <function add at 0x0000016262D2AF20>
#
# b = add
# print(b)        # <function add at 0x000001EADF82AF20>
#
# print(add(33, 44))      # 77
# print(a(33, 44))        # 77
# print(b(3, 4))      # 7

##################################################################################

# def sam(a):
#     def inner():
#         print(a)
#     return inner
#
#
# li = [10, 20, 30]
# print(li)       # [10, 20, 30]
#
# a = 10
# # print(inner())      # NameError
#
# print(sam(12))       # <function sam.<locals>.inner at 0x000001D672DCAF20>
#
# sam1 = sam(100)     #
# sam2 = sam(200)     #
# print(sam1)     # <function sam.<locals>.inner at 0x000002063128AF20>
# print(sam2)     # <function sam.<locals>.inner at 0x0000026DA180F560>
#
# sam1()      # 100
# sam2()      # 200


def sam(func):
    def inner():
        print(func)
        return func()

    return inner

def greeting():
    return "Hello World"

print(greeting())       # Hello World

a = sam(greeting)
print(a)    # <function sam.<locals>.inner at 0x000001CFF837F560>


def demo():
    return "In demo"

b = sam(demo)
print(b)        # <function sam.<locals>.inner at 0x0000014C36C5F6A0>


print(a())
"""
<function greeting at 0x0000017C6AA8AF20>
Hello World
"""

print(b())
"""
<function demo at 0x000001DEF976F600>
In demo
"""

#####################################################################################

def sam(func):
    def inner():
        print(func)
        return func()

    return inner


def greeting():
    return "Hello World"


def demo():
    return "In demo"

a = sam(greeting)
print(a())
"""
<function greeting at 0x000001AFC6B304A0>
Hello World
"""

greeting = sam(greeting)
print(greeting())
"""
<function greeting at 0x0000024F5B5504A0>
Hello World
"""

print(demo())
"""
In demo
"""

demo = sam(demo)
print(demo())
"""
<function demo at 0x000001CCF871F7E0>
In demo
"""

##################################################################################
# Decorator
"""
-> adding an extra functionality to the main function without modifying it, is 
   known as a decorator
-> decorator function must have a nested function 
-> Outer function/ deorator function must take only one argument ie, address of
   the main function
-> nested function/ inner function/ wrapper must take the arguments that must be
   taken by main function
-> main function must be called inside wrapper function
-> decorator function must return address of wrapper
-> Syntax:
            def deco(func):
                def wrapper(*ars, **kwargs):
                    PRE-TASK
                    result = func(*args, **kwargs)
                    POST-TASK
                    return result
                return wrapper
            return wrapper
"""

def calculate(func):
    def wrapper(x, y, z):
        print('Calculating.....')
        print(func)
        result = func(x, y, z)
        return result
    return wrapper


def add(a, b, c):
    return a + b + c

add = calculate(add)
print(add)      # <function calculate.<locals>.wrapper at 0x000001045CB0FA60>

print(add(1, 2, 3))     #

def sub(a, b, c):
    return a - b - c

sub = calculate(sub)
print(sub(10, 5, 3))


###############################################################################

def calculate(func):
    def wrapper(*args, **kwargs):
        print('Calculating.....')
        print(func)
        result = func(*args, **kwargs)
        return result
    return wrapper


def add(a, b, c):
    return a + b + c


def sub(a, b):
    return a - b

add = calculate(add)
sub = calculate(sub)

print(add(1, 2, 3))
print(sub(1, 2))





