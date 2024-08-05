# dictionary comprehension
"""
Syntax:
        Var = {key:value  for_loop}

"""

# build a dictionary of word and length pair in the sentence
sentence = "The Wings of Fire"
res = {word: len(word) for word in sentence.split()}
print(res)  # {'The': 3, 'Wings': 5, 'of': 2, 'Fire': 4}

# flip the keys and values using dictionary comprehension
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
res1 = {d[key]: key for key in d}
res2 = {value: key for key, value in d.items()}
print(res1)      # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
print(res2)      # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

for i, j in d.items():
    print(i, j)
"""
a 1
b 2
c 3
d 4
"""

# word count
sentence = "hello world welcome to python world hello everyone this is python world"
words = sentence.split()
res = {word: words.count(word) for word in words}
print(res)      # {'hello': 2, 'world': 3, 'welcome': 1, 'to': 1, 'python': 2, 'everyone': 1, 'this': 1, 'is': 1}

# character count
st = 'mississippi'
res = {ch: st.count(ch) for ch in st}
print(res)      # {'m': 1, 'i': 4, 's': 4, 'p': 2}

# dictionary of characters and it's ASCII values
st = 'iguitad'
res = {ch: ord(ch) for ch in st}
print(res)      # {'i': 105, 'g': 103, 'u': 117, 't': 116, 'a': 97, 'd': 100}

# create a dictionary of index numbers and characters from a given string

st = 'hello'
res = {index: st[index] for index in range(len(st))}
print(res)      # {0: 'h', 1: 'e', 2: 'l', 3: 'l', 4: 'o'}

for i in enumerate(st):
    print(i)
"""
(0, 'h')
(1, 'e')
(2, 'l')
(3, 'l')
(4, 'o')
"""

for index, val in enumerate(st):
    print(index, val)
"""
0 h
1 e
2 l
3 l
4 o
"""

for num, val in enumerate(st, start=10):
    print(num, val)
"""
10 h
11 e
12 l
13 l
14 o
"""

st = 'hello'
res = {index: val for index, val in enumerate(st)}
print(res)      # {0: 'h', 1: 'e', 2: 'l', 3: 'l', 4: 'o'}

# dictionary of word and length pair only if the word in a palindrome
st = 'hello eve do you know malayalam'
res = {word: len(word) for word in st.split() if word == word[::-1]}
print(res)      # {'eve': 3, 'malayalam': 9}


# WAP to map 2 iterables in the form of dictionary

st = 'abcd'
l = [1, 2, 3, 4]

for i in zip(l, st):
    print(i)
"""
(1, 'a')
(2, 'b')
(3, 'c')
(4, 'd')
"""

for i, j in zip(l, st):
    print(i, j)
"""
1 a
2 b
3 c
4 d
"""

for i, j, k in zip([1, 2, 3, 4], 'abc', (10, 20, 30, 40, 50)):
    print(i, j, k)
"""
1 a 10
2 b 20
3 c 30
"""

st = 'abcd'
l = [1, 2, 3, 4]
res = {key: val for key, val in zip(st, l)}
print(res)      # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

#########################################################################################

# build a dictionary whose value is more than 200
prices = {
    'ACME': 45.23,
    'AAPL': 612.65,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

res = {key: value for key, value in prices.items() if value >= 200}
print(res)       # {'AAPL': 612.65, 'IBM': 205.55}

# build a dictionary whose share is less than 100

# dictionary of country and dial code
# dictionary of dial code and country

dial_codes = [
    (86, 'China'),
    (91, 'India'),
    (44, 'United Kingdom'),
    (1, 'United States'),
    (92, 'Pakistan')
]

res1 = {country: dial_code for country, dial_code in dial_codes}
res2 = {dial_code: country for country, dial_code in dial_codes}
print(res1)     # {86: 'China', 91: 'India', 44: 'United Kingdom', 1: 'United States', 92: 'Pakistan'}
print(res2)     # {'China': 86, 'India': 91, 'United Kingdom': 44, 'United States': 1, 'Pakistan': 92}



