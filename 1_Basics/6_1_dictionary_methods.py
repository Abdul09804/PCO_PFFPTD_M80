# dictionary methods

# 1) pop
"""
-> pop is used to remove a specified key value pair from the dictionary
-> Syntax:
            Var.pop(key)
-> It will return the value of the key which got removed
-> If the key is not present it will throw KeyError
"""

# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
#
# print(d.pop('b'))       # 2
# print(d)                # {'a': 1, 'c': 3, 'd': 4, 'e': 5}

# print(d.pop('f'))       # KeyError: 'f'

################################################################################

# 2) pop item
"""
-> It is used to remove the last key from the dictionary
-> Syntax:
            Var.popitem()
-> It will return the key value pair which has been deleted
"""
# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# print(d.popitem())      # ('e', 5)

# d = {}
# print(d.popitem())      # KeyError: 'popitem(): dictionary is empty'

##################################################################################

# 3) clear
"""
-> It is used to remove all the key value pairs from the dictionary
-> Syntax:
            Var.clear()
-> The return type of clear is None
"""
# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# print(d.clear())    # None
# print(d)        # {}

##################################################################################

# 4) get
"""
-> It is used to get a value of a specified key from the dictionary
-> Syntax:
            Var.get(key)        # returns the value if key is present, returns None otherwise
            Var.get(key, defaultvalue)  # returns the value of key if it is present, returns default value is the key is not present
-> 
"""

temperatures = {'Bengaluru': 38,
                'Chennai': 42,
                'Delhi': 40,
                'Kashmir': 32
                }

print(temperatures.get("Bengaluru"))    # 38
print(temperatures.get('Chennai', 45))      # 42
print(temperatures.get('Nagpur'))           # None
print(temperatures.get('Nagpur', 39))       # 39
print(temperatures)     # {'Bengaluru': 38, 'Chennai': 42, 'Delhi': 40, 'Kashmir': 32}

###################################################################################

# 5) fromkeys
"""
-> It is used to create a dictionary from the values of iterable
-> Syntax:
            Var.fromkeys(iterable)          # returns dict with keys as values of iterable and value as None
            Var.fromkeys(iterable, val)     # return dict with keys as values of iterable and value as val
"""

print({}.fromkeys('abc'))   # {'a': None, 'b': None, 'c': None}

d = {}.fromkeys([1, 2, 3])
print(d)        # {1: None, 2: None, 3: None}

print({}.fromkeys('abcd', True))

temperature = {'Bengaluru': 38, 'Delhi': 40, 'Kashmir': 32, 'Mumbai': 43}

print(temperature.fromkeys('xyz'))  # {'x': None, 'y': None, 'z': None}
print(temperature)      # {'Bengaluru': 38, 'Delhi': 40, 'Kashmir': 32, 'Mumbai': 43}

############################################################################

# 6) setdefault
"""
-> It is used to add a new key value pair to the dictionary
-> Syntax:
            Var.setdefault(key)         # creates a key with value as None
            Var.setdefault(key, value)  # creates a new key with value as 'value'
-> If the key is already present, it will not alter the key
"""

d = {'a': 1, 'b': 2, 'c': 3}
print(d.setdefault('d'))    # NOne
print(d)        # {'a': 1, 'b': 2, 'c': 3, 'd': None}

d.setdefault('e', 10)
print(d)    # {'a': 1, 'b': 2, 'c': 3, 'd': None, 'e': 10}

d.setdefault('a', 100)
print(d)    # {'a': 1, 'b': 2, 'c': 3, 'd': None, 'e': 10}

##############################################################################

# 7) keys
"""
-> It is used to get all the keys of a dictionary
-> Syntax:
            Var.keys()
"""
temperature = {'Bengaluru': 38, 'Delhi': 40, 'Kashmir': 32, 'Mumbai': 43}
print(temperature.keys())   # dict_keys(['Bengaluru', 'Delhi', 'Kashmir', 'Mumbai'])

d = {'a': 1, 'b': 2, 'c': 3, 'd': None, 'e': 10}
print(d.keys())     # dict_keys(['a', 'b', 'c', 'd', 'e'])

#############################################################################

# 8) values
"""
-> It is used to get the values of the dictionary
-> Syntax:
            Var.values()
"""

print(d.values())           # dict_values([1, 2, 3, None, 10])
print(temperature.values()) # dict_values([38, 40, 32, 43])

###############################################################################

# 9) items
"""
-> It is used to get a collection of tuple with key and value pair
-> Syntax:  
            Var.items()
"""

print(d.items())            # dict_items([('a', 1), ('b', 2), ('c', 3), ('d', None), ('e', 10)])
print(temperature.items())  # dict_items([('Bengaluru', 38), ('Delhi', 40), ('Kashmir', 32), ('Mumbai', 43)])

#################################################################################

