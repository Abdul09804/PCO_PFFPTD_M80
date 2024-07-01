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

###############################################################################

# Memory Allocation of Sequential Datatype
"""
-> When the value is of sequential datatype, a layer of memory will be created
   which gets divided into number of blocks which is equal to length of the 
   collection.
-> Each value in the collection will be stored in individual blocks
-> Once after storing all the values an address will be given which gets stored
   wrt variable name in variable space
"""

# Indexing
"""
-> The process of accessing individual values from the collection is called
   indexing.
-> Positive Indexing - Here the subaddress is given from left to right of 
                       the collection.
                     - Positive indexing ranges from 0 to len(coll)-1
-> Negative Indexing - Here the sub address is given from right to left of 
                       the collection.
                     - Negative indexing ranges from -1 to -len(coll)
-> Even if we use negative indexing to fetch the values, internally it will
   consider it as positive indexing and get the value
-> To get individual values from the collection, we make use of the syntax,
            Var[index_no]
-> To modify the values, we make use of the syntax,
            Var[index_no] = new_value
"""

st = 'Hai Steve'
"""
-9	-8	-7	-6	-5	-4	-3	-2	-1
 H	 a	 i		 S	 t	 e	 v	 e
 0	 1	 2 	 3	 4	 5	 6	 7	 8

"""
print(len(st))

print(st[5])      # t
print(st[-3])     # e

# string modification

# st[4] = 's'
"""
-> We will not be able to modify the values of a string as it is a immutable 
   collection
-> A collection which does not allow the user to modify its values is called 
   immutable collection
"""

st = 'mississippi'
"""
-11	-10	-9	-8	-7	-6	-5	-4	-3	-2	-1
m	i	s	s	i	s	s	i	p	p	i
0	1	2	3	4	5	6	7	8	9	10
"""
st1 = 'pepsi'

print(st[2])

print(id(st[2]))        # 140722741549808

print(id(st1[-2]))      # 140722741549808

