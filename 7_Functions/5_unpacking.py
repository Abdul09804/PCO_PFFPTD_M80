# unpacking
def sam():
    return 1, 2, 3

print(sam())    # (1, 2, 3)
a, b, c = sam()
print(a, b, c)  # 1 2 3

name = 'eve'
c1, c2, c3 = 'eve'
print(c1, c2, c3)   # e v e

d = {'a': 1, 'b': 2}
k1, k2 = d
print(k1, k2)   # a b

a, b = {'hai', 3}
print(a, b)     # 3 hai

st = 'hello world'
# first = st[0]
# second = st[1]
# last_second = st[-2]
# last = st[-1]
first, second, *rest, last_second, last = st
print(first, second, last_second, last)     # h e l d
print(rest)     # ['l', 'l', 'o', ' ', 'w', 'o', 'r']
""" values are packed in the form of list """
print(''.join(rest))        # llo wor

print(*rest)    # l l o   w o r

"""
* -> when used while declaring a fuction or outside the function acts as packing operator
  -> when used while calling the function it acts as unpacking operator
"""

names = ['alex', 'steve', 'joseph', 'mary', 'john', 'stella', 'grace']
name1, name2, *rest, name3, name4 = names
print(name1, name2, name3, name4)   # alex steve stella grace
print(rest)     # ['joseph', 'mary', 'john']
print(*rest)    # joseph mary john

print('joseph')     # joseph
print(*'joseph')    # j o s e p h

names1 = ['alex', 'steve', 'joseph', 'mary']
names2 = ['john', 'stella', 'grace']
names = names1 + names2
print(names)    # ['alex', 'steve', 'joseph', 'mary', 'john', 'stella', 'grace']

names = [*names1, *names2]
print(names)    # ['alex', 'steve', 'joseph', 'mary', 'john', 'stella', 'grace']

print(*names1, *names2)     # alex steve joseph mary john stella grace

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
print(d1, d2)   # {'a': 1, 'b': 2} {'c': 3, 'd': 4}

d = {*d1, *d2}
print(d)    # {'d', 'a', 'c', 'b'}

d = {**d1, **d2}
print(d)    # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# print(**d1)     # TypeError

print(*d)       # a b c d
print(*d.values())  # 1 2 3 4
print(*d.items(), sep='\n')    # ('a', 1) ('b', 2) ('c', 3) ('d', 4)

