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

