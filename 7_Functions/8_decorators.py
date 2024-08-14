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