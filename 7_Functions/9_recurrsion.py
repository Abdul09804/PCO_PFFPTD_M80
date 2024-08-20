# recurrsion
"""
-> Calling a function inside the same function is called recurrsion
-> Syntax:
        def fname(args):
            if <cond>:
                return values
            ---------
            ---------
            return fname(args)

        def fname(args):
            if <cond>:
                return
            ---------
            ---------
            fname(args)
"""

# 1) find the sum of 'n' natural numbers using recursion
"""
Logic
n = 1 -> sum(1) -> 1
n = 2 -> sum(2) -> 2 + 1 -> 2 + sum(1)
n = 3 -> sum(3) -> 3 + 2 + 1 -> 3 + sum(2)
.
.
sum(n) -> n + sum(n-1)
"""

def _sum(n):
    if n == 1:
        return 1
    return n + _sum(n-1)

print(_sum(4))      # 10


# find the product of 'n' numbers using recursion

def prod(n):
    if n == 1:
        return 1
    return n * prod(n-1)

print(prod(5))      # 120

####################################################################################
"""
program to get the following output
li = [1, 2, [3, 4, [5, 6]]]
o/p = 21
"""

li = [1, 2, [3, 4, [5, 6]]]
s = 0
for i in li:
    if type(i) == int:
        s += i
    elif type(i) == list:
        for j in i:
            if type(j) == int:
                s += j
            elif type(j) == list:
                for k in j:
                    if type(k) == int:
                        s += k


def _sum(li):
    s = 0
    for i in li:
        if type(i) == int:
            s += i
        elif type(i) == list:
            s += _sum(i)
    return s


li = [1, 2, [3, 4, [5, 6]]]
print(_sum(li))


# Steps to convert any while loop program to recursion
"""
1) Initialise all the looping variables in the formal argument section
2) Write the termination condition exactly opposite to looping condition
3) Return the total result inside termination condition
4) Write the logic of the program as it is excluding looping part and updation
5) Increment or decrement must be done in formal argument section only
"""

# WAP to extract all the lowercase characters in a given string
st = 'TueSdAY'
i = 0
res = ''
while i < len(st):
    if 'a'<=st[i]<='z':
        res += st[i]
    i += 1
print(res)

def lowercase(st, i=0, res=''):
    if i >= len(st):
        return res
    if 'a'<=st[i]<='z':
        res += st[i]
    return lowercase(st, i+1, res)

print(lowercase(st))        #


# WAP to reverse the given number without slicing or typecasting

num = 456
rev = 0
while num != 0:
    rev = rev*10 + num%10
    num = num // 10
print(rev)

def reverse_num(num, rev=0):
    if num == 0:
        return rev
    rev = rev * 10 + num % 10
    return reverse_num(num//10, rev)

print(reverse_num(456))

# WAP to extract all the string data items in a given list using recursion

li = [87, 'hello', 8.86, [1, 2, 3], 'hai', 'python']

def sam(li, i=0, res=[]):
    if i >= len(li):
        return res
    if type(li[i]) == str:
        res += [li[i]]
    return sam(li, i+1, res)

# print(sam(li))      # ['hello', 'hai', 'python']

