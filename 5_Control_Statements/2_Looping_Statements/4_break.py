# break
"""
-> break is a keyword which is used to terminate from the loop in between the execution
-> we can break both for and while loop
"""

for i in range(1, 11):
    print(i)
    if i == 5:
        break
"""
1
2
3
4
5
"""

# 1) WAP to print the index of first occurrence of a given character in a string
st = 'mississippi'
ch = 's'
# o/p = 2
for i in range(len(st)):
    if st[i] == ch:
        print(i)
        break

# 2) WAP to print the index of second occurrence of a given character in a string
st = 'mississippi'
ch = 's'
# o/p = 3
count = 0
for i in range(len(st)):
    if st[i] == ch:
        count += 1
        if count == 2:
            print(i)
            break

"""
3) WAP to print the index of first occurrence of a given character in a string,  
   if the character is not present then print False
"""
st = 'mississippi'
ch = 'i'
for i in range(len(st)):
    if st[i] == ch:
        print(i)
        break
else:
    print(False)

"""
4) WAP to print the second vowel in a given string, if the vowel is not present then print
   False
"""

st = 'python'
count = 0
for ch in st:
    if ch in 'aeiouAEIOU':
        count += 1
        if count == 2:
            print(ch)
            break
else:
    print(False)

# 5) WAP to check if a given list is homogenous or not using break keyword

l = [1, 2, 8, 3, 4, 5]
for val in l:
    if type(l[0]) != type(val):
        print('Heterogeneous List')
        break
else:
    print('Homogenous List')

# 6) WAP to check if a given number is a prime number
num = 15
for i in range(2, num//2 + 1):
    if num % i == 0:
        print('Not a prime number')
        break
else:
    print('Prime Number')

# 7) WAP to check if a given string has only alphabets

st = 'GoogLe'
for ch in st:
    if not ('A' <= ch <= 'Z' or 'a' <= ch <= 'z'):
        print(False)
        break
else:
    print(True)

# 8) WAP to check if a given string has only uppercase characters
# 9) WAP to check if a given string has only lowercase characters
# 10) WAP to check if a given string has only alphanumeric characters

# 11) Guess the number


while 4 > 3:
    print('hello')


