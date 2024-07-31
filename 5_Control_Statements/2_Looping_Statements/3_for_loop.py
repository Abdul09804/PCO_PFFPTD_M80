# for loop
"""
-> Syntax:
            for item in iterable:
                SB
-> initialization and updation are automated
-> The loop will get executed number of times which is equal to length of the collection
-> we can directly access the values without index numbers
"""

for ch in 'abcd':
    print(ch)
"""
a
b
c
d
"""

for val in [1, 2.7, True, 9+8j, 'hello', [1, 2]]:
    print(val)
"""
1
2.7
True
(9+8j)
hello
[1, 2]
"""

for num in (1, 2, 3, 4):
    print((num, num**2))
"""
(1, 1)
(2, 4)
(3, 9)
(4, 16)
"""

for val in {True, 9+8j, 'hello'}:
    print(val)
"""
True
hello
(9+8j)
"""

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

for i in d:
    print(i)
"""
a
b
c
d
"""

for key in d.keys():
    print(key)
"""
a
b
c
d
"""

for key in d:
    print(d[key])
"""
1
2
3
4
"""

for val in d.values():
    print(val)
"""
1
2
3
4
"""

for key in d:
    print((key, d[key]))
"""
('a', 1)
('b', 2)
('c', 3)
('d', 4)
"""

for item in d.items():
    print(item)
"""
('a', 1)
('b', 2)
('c', 3)
('d', 4)
"""

for i in range(1, 6):
    print(i)
"""
1
2
3
4
5
"""

for i in range(5):
    print(i)
"""
0
1
2
3
4
"""
st = 'apple'
for index in range(len(st)):
    print(index)
"""
0
1
2
3
4
"""

for index in range(len(st)):
    print(index, st[index])
"""
0 a
1 p
2 p
3 l
4 e
"""

###########################################################################################

# 1) WAP to extract all the vowels in a given string

st = 'airways'
vowels = ''
for i in st:
    if i in 'aeiouAEIOU':
        vowels += i
print(vowels)       # aia

# 2) WAP to extract all the float numbers from a given list

"""
3) WAP to extract all the string present in a tuple to a dictionary where key is the 
   string and value is the length of the string
"""

t = ('bob', True, 'steve', 9.87, 'alexander')
d = {}
for i in t:
    if type(i) == str:
        d[i] = len(i)
print(d)        # {'bob': 3, 'steve': 5, 'alexander': 9}

# 4) WAP to count the number of occurrence of a given character in a string without using count

st = 'mississippi'
ch = 's'
# o/p = 4
count = 0
for i in st:
    if i == ch:
        count += 1
print(count)

# 5) WAP to get the following output
"""
st = 'aabcabccbaac'
# o/p = 'a5b3c4'
"""
st = 'aabcabccbaac'
res = ''
for i in st:
    if i not in res:
        res = res + i + str(st.count(i))    # '' + 'a' + '5' = 'a5'
print(res)  # a5b3c4

res = {}
for i in st:
    res[i] = st.count(i)
print(res)      # {'a': 5, 'b': 3, 'c': 4}

res = {}
for i in st:
    if i not in res:
        res[i] = 1
    else:
        res[i] += 1
print(res)

# 6) WAP to find the length of a list without using len

l = ['hello', 87, 9.75, [1, 2], 2-7j, ('a',)]
count = 0
for _ in l:     # throw away variable
    count += 1
print(count)    # 6

# 7) WAP to remove all duplicates from the string
"""
st = 'mississippi'
# o/p = misp
"""

# 8) WAP to extract all odd integer values present at even index in a given list
""" for i in range(len(l)) -> if i % 2 == 0 and l[i] % 2 != 0 """

# 9) WAP to create a tuple of 'n' natural numbers along with it's cube
""" res += ((n, n**3),) """

# 10) WAP to check if a given list is homogeneous

l = [1, 2.8, 3, 4, 5]
count = 0
for i in l:
    if type(l[0]) == type(i):
        count += 1
if count == len(l):
    print('Homogenous')
else:
    print('Heterogeneous')

# 11) WAP to create a list of all the factors of a given number
"""
8 -> 1 2 4 8
12 -> 1 2 3 4 6 12
7 -> 1 7
"""
num = 1000
factors = []
for n in range(1, num+1):
    if num % n == 0:    # n is a factor of num
        factors.append(n)
print(factors)

# 12) WAP to check if a given number is perfect number
"""
6 -> 1 + 2 + 3 = 6 -> Perfect number
18 -> 1 + 2 + 3 + 6 + 9 = 21 -> not a perfect number
28 -> 1 + 2 + 4 + 7 + 14 = 28 -> Perfect number 
15 -> 1 + 3 + 5 = 8 -> not a perfect number
"""

num = 28
sum_of_factors = 0
for n in range(1, num//2+1):
    if num % n == 0:
        sum_of_factors += n
if sum_of_factors == num:
    print('The given number is a perfect number')
else:
    print('Not a perfect number')

# 13) WAP to reverse the key and values of a dictionary

d = {'apple': 120, 'orange': 60, 'banana': 80, 'pineapple': 100}
res = {}
for i in d:
    res[d[i]] = i
print(res)      # {120: 'apple', 60: 'orange', 80: 'banana', 100: 'pineapple'}

# 14) WAP to check if a given number is a prime number












