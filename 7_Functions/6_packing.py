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

