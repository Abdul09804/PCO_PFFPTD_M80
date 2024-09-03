# Abstraction
"""
-> abstract class acts as design specification
-> ABC - Abstract Base Class
-> abstract method - method which has declaration but not definition
-> abstract class - class which has atleast 1 abstract method
-> to create an abstract class we have to inherit ABC
-> to create an abstract method we have to make use of the decorator abstractmethod
-> we can not create an object for abstract class
-> until all the methods are over-rided we will not be able to create an object for the class
"""

from abc import ABC, abstractmethod

class Calc(ABC):
    @abstractmethod
    def add(self, a, b):
        pass

    @abstractmethod
    def sub(self, a, b):
        pass

    @abstractmethod
    def mul(self, a, b):
        pass

    @abstractmethod
    def div(self, a, b):
        pass


class Calculator(Calc):
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def div(self, a, b):
        return a / b

    def mul(self, a, b):
        return a * b


obj1 = Calculator()
print(obj1.add(3, 7))


################################################################################################

class BankAccount(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def roi(self):
        pass

    @abstractmethod
    def transfer(self):
        pass


