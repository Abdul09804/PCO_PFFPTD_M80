# nested loops

# for i in 'abc':
#     for j in '123':
#         print(i, j)
"""
a 1
a 2
a 3
b 1
b 2
b 3
c 1
c 2
c 3
"""
# for i in 'AB':
#     for j in 'ab':
#         for k in '12':
#             print(i, j, k)

"""
A a 1
A a 2
A b 1
A b 2
B a 1
B a 2
B b 1
B b 2
"""

# 1) WAP to get the following output without using len

st = "python programming language"
#o/p = [6, 11, 8]
# words = st.split()
# res = []
# for word in words:
#     count = 0
#     for ch in word:
#         count += 1
#     res.append(count)
# print(res)

# o/p = {'python': 6, 'programming': 11, 'language': 8}
# st = "python programming language"
# words = st.split()
# res = {}
# for word in words:
#     count = 0
#     for ch in word:
#         count += 1
#     res[word] = count
# print(res)

# 2) WAP to create a list of numbers from 1 to 5 along with it's factorial
# o/p = [(1, 1), (2, 2), (3, 6), (4, 24), (5, 120)]

# fact = []
# for n in range(1, 6):
#     p = 1
#     for i in range(1, n+1):
#         p *= i
#     fact.append((n, p))
# print(fact)

# 3) WAP to get the following output
"""
num_list = [[1, 8, 7], [7, 5], [4, 10, 27], [9, 10, 96, 5]]
o/p = [16, 12, 41, 120]
"""

# num_list = [[1, 8, 7], [7, 5], [4, 10, 27], [9, 10, 96, 5]]
# out = []
# for i in num_list:
#     s = 0
#     for j in i:
#         s += j
#     out.append(s)
# print(out)

# 4) WAP to print all the prime numbers between the range m, n
"""
m = 2
n = 20
O/p -> 2 3 5 7 11 13 17 19
"""
# m, n = 1, 10
# for num in range(m, n+1):
#     if num > 1:
#         for i in range(2, num//2 + 1):
#             if num % i == 0:
#                 break
#         else:
#             print(num)

# 5) WAP to print 'n' prime numbers
"""
n = 5 -> 2 3 5 7 11
n = 8 -> 2 3 5 7 11 13 17 19
"""

n = 25
num = 2
count = 0
while True:
    if count == n:
        break       # this breaks outer loop

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            break           # inner loop
    else:
        print(num)
        count += 1

    num += 1

# 6) WAP to print 'n'th prime number
"""
n = 4 -> 7
n = 25 -> 97
"""

n = 7
num = 2
count = 0
while True:

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            break           # inner loop
    else:
        count += 1

    if count == n:
        print(num)
        break       # this breaks outer loop

    num += 1


# 7) WAP to print all the armstrong numbers between the range m, n
"""
371 -> 3**3 + 7**3 + 1**3 = 27 + 343 + 1 = 371  -> Armstrong
370 -> 3**3 + 7**3 + 0**3 = 370 -> Armstrong
123 -> 1**3 + 2**3 + 3**3 = 1 + 8 + 27 = 36 -> No
1634 -> 1**4 + 6**4 + 3**4 + 4**4 = 1 + 1296 + 81 + 256 = 1634 -> Armstrong
"""
# 8) WAP to print 'n' armstrong numbers
# 9) WAP to print 'n'th armstrong number

# 10) WAP to print all the harshad numbers between the range m, n
"""
if a number is exactly divisible by sum of it's digits then the number is a Harshad number
12 -> 1 + 2 = 3 -> 12 % 3 == 0 -> True -> Harshad number
34 -> 3 + 4 = 7 -> 34 % 7 == 0 -> False -> No
21 -> 2 + 1 = 3 -> 21 % 3 == 0 -> True -> Harshad number
"""
# 11) WAP to print 'n' harshad numbers
# 12) WAP to print 'n'th harshad number

# 13) WAP to print all the perfect numbers between the range m,n
# 14) WAP to print 'n' perfect numbers
# 15) WAP to print 'n'th perfect number


# 16) WAP to 'n' fibonacci numbers
"""
fibonacci series -> 0 1 1 2 3 5 8 13 21 34 ....................
"""

n = 10
num1 = 0
num2 = 1
if n == 1:
    print(num1)
else:
    print(num1, num2, sep='\n')
    count = 2                       # 2 fibonacci numbers are already printed
    while count < n:
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        print(num2)
        count += 1

"""
n = 6
num1 = 0 -> 1 -> 1 -> 2 -> 3
num2 = 1 -> 1 -> 2 -> 3 -> 5
0 1 1 2 3 5
count = 2 -> 3 -> 4 -> 5 -> 6

2 < 6 -> True
num3 = 0 + 1 = 1
num1 = 1
num2 = 1

3 < 6 -> True
num3 = 1 + 1 = 2 
num1 = 1
num2 = 2

4 < 6 -> True
num3 = 1 + 2 = 3
num1 = 2
num2 = 3

5 < 6 -> True
num3 = 2 + 3 = 5
num1 = 3 
num2 = 5

6 < 6 -> False 
"""

# 17) WAP to print 'n'th fibonacci number




