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

