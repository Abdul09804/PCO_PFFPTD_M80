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

words = ['hello', 'everyone', 'welcome', 'to', 'python', 'class']
def find_len(st):
    c = 0
    for _ in st:
        c += 1
    return c

print(sorted(words, key=find_len))      # ['to', 'hello', 'class', 'python', 'welcome', 'everyone']

######################################################################################

names = ['alex', 'mary', 'anthony', 'steve', 'stella', 'eve', 'john', 'amar']

def first_char(st):
    return st[0]


print(sorted(names))
print(sorted(names, key=first_char))
print(sorted(names, key=lambda st: st[0]))
"""
['alex', 'amar', 'anthony', 'eve', 'john', 'mary', 'stella', 'steve']
['alex', 'anthony', 'amar', 'eve', 'john', 'mary', 'steve', 'stella']
['alex', 'anthony', 'amar', 'eve', 'john', 'mary', 'steve', 'stella']
"""

##########################################################################################

d = {'hello': 5, 'everyone': 8, 'good': 4, 'evening': 7}

print(d.items())            # [('hello', 5), ('everyone', 8), ('good', 4), ('evening', 7)]

print(sorted(d.items()))    # [('evening', 7), ('everyone', 8), ('good', 4), ('hello', 5)]

# sort based on keys
print(sorted(d.items(), key=lambda item: item[0]))      # [('evening', 7), ('everyone', 8), ('good', 4), ('hello', 5)]

# sort based on values
print(sorted(d.items(), key=lambda item: item[-1]))     # [('good', 4), ('hello', 5), ('evening', 7), ('everyone', 8)]

# sort based on last character of the key
print(sorted(d.items(), key=lambda item: item[0][-1]))      # [('good', 4), ('everyone', 8), ('evening', 7), ('hello', 5)]

#######################################################################################

d = {'hello': 'everyone', 'happy': 'morning', 'well': 'done', 'good': 'handwriting'}

# sort based on length of key
# sort based on length of value
# sort based on first character of key
# sort based on last character of value

#########################################################################################

prices = {
    'ACME': 45.23,
    'AAPL': 634.87,
    'IBM': 254.8,
    'HPQ': 48.87,
    'FB': 10.75
}


# sort based on prices
print(sorted(prices.items(), key=lambda item: item[1]))     # [('FB', 10.75), ('ACME', 45.23), ('HPQ', 48.87), ('IBM', 254.8), ('AAPL', 634.87)]

# sort based on names
print(sorted(prices.items(), key=lambda item: item[0]))     # [('AAPL', 634.87), ('ACME', 45.23), ('FB', 10.75), ('HPQ', 48.87), ('IBM', 254.8)]

# print the smallest and largest priced share along with share names
smallest, *rest, largest = sorted(prices.items(), key=lambda item: item[-1])
print(smallest)     # ('FB', 10.75)
print(largest)      # ('AAPL', 634.87)

# print the second largest share
*rest, second_largest, largest = sorted(prices.items(), key=lambda item: item[-1])
print(second_largest)       # ('IBM', 254.8)

# print the first 2 least priced shares
# print the first 2 most priced shares

######################################################################################

# get the largest and smallest word in the sentence

st = 'python is a programming language'

words = st.split()

smallest, *rest, largest = sorted(words, key=len)
print(smallest, largest)    # a programming

####################################################################################

# get the largest and smallest non-repeating word in the sentence

st = 'python is a programming language and programming is easy'

non_repeating_words = [word for word in st.split() if st.split().count(word) == 1]
print(non_repeating_words)      # ['python', 'a', 'language', 'and', 'easy']

smallest, *rest, largest = sorted(non_repeating_words, key=len)         #
print(smallest)     # a
print(largest)      # language

