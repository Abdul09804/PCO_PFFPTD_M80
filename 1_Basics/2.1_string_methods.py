# string methods

# 1) upper
"""
-> It is used to convert the lowercase characters to uppercase characters
-> Syntax:
        Var.upper()
-> The return type of upper is a string
-> string methods will not modify the original strings
"""

st = 'hello'
print(st.upper())   # HELLO
print(st)       # hello

print('heLlo WOrld 123@'.upper())   # HELLO WORLD 123@

#################################################################################

# 2) lower
"""
-> It is used to convert uppercase characters to lowercase charcaters
-> Syntax:
        Var.lower()
-> The return type of lower is a string
"""

st = 'Hello WORLd 12%^^'
print(st.lower())   # hello world 12%^^

##################################################################################

# 3) swapcase
"""
-> It is used to convert uppercase to lowercase and vice versa
-> Syntax:
        Var.swapcase()
-> The return type of swapcase is string
"""
st = 'Hello WORLd 12%^^'
print(st.swapcase())    # hELLO worlD 12%^^

##################################################################################

# 4) title
"""
-> It is used to convert the given string to title format
-> Syntax:
        Var.title()
-> The return type of title is a string
"""

book = "the stories of mahabharata"
print(book.title())     # The Stories Of Mahabharata

book = "4small sToRies"
print(book.title())     # 4Small Stories

print("THE STORIES".title())    # The Stories

################################################################################

# 5) capitalize
"""
-> It is used to convert the first alphabet to uppercase and rest 
   of them to lowercase
-> Syntax:
        Var.capitalize()
-> The return type of capitalize is string
"""
book = "the stories of mahabharata"
print(book.capitalize())    # The stories of mahabharata

book = '4tune teller'
print(book.capitalize())    # 4tune teller

################################################################################

# 6) isupper
"""
-> It is used to check whether all the alphabets present are uppercase alphabets
-> Syntax:
        Var.isupper()
-> The return type of isupper is boolean
"""

st = 'HELLO'
print(st.isupper())     # True

print('HELLo'.isupper())    # False

print('HELLO WORLD123@764'.isupper())  # True

###############################################################################

# 7) islower

############################################################################

# 8) isalpha
"""
-> It is used to check whether string has only alphabets
-> Syntax:
        Var.isalpha()
-> The return type of isalpha is boolean
"""

print('helLO'.isalpha())        # True

print('hai ram'.isalpha())      # False

print('PYTHON'.isalpha())       # True

print('python'.isalpha())       # True

##############################################################################

# 9) isdigit()
"""
-> It is used to check whether string consists of only numbers
-> Syntax:
        Var.isdigit()
-> The return type of isdigit is boolean
"""

print('9845 123 536'.isdigit())     # False
print('9876543210'.isdigit())       # True

#############################################################################

# 10) isalnum
"""

"""

st = 'HelloWorld123'
print(st.isalnum())  # True

print('Hello World123'.isalnum())       # False
print('hello'.isalnum())        # True
print('HELLO'.isalnum())        # True
print('1234'.isalnum())         # True

############################################################################

# 11) istitle
"""
-> IT is used to check whether the string is in title format
-> Syntax:
        Var.istitle()
-> The return type of istitle is boolean
"""

st = 'The Stories Of Mahabharata'
print(st.istitle())     # True

############################################################################

# 12) startswith
"""
-> It is used to check whether a string is starting with a specified substring
-> Syntax:
        Var.startswith(substring)
-> The return type of startswith is boolean
"""

st = 'hello world'
print(st.startswith('h'))   # True
print(st.startswith('he'))  # True
print(st.startswith('H'))   # False

###############################################################################

# 13) endswith

##############################################################################

# 14) count
"""
-> It is used to count the number of occurrence of a given substring
   in a string within specified limits
-> Syntax:
        Var.count(substring)
        Var.count(substring, start)
        Var.count(substring, start, end)
-> The return type of count is integer
-> If the substring is not present, count will return 0
"""

st = 'mississippi'
print(st.count('s'))    # 4
print(st.count('s', 4))     # 2
print(st.count('s', 3, 6))  # 2

print(st.count('ssi'))      # 2

print(st.count('z'))    # 0

#############################################################################

# 15) index
"""
-> It is used to get the index number of first ocurrence of first character of a
   a given substring.
-> Syntax:
        Var.index(substring) 
        Var.index(substring, SI)
        Var.index(substring, SI, EI)
-> The return type of index is a integer
-> If the value is not present between the limits  control will throw 
   ValueError
"""

st = 'mississippi'
print(st.index('i'))    # 1

print(st.index('s', 4))     # 5
print(st.index('i', 5, 10))     # 7

# print(st.index('l'))    # ValueError

print(st.index('ssi'))      # 2

