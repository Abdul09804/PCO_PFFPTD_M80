# nested loops

for i in 'abc':
    for j in '123':
        print(i, j)
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
for i in 'AB':
    for j in 'ab':
        for k in '12':
            print(i, j, k)

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
words = st.split()
res = []
for word in words:
    count = 0
    for ch in word:
        count += 1
    res.append(count)
print(res)

# o/p = {'python': 6, 'programming': 11, 'language': 8}
st = "python programming language"
words = st.split()
res = {}
for word in words:
    count = 0
    for ch in word:
        count += 1
    res[word] = count
print(res)

# 2) WAP to create a list of numbers from 1 to 5 along with it's factorial
# o/p = [(1, 1), (2, 2), (3, 6), (4, 24), (5, 120)]

fact = []
for n in range(1, 6):
    p = 1
    for i in range(1, n+1):
        p *= i
    fact.append((n, p))
print(fact)

# 3) WAP to get the following output





