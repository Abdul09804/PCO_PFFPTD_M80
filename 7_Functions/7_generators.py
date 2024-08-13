# generators

# def even():
#     for num in range(1, 21):
#         if num % 2 == 0:
#             return num

# res = even()
# print(res)

# def _even():
#     for num in range(1, 21):
#         if num % 2 == 0:
#             yield num
#
# _res = _even()
# print(_res)     # <generator object _even at 0x000001C5BD9BFED0>
# print(list(_res))        # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# print(type(_res))   # <class 'generator'>

# _res = _even()
# for i in _res:
#     print(i)

# _res = _even()
# print(next(_res))       # 2
# print(next(_res))       # 4
# print(next(_res))       # 6
# print(next(_res))
# print(next(_res))
# print(next(_res))
# print(next(_res))
# print(next(_res))
# print(next(_res))
# print(next(_res))
# print(next(_res))       # StopIteration

"""
We can access the values present in generator object using 
1) typecasting
2) for loop
3) next()
"""

st = 'hello'
# print(next(st))     # TypeError

"""
1) Iterators
-> zip, enumerate, map, filter, generators
-> iterate over them using for loop
-> it does not have length
-> next() can be applied
-> can not re-initialise itself

2) Iterables
-> str, list, tuple, set, dictionary, range
-> iterate over them using for loop
-> it  has length
-> next can not be applied
-> gets reinitialised on it's own
"""

# _res = _even()
# # print(len(_res))    # TypeError

# l = [1, 2, 3, 4]
# for i in l:
#     print(i)
#
# for i in l:
#     print(i)
#
# res = enumerate(l)
# for i in res:
#     print(i)
#
# res = enumerate(l)
# for i in res:
#     print(i)

# print(next(res))    # StopIteration

# res = enumerate(l)
# print(next(res))    # (0, 1)
# print(next(res))    # (1, 2)
# for i in res:
#     print(i)

#####################################################################################

def spam():
    print('Hello')
    return 1
    return 2
    return 3

# res = spam()    # 'hello'
# print(res)      # 1

def _spam():
    print('Hello')
    yield 1
    yield 2
    yield 3

# res = _spam()
# print(res)  # <generator object _spam at 0x0000024162BB5480>
# print(list(res))
"""
Hello
[1, 2, 3]
"""

# res = _spam()
# print(next(res))
"""
Hello
1
"""
# print(next(res))    # 2
# print(next(res))    # 3
# print(next(res))    # StopIteration

def spam_gen():
    print('Hello')
    yield 10
    print('Good morning')
    yield 20
    print('How are you')
    yield 30

res = spam_gen()
print(next(res))
"""
Hello
10
"""

print(next(res))
"""
Good morning
20
"""

print(next(res))
"""
How are you
30
"""

# print(next(res))    # StopIteration

###################################################################################

# generate even numbers

def even_gen():
    print('Initialising generator')
    num = 1
    while True:
        if num % 2 == 0:
            yield num
        num += 1

# res = even_gen()
# # print(list(res))
# print(next(res))
# print(next(res))
# for i in range(1, 101):
#     print(next(res))

# list of names starting with vowels using generators

names = ['alex', 'iqbal', 'eve', 'bob', 'clare', 'uday']

def vowel_names(iterable):
    for name in iterable:
        if name[0] in 'aeiouAEIOU':
            yield name

res = vowel_names(names)
print(next(res))        # alex
print(list(res))        # ['iqbal', 'eve', 'uday']

###################################################################################

# create a countdown generator from 10 to 1

def countdown_gen():
    for i in range(10, 0, -1):
        yield i

res = countdown_gen()
print(next(res))
print(next(res))

###################################################################################

# generate infinite prime numbers

# generate infinite fibonacci series

####################################################################################


print(max(1, 4))    # 4
print(min(8, 6))    # 6

print(ord('a'))     # 97
print(chr(97))      # 'a'

