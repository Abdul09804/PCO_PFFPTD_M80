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
-> It is used to get the index number of first ocurrence of the character of a
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

###############################################################################

# 16) rindex
"""
-> It is used to get the index of first occurrence of given character searching
   from right to left of the string.
-> Syntax:
        Var.rindex(substring)
        Var.rindex(substring, SI)
        Var.rindex(substring, SI, EI)
-> The return type of rindex is integer
"""
st = 'mississippi'
print(st.rindex('i'))   # 10
print(st.rindex('s'))   # 6
print(st.index('s'))    # 2

print(st.rindex('i', 4, 10))        # 7
print(st.index('i', 4, 10))         # 4

print(st.rindex('i', 1, 9))     # 7

st = 'python program'
"""
-14	-13	-12	-11	-10	-9	-8	-7	-6	-5	-4	-3	-2	-1
p	y	t	h	o	n 		p	r	o	g	r	a	m
0	1	2	3	4	5	6	7	8	9	10	11	12	13
"""
print(st.rindex('o'))       # 9
print(st.index('o'))      # 4

print(st.rindex('p'))       # 7
print(st.index('p'))        # 0

print(st.rindex('p', 0, 8))     #
# print(st.index('p', 0, 8))

# 17) find
"""
-> It works same as index if the value is present.
-> If the value is not present, control will throw ValueError in case index method
   but, it will give the result as -1 if the value is not present.
-> Syntax:
        Var.find(substring) 
        Var.find(substring, SI)
        Var.find(substring, SI, EI)
-> The return type of find s a integer
-> If the value is not present between the limits -1 is returned
"""

# st = 'hello universe'
# print(st.find('e'))     # 1
#
# print(st.index('e'))    # 1
#
# # print(st.index('z'))    # ValueError: substring not found
#
# print(st.find('z'))     # -1 -> It gives -1 if the value is not present

################################################################################

# 18) rfind
"""
-> 
"""

#################################################################################

# 19) replace
"""
-> It is used to replace a substring by a new string
-> Syntax:
            Var.replace(oldstring, newstring)
            Var.replace(oldstring, newstring, no_of_replacements)
-> The return type of replace is a string 
"""

st = "she sells seashells in the seashore"

print(st.replace('s', 'S'))     # She SellS SeaShellS in the SeaShore

print(st.replace('sea', 'Sea'))     # she sells Seashells in the Seashore

print(st.replace('s', 'S', 2))  # She Sells seashells in the seashore

print(st.replace(' ', '_'))     # she_sells_seashells_in_the_seashore

print(st.replace('w', 'W'))     # she sells seashells in the seashore


################################################################################

# 20) strip
"""
-> It is used to remove leading and trailing whitespaces, \n and \t characters
-> Syntax:
            Var.strip()
            Var.strip(ch)       # strips leading and trailing ch
-> The return type of strip is a string
"""

st = '              hello world             '
print(len(st))      # 38

print(st)           # '              hello world             '

print(st.strip())   # hello world
print(len(st.strip()))      # 11

st = '@@@@@@@@@@@@@@hello world@@@@@@@@@@@@@@@@@@@@'
print(st.strip())       # '@@@@@@@@@@@@@@hello world@@@@@@@@@@@@@@@@@@@@'

print(st.strip('@'))        # hello world

st = '@@@@@@@@@@@@@         hello world        $$$$$$$$$$$$$$$$$'

print(st.strip())       # @@@@@@@@@@@@@         hello world        $$$$$$$$$$$$$$$$$

print(st.strip('@'))        # '         hello world        $$$$$$$$$$$$$$$$$'

print('    hello      '.strip())        # hello

print(st.strip('@').strip('$'))     # '         hello world        '

print(st.strip('@').strip('$').strip())     # 'hello world'

###############################################################################

# 21) lstrip
"""
-> It is used to remove the leading whitespaces or \n or \t characters
-> Syntax:
            Var.lstrip()    
            Var.lstrip(ch)
-> The return type of lstrip is a string
"""

st = '              hello world             '
print(st.lstrip())      # 'hello world             '

st = '@@@@@@@@@@@@@@hello world@@@@@@@@@@@@@@@@@@@@'
print(st.lstrip('@'))       # 'hello world@@@@@@@@@@@@@@@@@@@@'

##############################################################################

# 22) rstrip

##############################################################################

# 23) split
"""
-> It is used to split the string as list of strings
-> Syntax:
            Var.split()
-> The return type of split is list
"""

st = 'the stories of world war 2'
print(st.split())       # ['the', 'stories', 'of', 'world', 'war', '2']

print(st.split('e'))    # ['th', ' stori', 's of world war 2']

print(st.split(maxsplit=2))     # ['the', 'stories', 'of world war 2']

st = 'the_stories_of_world_war_2'
print(st.split('_'))        # ['the', 'stories', 'of', 'world', 'war', '2']

print(st.split('_', maxsplit=3))    # ['the', 'stories', 'of', 'world_war_2']

print(st.split('_', 3))     # ['the', 'stories', 'of', 'world_war_2']

#############################################################################

# 24) rsplit
"""

"""
st = 'the stories of world war 2'

print(st.split())   # ['the', 'stories', 'of', 'world', 'war', '2']
print(st.rsplit())  # ['the', 'stories', 'of', 'world', 'war', '2']

print(st.split(maxsplit=2))     # ['the', 'stories', 'of world war 2']
print(st.rsplit(maxsplit=2))    # ['the stories of world', 'war', '2']

################################################################################

# 25) join
"""
-> It is used to join an iterable by a gluestring
-> Syntax:
            gluestring.join(iterable)
-> The return type of join is a string
"""

print(' '.join(['the', 'stories', 'of', 'world', 'war', '2']))  # the stories of world war 2

print(''.join(['the', 'stories', 'of', 'world', 'war', '2']))       # thestoriesofworldwar2

print('@$#'.join(['the', 'stories', 'of', 'world', 'war', '2']))        # the@$#stories@$#of@$#world@$#war@$#2

print(' '.join('abc'))  # a b c

# print(' '.join([1, 2, 3]))  # TypeError




