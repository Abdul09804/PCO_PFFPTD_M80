# packing

# variable positional arguments

def add_num(*args):
    print(args)         # pack the values in the form of tuple
    print(type(args))
    print(*args)        # 1 2 3 4 5 6 7 8 9 0
    s = 0
    for i in args:
        s += i
    print(s)


add_num(1, 2)
add_num(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
add_num()
# add_num(a=1, b=2)   # TypeError: add_num() got an unexpected keyword argument 'a'

# combination

def sam(name, *args):
    print(name)
    print(args)

sam(1, 2, 3, 4, 5)
"""
1
(2, 3, 4, 5)
"""

sam("John", 8, 8, 23)
"""
John
(8, 8, 23)
"""

##########################################################################################

# variable keyword arguments

def sam(**kwargs):
    print(kwargs)
    print(type(kwargs))
    print(*kwargs)
    print(*kwargs.values())
    print(*kwargs.items())

# sam(1, 2, 3)        # TypeError: sam() takes 0 positional arguments but 3 were given
sam(a=1, b=2, c=3, d=4)
"""
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
<class 'dict'>
a b c d
1 2 3 4
('a', 1) ('b', 2) ('c', 3) ('d', 4)
"""

# combination

def sam(name, **kwargs):
    print(name, kwargs, sep='\n')


sam("John", last_name="Patrick")
"""
John
{'last_name': 'Patrick'}
"""

sam(name="John", last_name="Patrick", marks={'physics': 95, 'chemistry': 93, 'maths': 99, 'biology': 90})
"""
John
{'last_name': 'Patrick', 'marks': {'physics': 95, 'chemistry': 93, 'maths': 99, 'biology': 90}}
"""

############################################################################################

# variable positional and variable keyword

def sam(*args, **kwargs):
    print(args, kwargs)


sam()       # () {}
sam(1, 2, 3)        # (1, 2, 3) {}
sam(a=10, b=20, c=30)       # () {'a': 10, 'b': 20, 'c': 30}
sam(1, 2, 3, a=10, b=20, c=30)  # (1, 2, 3) {'a': 10, 'b': 20, 'c': 30}
# sam(a=10, b=20, c=30, 'hai', 'hello')   # SyntaxError: positional argument follows keyword argument

###########################################################################################

# only positional arguments
""" 
arguments before / must be positional arguments , arguments after / can be either 
positional or keyword
"""

def sum_of_num(a, b, /, c):
    print(a + b + c)

sum_of_num(1, 2, 3)
sum_of_num(1, 2, c=3)
# sum_of_num(a=1, b=2, c=3)       # TypeError: sum_of_num() got some positional-only arguments passed as keyword arguments: 'a, b'

########################################################################################

# only keyword arguments
"""
arguments after * must be keyword only arguments, arguments before * can be either positional
or keyword
"""

def sum_of_nums(a, *, b, c):
    print(a + b + c)


sum_of_nums(a=11, b=22, c=33)
sum_of_nums(11, b=22, c=33)
# sum_of_nums(11, 22, 33)     # TypeError: sum_of_nums() takes 1 positional argument but 3 were given

########################################################################################

# combination
"""
a, b -> only positional
c, d -> can be either positional or keyword
e, f -> must be keyword arguments only
"""

def sum_of_nums(a, b, /, c, d, *, e, f):
    print(a + b + c + d + e + f)


# sum_of_nums(1, 2, 3, 4, 5, 6)       # TypeError
sum_of_nums(1, 2, 3, 4, e=5, f=6)
sum_of_nums(1, 2, c=3, d=4, e=5, f=6)
sum_of_nums(1, 2, 3, d=4, e=5, f=6)

#######################################################################################


def sum_of_nums(a, b, /, c, d=0, *, e=0, f=0):
    print(a + b + c + d + e + f)


sum_of_nums(1, 2, 3)
sum_of_nums(1, 2, 3, 4, e=5, f=6)
sum_of_nums(1, 2, c=4, e=5, f=6)
sum_of_nums(1, 2, c=0, d=23, e=86, f=79)

#######################################################################################

