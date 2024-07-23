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
data = eval(input('Enter the data : '))
if type(data) in [list, set, dict]:
    print('Mutable Datatype')
else:
    print('Immutable Datatype')

# 6) WAP to check if a character is a vowel
char = input('Enter the character : ')
if char in 'aeiouAEIOU':
    print('Vowel')
else:
    print('Not a vowel')


# 7) WAP to check if a character is a consonant
""" ('A'<=ch<='Z' or 'a'<=ch<='z') and char not in 'aeiouAEIOU' """

