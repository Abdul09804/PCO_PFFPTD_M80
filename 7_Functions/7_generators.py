# generators

def even():
    for num in range(1, 21):
        if num % 2 == 0:
            return num

# res = even()
# print(res)

def _even():
    for num in range(1, 21):
        if num % 2 == 0:
            yield num

_res = _even()
# print(_res)     # <generator object _even at 0x000001C5BD9BFED0>
# print(list(_res))        # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# print(type(_res))   # <class 'generator'>

# _res = _even()
# for i in _res:
#     print(i)

_res = _even()
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

