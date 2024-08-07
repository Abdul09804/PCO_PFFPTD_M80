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


# print(greetings)        # <function greetings at 0x00000282BB8004A0>
# print(greetings())
"""
Hello Universe
None
"""
# greetings()     # Hello Universe

# WAP to reverse a given string

# def rev_str():
#     st = input('Enter the string : ')
#     rev = ''
#     for i in st:
#         rev = i + rev
#     print(rev)
#
#
# rev_str()

# WAP to count the number of integers in a given heterogeneous list

# def count_integers():
#     l = [1, 8.86, 'hai', 8+7j, 90, 12]
#     count = 0
#     for val in l:
#         if type(val) == int:
#             count += 1
#     print(count)
#
#
# count_integers()

#########################################################################################

# 2) Function with arguments and without return values

"""
Syntax:
        def fname(Var1, Var2, ....., Varn):
            SB
        fname(Val1, Val2,......, Valn)
"""

# def display(name, empid, salary):
#     print(f"Hello I'm {name}, my Employee ID is {empid} and I earn Rs.{salary} per month")
#
# # display()       # TypeError
#
# display("John", "ABC123", 20000)


# WAP to count the number of occurrence of a given character in a string

def count_char(st, ch):
    count = 0
    for i in st:
        if i == ch:
            count += 1
    print(count)

#
# count_char("apple", 'p')        # 2
# st = 'mississippi'
# ch = 's'
# count_char(st, ch)      # 4
#
# a = 'mississippi'
# b = 'p'
# count_char(a, b)        # 2


# WAP to extract all uppercase character in a given string

def upper_case(st):
    uc = ''
    for i in st:
        if 'A' <= i <= 'Z':
            uc += i
    print(uc)


# upper_case('FoReiGn')


##########################################################################################

# 3) Function without argunments and with return values
"""
Syntax:
        def fname():
            SB
            return Val1, Val2, ....., Valn
        print(fname())
        res = fname()
        print(res)
        var1, var2, ., varn = fname()
"""


# def sam():
#     return
#
#
# print(sam())        # None
# sam()

# def sam():
#     return 1, 2, 3
#
#
# sam()
# print(sam())        #  (1, 2, 3)
# res = sam()
# print(res)          # (1, 2, 3)
# a, b, c  = sam()
# print(a, b, c)      # 1 2 3


# WAP to get the following output
nums = [8, 32, 86, 99, 12]
# o/p = [8, 5, 14, 18, 3]

# def sum_of_digits():
#     nums = [8, 32, 86, 99, 12]
#     res = []
#     for num in nums:
#         s = 0
#         for i in str(num):
#             s += int(i)
#         res.append(s)
#     return res
#
#
# sum_of_digits()
# print(sum_of_digits())      # [8, 5, 14, 18, 3]

#########################################################################################

# 4) Function with arguments and with return value
"""
Syntax:
        def fname(args):
            SB
            retun val1, val2, ...., valn
            
        print(fname(args))
        res = fname(args)
        print(res)
        Var1, Var2, ...., Varn = fname(args)
"""

# def sam(a, b):
#     return a+b, a-b, a*b, a/b
#
#
# print(sam(4, 2))        # (6, 2, 8, 2.0)
# add, sub, mul, div = sam(4, 2)
# print(add, sub, mul, div)       # 6 2 8 2.0


############################################################################################

# WAP to reverse the given string

# st = 'hello world'
# rev = ''
# for ch in st:
#     rev = ch + rev
# print(rev)

# Type1

# def rev1():
#     # st = 'hello world'
#     # rev = ''
#     # for ch in st:
#     #     rev = ch + rev
#     # print(rev)
#
#
# rev1()


# Type2

# def rev2(st):
#     rev = ''
#     for ch in st:
#         rev = ch + rev
#     print(rev)
#
#
# rev2('hello')
# rev2(input('Enter the string : '))


# Type3

# def rev3():
#     st = 'hello world'
#     rev = ''
#     for ch in st:
#         rev = ch + rev
#     return rev
#
# print(rev3())
# res = rev3()
# print(rev)

# Type4

# def rev4(st):
#     rev = ''
#     for ch in st:
#         rev = ch + rev
#     return rev
#
#
# print(rev4('python'))
# res = rev4('python')
# print(res)

#######################################################################################

# WAP to check if a given number is a prime number

num = 7
for i in range(2, num//2+1):
    if num % i == 0:
        print(False)
        break
else:
    print(True)


# Type 1

def is_prime1():
    num = 7
    for i in range(2, num//2 + 1):
        if num % i == 0:
            print(False)
            break
    else:
        print(True)


is_prime1()

# Type2

def is_prime2(num):
    for i in range(2, num//2 + 1):
        if num % i == 0:
            print(False)
            break
    else:
        print(True)


is_prime2(21)

# Type3

def is_prime3():
    num = 16
    for i in range(2, num//2+1):
        if num % i == 0:
            return False
    else:
        return True


print(is_prime3())
res = is_prime3()
print(res)

# Type4
def is_prime4(num):
    for i in range(2, num//2+1):
        if num % i == 0:
            return False
    else:
        return True


print(is_prime4(61))

num = int(input('Enter the number : '))
if is_prime4(num) == True:
    print('The given number is a prime number')
else:
    print('Not a prime number')


# WAP to check if a given number is a palindrome using all 4 types of functions
# num = 865
# temp = num
# rev = 0
# while temp != 0:        # temp > 0
#     rev = rev*10 + temp % 10
#     temp = temp // 10
# if num == rev:
#     print('Palindrome')
# else:
#     print('Not a palindrome')

def is_palindrome(num):
    temp = num
    rev = 0
    while temp != 0:  # temp > 0
        rev = rev * 10 + temp % 10
        temp = temp // 10
    if num == rev:
        return True
    return False

print(is_palindrome(8))






