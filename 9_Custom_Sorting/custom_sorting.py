# custom sorting

nums = [12, 3, 875, 134, 97, 34, 53, 65]
print(nums.sort())      # None
print(nums)     # [3, 12, 34, 53, 65, 97, 134, 875]

names = ['alex', 'stella', 'joseph', 'michael']
print(names.sort())     # None
print(names)        # ['alex', 'joseph', 'michael', 'stella']

s = 'abcd'
# s.sort()        # AttributeError

nums = [12, 3, 875, 134, 97, 34, 53, 65]
print(sorted(nums))     # [3, 12, 34, 53, 65, 97, 134, 875]
print(nums)             # [12, 3, 875, 134, 97, 34, 53, 65]

words = ['python', 'c', 'ruby', 'manual', 'java', 'pearl', 'javascript']
print(sorted(words))                # ['c', 'java', 'javascript', 'manual', 'pearl', 'python', 'ruby']
print(sorted(words, reverse=True))  # ['ruby', 'python', 'pearl', 'manual', 'javascript', 'java', 'c']
print(sorted(words, key=len))       # ['c', 'ruby', 'java', 'pearl', 'python', 'manual', 'javascript']
print(sorted(words, key=len, reverse=True))    # ['javascript', 'python', 'manual', 'pearl', 'ruby', 'java', 'c']

nums = [(22, 1), (2, 12), (4, 3), (21, 4), (8, 12), (12, 28), (12, 9)]
print(sorted(nums))     # [(2, 12), (4, 3), (8, 12), (12, 9), (12, 28), (21, 4), (22, 1)]

s = 'hello'
print(sorted(s))        # ['e', 'h', 'l', 'l', 'o']

s = {12, 3, 875, 134, 97, 34, 53, 65}
print(sorted(s))        # [3, 12, 34, 53, 65, 97, 134, 875]

d = {'hello': 5, 'everyone': 8, 'good': 4, 'evening': 7}
print(sorted(d))        # ['evening', 'everyone', 'good', 'hello']
print(sorted(d.values()))       # [4, 5, 7, 8]
print(sorted(d.items()))        # [('evening', 7), ('everyone', 8), ('good', 4), ('hello', 5)]

#########################################################################################

words = ['hello', 'everyone', 'welcome', 'to', 'python', 'class']

print(sorted(words))                    # ['class', 'everyone', 'hello', 'python', 'to', 'welcome']
print(sorted(words, reverse=True))      # ['welcome', 'to', 'python', 'hello', 'everyone', 'class']
print(sorted(words, key=len))                   # ['to', 'hello', 'class', 'python', 'welcome', 'everyone']
print(sorted(words, key=len, reverse=True))     # ['everyone', 'welcome', 'python', 'hello', 'class', 'to']

#########################################################################################

