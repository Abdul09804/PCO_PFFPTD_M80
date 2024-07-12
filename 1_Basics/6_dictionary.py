# Dictionary
"""
-> It is a collection of key value pairs where key and value is separated by :
   and key value pairs are separated by comma operator
-> Syntax:
            Var = {k1: v1, k2: v2, ..........., kn: vn}
-> key must be immutable, value can be either mutable or immutable datatype.
-> The default value of dictionary is {}
-> To get the value from a dictionary we make use of the syntax,
            Var[key]
-> To modify the value, we make use of the syntax
            Var[key] = value
            if key is present, it will modify the value. If the key is not present
            a new key is added
-> To delete a key value pair we make use of the syntax,
            del Var[key]
            if the key is not present, it throws KeyError
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

d = {'a': 10, 'b': 20, 'a': 40}
print(d)        # {'a': 40, 'b': 20}

# accessing the values of dictionary

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# print(d[1])   # KeyError: 1

print(d['a'])       # 1
print(d['d'])       # 4

temperatures = dict(Bengaluru=38, Chennai=42, Delhi=40, Kashmir=32)
print(temperatures)     # {'Bengaluru': 38, 'Chennai': 42, 'Delhi': 40, 'Kashmir': 32}
print(temperatures['Chennai'])  # 42

print(temperatures['Kashmir'])  # 32

# print(temperatures['Mumbai'])   # KeyError: 'Mumbai'

# modifying the values

temperatures['Chennai'] = 42.6
print(temperatures)     # {'Bengaluru': 38, 'Chennai': 42.6, 'Delhi': 40, 'Kashmir': 32}

temperatures['Mumbai'] = 43
print(temperatures)     # {'Bengaluru': 38, 'Chennai': 42.6, 'Delhi': 40, 'Kashmir': 32, 'Mumbai': 43}

# delete the values

del temperatures['Chennai']
print(temperatures)     # {'Bengaluru': 38, 'Delhi': 40, 'Kashmir': 32, 'Mumbai': 43}

# del temperatures['Patna']       # KeyError: 'Patna'

holidays = {(26, 1): "Republic Day",
            (15, 8): "Independence Day",
            (2, 10): "Gandhi Jayanthi"}

print(holidays[(26, 1)])        # Republic Day

