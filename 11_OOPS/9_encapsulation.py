# public members/ public attributes
"""
-> These are the members which can be accessed both inside and outside the class
   as well as in child class
"""

class Demo:
    value = 10

    def __init__(self, name):
        self.name = name

    def display(self):
        return self.name, self.value


d1 = Demo("Steve")
print(d1.name)
print(d1.value)
print(d1.display())
"""
Steve
10
('Steve', 10)
"""

class Demo1(Demo):
    pass

d2 = Demo1("john")
print(d2.name)
print(d2.value)
print(d2.display())
"""
john
10
('john', 10)
"""

####################################################################################

# protected members / protected attributes
"""
-> These are the members that should be accessed inside the class or in the child class
   but not outside the class
-> But we can access them outside the class 
"""

class Demo:
    _value = 10
    def __init__(self, name):
        self._name = name

    def _display(self):
        return self._name, self._value


d1 = Demo("John")
# print(d1.name)
print(d1.__dict__)      # {'_name': 'John'}
print(d1._name)
print(d1._value)
print(d1._display())
"""
John
10
('John', 10)
"""


#######################################################################################

# private members/ private attributes
"""
-> These are the members that can not be accessed outside the class or in the child class
-> But we can access them outside the class
"""

class Demo:
    _value = 10

    def __init__(self, name):
        self.__name = name

    def display(self):
        return self.__name, self._value


d1 = Demo("Mary")
# print(d1.name)      # AttributeError
# print(d1.__name)        # AttributeError
print(d1.__dict__)      # {'_Demo__name': 'Mary'}
print(d1._Demo__name)   # Mary
print(d1.display())     # ('Mary', 10)


class Demo1(Demo):
    def spam(self):
        # print(self.__name)
        print(self._Demo__name)

d1 = Demo1("Steve")
d1.spam()        # Steve


