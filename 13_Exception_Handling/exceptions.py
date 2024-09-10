# exception handling

a = 10
b = '20'
# print(a + b)    # TypeError

l = [1, 2, 3]
# l.extend(5)     # TypeError
# l.extend('hai')

# l.add(45)       # AttributeError

# l.remove(8)     # ValueError
# l.remove(2)

s = {1, 2}
s.add(3)
# s.add([5, 7])       # TypeError

# if 5:
#             # IndentationError

# if 5        # SyntaxError

# a, b, c, d = 1, 2, 3, 4, 5      # ValueError

t = (1, 2)
# t.append(7)     # AttributeError

# t[0] = (1, 2)       # TypeError

# print(5/0)      # ZeroDivisionError

# with open('sample.txt') as file:        # FileNotFoundError
#     pass

# with open('sample1.txt', 'x') as file:      # FileExistsError
#     pass

"""
-> We can handle these exceptions using try and except block 
-> try block includes problem statement which throws an error
-> except block takes control when try block has some exceptions
-> 1) Specific Exception Handling
   2) Generic Exception Handling
   3) Default Exception Handling
"""

# 1) Specific Exception Handling

def add():
    a = eval(input('Enter the value of a : '))
    b = eval(input('Enter the value of b : '))
    print(a + b)

# add()

# try:
#     add()
# except TypeError:
#     print("Datatype not matching")

# try:
#     add()
# except TypeError as message:
#     print(message)


# def add():
#     try:
#         a = eval(input('Enter the value of a : '))
#         b = eval(input('Enter the value of b : '))
#         print(a + b)
#     except TypeError as message:
#         print(message)
#         add()
#
# add()

"""
The above program can handle only TypeError but not SyntaxError
"""

# a = int(input())
# b = int(input())


# def add():
#     try:
#         a = int(input('Enter the value of a : '))
#         b = int(input('Enter the value of b : '))
#         print(a + b)
#     except ValueError as msg:
#         print(msg)
#         add()
#
# add()






