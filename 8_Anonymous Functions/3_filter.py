# filter
"""
-> Syntax:
            filter(func, iterable)
-> The input collection will be filtered based on the value obtained from the function
-> If the function returns default value, the corresponding input will be skipped from
   the collection, if the functions returns a non default value, the corresponding
   input will be stored in filter object
"""
even = lambda num: num % 2 == 0

print(list(map(even, range(1, 6))))     # [False, True, False, True, False]
print(list(filter(even, range(1, 6))))    # [2, 4]

even = lambda num: num**2 if num % 2 == 0 else 0
print(list(map(even, range(1, 6))))     # [0, 4, 0, 16, 0]
print(list(filter(even, range(1, 6))))  # [2, 4]

# filter only words whose length is equal to 5
sentence = "hello steve where are you going"
res = filter(lambda word: len(word) == 5, sentence.split())
print(list(res))        # ['hello', 'steve', 'where', 'going']

# extract the name which is a plaindrome
names = ['steve', 'eve', 'bob', 'alex', 'gagan']
print(list(filter(lambda name: name == name[::-1], names)))     # ['eve', 'bob']

# extract all the squares of even numbers in a given list

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = filter(lambda num: num % 2 == 0, li)
res = map(lambda num: num**2, evens)
print(list(res))        # [4, 16, 36, 64, 100]

# WAP to count the number of occurrence of a given character in a string without using count in type2 and type4 func

st = 'mississippi'
ch = 's'
# o/p = 4
count = 0
for i in st:
    if i == ch:
        count += 1
print(count)

