# Functions
"""
-> Functions are the named memory block which has some set of instructions used to
   perform a specific task
   1) Inbuilt Functions - print, input, min, max, etc
   2) User Defined Functions

User Defined Functions
-> These are the functions which are created based on user requirements
-> Syntax:
            def fname(args):                # function declaration
                function statement/ SB      # function definition
                return values
            fname(args)                     # function call
            # where passing the arguments and returning the value are not mandatory
-> def - it is a keyword which is used to create a function
-> fname - name given to identify some set of instructions
-> args - parameters/ values which are used to perform the task
-> return - a keyword which makes he control come out of the function by taking some values
-> function call - only if we call the function it will be executed

User Defined functions are classified into 4 types
1) Function without arguments and without return values - reverse
2) Function with arguments and without return values - append, insert, extend
3) Function without arguments and with return values - upper, lower, swapcase,
4) Function with arguments and with return values - count, type, id
"""

# 1) Function without arguments and without return values
"""
-> Syntax:
        def fname():
            SB
        fname()
"""


def greetings():
    print('Hello Universe')


print(greetings)        # <function greetings at 0x00000282BB8004A0>
print(greetings())
"""
Hello Universe
None
"""
greetings()     # Hello Universe

# WAP to reverse a given string

def rev_str():
    st = input('Enter the string : ')
    rev = ''
    for i in st:
        rev = i + rev
    print(rev)


rev_str()

# WAP to count the number of integers in a given heterogeneous list

def count_integers():
    l = [1, 8.86, 'hai', 8+7j, 90, 12]
    count = 0
    for val in l:
        if type(val) == int:
            count += 1
    print(count)


count_integers()





