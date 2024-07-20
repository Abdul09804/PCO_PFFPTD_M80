# input
"""
-> a function which is used to get the input from the user
-> Syntax:
            Var = input(message)
            where, message is not mandatory
-> By default the input will always be in the form of string
"""

# a = input("Enter the value : ")
# print(a)
# print(type(a))
"""
Enter the value : hello
hello
<class 'str'>

Enter the value : 10
10
<class 'str'>

Enter the value : 9.86
9.86
<class 'str'>
"""

# to take integer input
# a = int(input("Enter the value : "))
# print(a)
# print(type(a))
"""
Enter the value : 87689
87689
<class 'int'>
"""

# to take float input -> float(input())

# to take complex input -> complex(input())

# to take boolean input -> complex(input())

# a = list(input("Enter the value : "))
# print(a)
# print(type(a))
"""
['[', '1', '0', ',', ' ', '2', '0', ']']
<class 'list'>
"""

#############################################################################################
"""
-> To consider input for any datatype we make use of the eval function,
        eval(input(message))
"""

val = eval(input('Enter the value : '))
print(val)
print(type(val))
"""
Enter the value : 10
10
<class 'int'>

Enter the value : [10, 20, 30]
[10, 20, 30]
<class 'list'>

Enter the value : {'a': 10, 'b': 30}
{'a': 10, 'b': 30}
<class 'dict'>
"""


