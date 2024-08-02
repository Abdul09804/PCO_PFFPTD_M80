# continue
"""
-> 'continue' is used to make the control skip the current iteration and go for the next iteration
"""

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

# 1) WAP to extract all the string data items in a given list
li = [3, 'hai', 8.87, '7657', 'data', 'python']
res = []
for i in li:
    if type(i) != str:
        continue
    res.append(i)
print(res)


# pass
"""
-> It is a keyword which is used to validate an empty statement block
"""

if 4 > 3:
    pass

for i in range(1, 11):
    pass



