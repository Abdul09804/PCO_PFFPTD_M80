# Parameters
"""
def sam(ref1, ref2):    # formal arguments/ parameters
    pass
sam(val1, val2)         # actual arguments/ arguments
"""

# def sam(a, b):
#     print(a, b)


# sam(1, 2)       # 1 2
# sam(1)                  # TypeError:

# def greeting(message):
#     print(message)


# greeting('hai')
# greeting()  # TypeError
# greeting(input('Enter the message : '))
# greeting(message)   # NameError

# message = 'hello world'
# print(message)

"""
Types of arguments
1) Positional Arguments
2) Keyword Arguments
"""

# 1) Positional Arguments

def display(name, empid, sal):
    print(f"My name is {name}, my employee ID is{empid}, I earn {sal} rupees a month")

display("John", "ABC123", 10000)    # My name is John, my employee ID isABC123, I earn 10000 rupees a month

display("ABC123", "John", 10000)    # My name is ABC123, my employee ID isJohn, I earn 10000 rupees a month

# display("John", "ABC234")       # TypeError


# 2) Actual Arguments

def sam(a, b, c):
    print(f"The values of a, b, and c are {a}, {b} and {c}")


sam(a=1, b=2, c=3)      # The values of a, b, and c are 1, 2 and 3
sam(c=3, a=1, b=2)      # The values of a, b, and c are 1, 2 and 3

display(empid="ABC123", sal=10000, name="John")     # My name is John, my employee ID isABC123, I earn 10000 rupees a month

###########################################################################################

# default parameters

def greeting(message='hai'):
    print(message)


greeting('Hello world')
greeting()      # hai


def sam(a, b=2, c=3):
    print(f"The values of a, b and c are {a}, {b} and {c}")

sam(10, 20, 30) # The values of a, b and c are 10, 20 and 30
sam(b=20, c=30, a=10)   # The values of a, b and c are 10, 20 and 30
sam(10)     # The values of a, b and c are 10, 2 and 3
sam(10, c=20)   # The values of a, b and c are 10, 2 and 20
sam(10, 20, c=30)   # The values of a, b and c are 10, 20 and 30
# sam(a=10, 20, c=30)     # SyntaxError: positional argument follows keyword argument
sam(10, c=30, b=20)     # The values of a, b and c are 10, 20 and 30
# sam()   # TypeError -> min one argument is required

# WAP to find the sum of minimum 2 numbers and maximum 4 numbers
def add_num(n1, n2, n3=0, n4=0):
    print(n1+n2+n3+n4)

add_num(1, 2)
add_num(2, 3, 4)
add_num(1, 2, 3, 4)
add_num(1, 2, n4=4)


# WAP to find the product of minimum 3 numbers and maximum 5 numbers

def prod(n1, n2, n3, n4=1, n5=1):
    print(n1*n2*n3*n4*n5)

prod(1, 2, 3)
prod(1, 2, 3, 4)
prod(1, 2,3, 4, 5)
prod(1, 2, 3, n5=5)

"""
WAP to count the number of occurrence of a given substring in a given string between 
the specified limits only if specified 
"""

# st = 'mississippi'

def count_substring(st, sub, SI=0, EI=0):
    if EI == 0:
        EI = len(st)
    count = 0
    for i in range(SI, EI):
        if st[i] == sub:
            count += 1
    print(count)

st = 'mississippi'
count_substring(st, 's', 3, 8)  # 3
count_substring(st, 's')        # 4 -> SI = 0 and EI = 11
count_substring(st, 's', 5)     # 2 -> EI = 11
count_substring(st, 's', EI=5)  # 2

# create a function same as index method


