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

n = 10
s = 0
i = 1
while i <= n:
    s += i
    i += 1
print(f"The num of first {n} natural numbers is {s}")
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



