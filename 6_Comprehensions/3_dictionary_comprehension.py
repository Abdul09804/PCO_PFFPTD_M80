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

#

