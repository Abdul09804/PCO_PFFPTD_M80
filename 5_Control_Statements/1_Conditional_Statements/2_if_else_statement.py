# if else statement
"""
-> if the condition is True, control will execute TSB, if the condition is False,
   control will execute FSB
-> Syntax:
            if <condition>:
                TSB
            else:
                FSB
"""

# 1) WAP to check if a given number is odd or even number
# num = int(input('Enter the number : '))
# if num % 2 != 0:
#     print('odd number')
# else:
#     print('even number')

# 2) WAP to check if a given character is a lowercase character or not
# char = input('Enter the character : ')
# if 'a' <= char <= 'z':
#     print('Lowercase Character')
# else:
#     print('not a lowercase character')

# 3) WAP to check if a character is a special character or an alphanumeric character

# 4) WAP to check if the given data is a single value datatype
# data = eval(input('Enter the data : '))
# if type(data) in [int, float, complex, bool]:
#     print('Single Value datatype')
# else:
#     print('Multivalue datatype')

# 5) WAP to check if a given data is a mutable datatype
# data = eval(input('Enter the data : '))
# if type(data) in [list, set, dict]:
#     print('Mutable Datatype')
# else:
#     print('Immutable Datatype')

# 6) WAP to check if a character is a vowel
# char = input('Enter the character : ')
# if char in 'aeiouAEIOU':
#     print('Vowel')
# else:
#     print('Not a vowel')


# 7) WAP to check if a character is a consonant
""" ('A'<=ch<='Z' or 'a'<=ch<='z') and char not in 'aeiouAEIOU' """

# 8) WAP to check whether a character is present in the string
# st = input('Enter the string : ')
# ch = input('Enter the character : ')
# if ch in st:
#     print(True)
# else:
#     print(False)

# 9) WAP to check whether a given string is a palindrome
""" madam racecar mom malayalam """
# st = input('Enter the string : ')
# if st == st[::-1]:
#     print(f"The given string '{st}' is a palindrome")     # print("The given string", st, "is a palindrome")
# else:
#     print(f"The given string '{st}' is not a palindrome")

# 10) WAP to check if string has even number of values
# st = 'apple'
# if len(st) % 2 == 0:
#     print(True)
# else:
#     print(False)

# 11) WAP to check if the given list has a mid-value, if it has then print the mid-value

# l = [11, 22, 33, 44, 55]
# if len(l) % 2 != 0:
#     print('The list has mid value')
#     mid_index = len(l)//2
#     print(f"The mid value is {l[mid_index]}")
# else:
#     print('The list has no mid value')

"""
len     mid-index
1           0
3           1
5           2
7           3
.
n           n//2
"""


