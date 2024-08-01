# break
"""
-> break is a keyword which is used to terminate from the loop in between the execution
-> we can break both for and while loop
"""

for i in range(1, 11):
    print(i)
    if i == 5:
        break
"""
1
2
3
4
5
"""

# 1) WAP to print the index of first occurrence of a given character in a string
st = 'mississippi'
ch = 's'
# o/p = 2
for i in range(len(st)):
    if st[i] == ch:
        print(i)
        break

# 2) WAP to print the index of second occurrence of a given character in a string
st = 'mississippi'
ch = 's'
# o/p = 3
count = 0
for i in range(len(st)):
    if st[i] == ch:
        count += 1
        if count == 2:
            print(i)
            break
