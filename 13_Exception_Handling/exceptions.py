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

# multiple exception blocks

# def div():
#     try:
#         a = eval(input())
#         b = eval(input())
#         print(a / b)
#     except TypeError as message:
#         print(message)
#         print('TypeError handled')
#     except ZeroDivisionError as message:
#         print(message)
#         print('Zero Division Error Handled')
#         div()
#     except SyntaxError:
#         print('Syntax Error Handled')
#
# div()

# try:
#     with open('exception.txt', 'x') as file:
#         file.write("Good morning all")
# except FileExistsError:
#     with open('exception.txt', 'a') as file:
#         file.write("Good morning all")


#################################################################################

# 2) Generic Exception Handling
"""
-> It can handle all types of errors except Keyboard Interruption
-> Syntax:
            try:
                problem statement
            except Exception/ BaseException as message:
                solution
"""

# def div():
#     try:
#         a = eval(input())
#         b = eval(input())
#         print(a / b)
#     except Exception as msg:
#         print(msg)
#         print('Error Handled')
#
# div()

# l = [10, 20, 30, 40]
# l.remove(11)

# try:
#     l = [10, 20, 30, 40]
#     l.remove(11)
# except BaseException as msg:
#     print(msg)
#     print('Error Handled')

# try:
#     while True:
#         print('Hello All')
# except Exception:
#     print('Error Handled')

################################################################################

# 3) Default Exception
"""
-> Default Exception handles all kinds of exceptions including keyboard interruption
-> Syntax:
        try:
            Problem Statement
        except:
            Solution
"""

# try:
#     while True:
#         print('Hello All')
# except:
#     print('Exception Handled')

# try:
#     print(10 / 0)
# except:
#     print('Error Handled')

# multiple exception blocks

# try:
#     # print(10 + 'a')
#     # print(name)
#     # print(20 / 0)
#     while True:
#         print('Hello')
# except TypeError as msg:
#     print(msg)
#     print('type error handled')
# except NameError as msg:
#     print(msg)
# except Exception as msg:
#     print(msg)
#     print('Generic Exception Handled')
# except:
#     print('Default Exception Handled')

#################################################################################

# raise Exceptions as per requirement

# try:
#     actual_password = '1234'
#     entered_password = input('Enter the password : ')
#     if actual_password == entered_password:
#         print('Phone Unlocked')
#     elif entered_password.isdigit() == False:
#         raise TypeError ("Password must contain only digits")
#     elif len(entered_password) != len(actual_password):
#         raise ValueError ("Password must contain exactly 4 digits")
#     else:
#         raise ValueError ("Incorrect Password")
# except ValueError as message:
#     print(message)
# except TypeError as message:
#     print(message)

###############################################################################

# Custom Exception

# class PhoneLocked(Exception):
#     pass
#
# for i in range(3):
#     try:
#         actual_password = '1234'
#         entered_password = input('Enter the password : ')
#         if actual_password == entered_password:
#             print('Phone Unlocked')
#             break
#         elif entered_password.isdigit() == False:
#             raise TypeError("Password must contain only digits")
#         elif len(entered_password) != len(actual_password):
#             raise ValueError("Password must contain exactly 4 digits")
#         else:
#             raise ValueError("Incorrect Password")
#     except ValueError as message:
#         print(message)
#     except TypeError as message:
#         print(message)
# else:
#     raise PhoneLocked ("No of attempts exceeded")

#################################################################################

try:
    a = eval(input())
    b = eval(input())
    print(a + b)
except TypeError:
    print('TypeError Handled')
except Exception:
    print('Generic Exception Handled')
except:
    print('Default Exception Handled')
else:
    print("In else block")
finally:
    print('In finally block')

"""
else - when there are no exceptions, else block will get executed
finally - gets executed if even if there is an error or no error
Order -> 
        try -> specific -> generic -> default -> else -> finally
"""

