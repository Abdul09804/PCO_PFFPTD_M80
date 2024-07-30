# while loop
"""
-> TSB gets executed until the given condition is False
-> Syntax:
            initialise
            while <condition>:
                TSB
                updation
-> If the looping variable is not intialized, control will throw NameError
-> If the value is not updated, the loop becomes infinite
"""
# 1) WAP to print the numbers from 1 to 10

# i = 1
# while i <= 10:
#     print(i)
#     i = i + 1

# 2) WAP to print the numbers from 1 to 10 along with their squares
"""
(1, 1)
(2, 4)
(3, 9)
.
.
.
(10, 100)
"""
# i = 1
# while i <= 10:
#     print((i, i**2))
#     i = i + 1

# 3) WAP to print the tables of a given number
"""
n = 7
7 * 1 = 7
7 * 2 = 14
7 * 3 = 21
.
.
7 * 10 = 70
"""

# n = int(input('Enter the number : '))
# i = 1
# while i <= 10:
#     print(f"{n} * {i} = {n*i}")
#     i += 1

# 4) WAP to print the numbers from 10 to 1
# i = 10
# while i >= 1:
#     print(i)
#     i -= 1

# 5) WAP to find the sum of first 'n' natural numbers

# n = 10
# s = 0
# i = 1
# while i <= n:
#     s += i
#     i += 1
# print(f"The num of first {n} natural numbers is {s}")
"""
n = 4
s = 0 -> 1 -> 3 - > 6 -> 10
i = 1 -> 2 -> 3 -> 4 -> 5

1 <= 4
s = 0 + 1 = 1

2 <= 4
s = 1 + 2 = 3

3 <= 4
s = 3 + 3 = 6

4 <= 4
s = 6 + 4 = 10

5 <= 4 -> False
"""

# 6) WAP to find the product of first 'n' natural numbers

# n = int(input('Enter the number : '))
# i = 1
# p = 1
# while i <= n:
#     p *= i
#     i += 1
# print(f"The product of first '{n}' natural numbers is {p}")

# 7) WAP to print all the characters present at odd index numbers

# st = 'hello'
# i = 0
# while i < len(st):
#     if i % 2 != 0:
#         print(st[i])
#     i += 1

# 8) WAP to print the values present at even index in a given list

# 9) WAP to print all the uppercase characters in a given string

st = 'HEllO WoRld'
i = 0
while i < len(st):
    if 'A' <= st[i] <= 'Z':
        print(st[i])
    i += 1

st = 'HEllO WoRld'
i = 0
while i < len(st):
    if st[i].isupper() == True:        # st[i].isupper()
        print(st[i])
    i += 1


# 10) WAP to print all the lowercase characters in a given string
# 11) WAP to print all the numeric characters in a given string
# 12) WAP to print all the special characters in a given string


# 13) WAP to extract all the vowels in a given string

st = 'AeroPlane'
# Aeoae
vowels = ''
i = 0
while i < len(st):
    if st[i] in 'aeiouAEIOU':
        vowels += st[i]
    i += 1

print(vowels)

"""
st = 'AeroPlane'
i = 0
vowels = '' -> 'A'

'A' in 'aeiouAEIOU' -> True
vowels = '' + 'A' = 'A'

'e' in 'aeiouAEIOU' -> True
vowels = 'A' + 'e' = 'Ae'

'r' in 'aeiouAEIOU' -> False
"""

# 14) WAP to extract all the even numbers in a given list

l = [2, 8, 81, 87, 99, 24, 88, 55, 44]
out = []
i = 0
while i < len(l):
    if l[i] % 2 == 0:
        out += [l[i]]
    i += 1
print(out)

"""
out = [] + [2] = [2]
out = [2] + [8] = [2, 8]
"""

# 15) WAP to extract all the consonants in a given string

# 16) WAP to find the sum of all real numbers present in a given list

li = [3, 8.65, 9+7j, 23, 9.123, 8.34, 'hai', False, 9.99]
# o/p = 62.103
s = 0
i = 0
while i < len(li):
    if type(li[i]) in [int, float]:
        s += li[i]
    i += 1
print(s)

# 17) WAP to extract all the string dataitems in a given tuple to another tuple

t = ('hai', 7.9, '123', 123, 'python', 'data')
out = ()
i = 0
while i < len(t):
    if type(t[i]) == str:
        out += (t[i],)
    i += 1
print(out)

# 18) WAP to count all the numbers between 1 and 200 which are divisible by 3

# 19) WAP to create a list of all numbers between 100 and 3500 which are divisible by both 5 and 7

# 20) WAP to separate all the even and odd numbers to a separate list

# 21) WAP to separate all the characters from a given string

# 22) WAP to reverse a given string without using slicing

# Method 1
st = 'data'
# atad
out = ''
i = -1
while i >= -len(st):
    out += st[i]
    i -= 1
print(out)
"""
st = 'data'
out = '' -> 'a' -> 'at' -> 'ata' -> 'atad'
i = -1 -> -2 -> -3 -> -4 -> -5

-1 >= -4 -> True
out = '' + 'a' = 'a'

-2 >= -4 -> T
out = 'a' + 't' = 'at'

-3 >= -4 -> T
out = 'at' + 'a' = 'ata'

-4 >= -4 -> T
out = 'ata' + 'd' = 'atad'

-5 >= -4 -> False
"""

# Method 2
st = 'data'
# atad
out = ''
i = len(st) - 1
while i >= 0:
    out += st[i]
    i -= 1
print(out)

# Method 3
st = 'data'
rev = ''
i = 0
while i < len(st):
    rev = st[i] + rev
    i += 1
print(rev)
"""
st = 'data'
rev = '' -> 'd' -> 'ad' -> 'tad' -> 'atad'
i = 0 -> 1 -> 2 -> 3 -> 4

rev = 'd' + '' = 'd'

rev = 'a' + 'd' = 'ad'

rev = 't' + 'ad' = 'tad'

rev = 'a' + 'tad' = 'atad'
"""

# 23) WAP to check if a given string is a palindrome or not
st = 'icici'
rev = ''
i = 0
while i < len(st):
    rev = st[i] + rev
    i += 1
if st == rev:
    print('The given string is a palindrome')
else:
    print('The given string is not a palindrome')

# 24) WAP to reverse a given number without typecasting or slicing

num = 865
temp = num
rev = 0
while temp != 0:        # temp > 0
    rev = rev*10 + temp % 10
    temp = temp // 10
print(f"The reverse of given number {num} is {rev}")

"""
num = 865
temp = 865 -> 86 -> 8 -> 0
rev = 0 -> 5 -> 56 -> 568

865 != 0
rev = 0*10 + 5 = 5
temp = 865 // 10 = 86

86 != 0
rev = 5*10 + 6 = 56
temp = 86 // 10 = 8

8 != 0
rev = 56*10 + 8 = 568
temp = 8 // 10 = 0

0 != 0 -> False
"""

# 25) WAP to check if a given number is a palindrome



