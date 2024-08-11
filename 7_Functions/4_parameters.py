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

