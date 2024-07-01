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

# 5)