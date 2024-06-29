# String
"""
-> It is a collection of characters enclosed between single quotes, double quotes
   or 3 pairs of single quotes
-> The characters can be alphabets(UC and LC), numbers or special characters
-> Syntax:
        Var = 'Val1Val2......Valn'
        Var = "Val1Val2......Valn"
        Var = '''Val1Val2......Valn'''
-> Even though we make use of double or 3 pairs of quotes, internally it will be
   considered as single quotes only
-> The default value of string is ''
"""

st1 = 'hello'
st2 = "hello"
st3 = '''hello'''
st4 = """hello"""
print(st1)      # 'hello'
print(st2)      # 'hello'
print(st3)      # 'hello'
print(st4)      # 'hello'

st = ''
print(bool(st))     # False


# greeting = 'welcome to today's class'   # SyntaxError

"""escape character is used to make ' as a part of the string and not end of string"""

greeting = 'welcome to today\'s class'
print(greeting)     # welcome to today's class

"""
We make use of double quoted string when we have to use single quote inside it
"""

greeting = "Welcome to python's World"
print(greeting)     # Welcome to python's World

path = "C:\testing\newfolder\sample.py"
print(path)
"""
C:	esting
ewfolder\sample.py
"""

""" we make use of escape character to remove the special meaning"""

path = "C:\\testing\\newfolder\sample.py"
print(path)     # C:\testing\newfolder\sample.py

"""
we make use of raw string ('r' or 'R') to remove the special meaning like \t or \n character
"""
path = r"C:\testing\newfolder\sample.py"
print(path)     # C:\testing\newfolder\sample.py

st = ('hello everyone'
      'good morning'
      'how was your day')

print(st)   # hello everyonegood morninghow was your day

"""
-> To create a multi-line string we make use of triple quoted string
-> also we use it for documentation purpose
-> 3 pairs of quotes is also known as doc string
"""
st = """hello everyone
good morning
have a good day"""

print(st)
"""
hello everyone
good morning
have a good day
"""



