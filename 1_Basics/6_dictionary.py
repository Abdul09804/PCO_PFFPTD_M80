# Dictionary
"""
-> It is a collection of key value pairs where key and value is separated by :
   and key value pairs are separated by comma operator
-> Syntax:
            Var = {k1: v1, k2: v2, ..........., kn: vn}
-> key must be immutable, value can be either mutable or immutable datatype.
-> The default value of dictionary is {}
->
"""

d1 = {1: 'one', (6, 5): 1, 'year': 2020}
print(d1)   # {1: 'one', (6, 5): 1, 'year': 2020}
print(d1[1])        # one

d2 = {'a': 1, 'b': 2, 'c': 3}
print(d2)

# creating a dictionary with string keys
prices = dict(apple=123, mango=78, orange=65, grapes=200)
print(prices)       # {'apple': 123, 'mango': 78, 'orange': 65, 'grapes': 200}

# d3 = {1: 'one', [1, 2]: 'nums'}     # can not store mutable datatypes as keys

d4 = {'one': [1, 2, 3]}
print(d4)       # {'one': [1, 2, 3]}

# Memory Allocation of Dictionary
"""
-> When the value is of dictionary a key and value layer will be created in value
   space/ heap memory, the address of each value will be stored in value layer wrt
   corresponding key which will be stored in key layer
-> Once after storing all the key and values address will be given to key layer
   which gets stored wrt variable name in variable space
-> For control the visible layer is key layer
-> python_visualizer_path = https://pythontutor.com/render.html#mode=edit
"""


