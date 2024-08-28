"""
There are 4 main pillars of object-oriented programming
1) Inheritance
2) Polymorphism
3) Abstraction
4) Encapsulation
"""
"""
Inheritance
-> Here, we derive the properties from one class to another class
-> Inheritance is a mechanism for creating a new class that specifies or modifies 
   the behavior of an existing class
-> Class from which we inherit the properties is called parent class/ base class/
   super class
-> Class to which we inherit the properties is called subclass/ derived class/ child
   class/ subtype
-> Child class will inherit the properties from parent class, it may add new 
   attributes or redefine any of the properties
-> There are 5 types
    1) Single Level Inheritance
    2) Multi Level Inheritance
    3) Multiple Inheritance
    4) Hierarchical Inheritance
    5) Hybrid Inheritance
"""

"""
Single Level Inheritance
-> Deriving the properties from one class to another class by considering one
   level is called single level inheritance.
-> Every class is a kind of single level inheritance because it inherits some of
   properties (methods) from object class 
-> Syntax:
            class PC:
                SB
            class CC(PC):
                SB
"""

# class A:
#     pass
#
# print(dir(A))

# class demo:
#     a = 11
#     b = 22
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class child_demo(demo):
#     pass
#
# print(dir(demo))
# print(demo.__dict__)    # 'a': 11, 'b': 22
#
# print(dir(child_demo))  # same as that of demo
# print(child_demo.__dict__)
#
# obj1 = child_demo(3, 4)
# print(obj1.__dict__)    # {'x': 3, 'y': 4}
# print(dir(obj1))        # a, b, x, y
#
# obj2 = demo(30, 40)
# print(obj2.__dict__)    # {'x': 30, 'y': 40}
# print(dir(obj2))        # 'a', 'b', 'x', 'y'

##############################################################################

# child and parent has unique properties

class Demo:
    def __init__(self, value):
        self.value = value

    def apple(self):
        print("Demo.apple", self.value)

    def yahoo(self):
        print("Demo.yahoo", self.value)


class Demo1(Demo):
    def google(self):
        print("Demo1.google", self.value)


# obj1 = Demo(11)
# obj2 = Demo1(22)
#
# print(dir(Demo))        # 'apple', 'yahoo'
# print(Demo.__dict__)    # 'apple', 'yahoo'

# print(dir(Demo1))       # 'apple', 'google', 'yahoo'
# print(Demo1.__dict__)   # 'google'

# print(dir(obj1))        # 'apple', 'value', 'yahoo'
# print(obj1.__dict__)    # {'value': 11}
#
# print(dir(obj2))        # 'apple', 'google', 'value', 'yahoo'
# print(obj2.__dict__)    # {'value': 22}

###############################################################################

# child and parent has same properties

class Demo:
    def __init__(self, value):
        self.value = value

    def apple(self):
        print("Demo.apple", self.value)

    def yahoo(self):
        print("Demo.yahoo", self.value)

class Demo1(Demo):
    def yahoo(self):
        print("Demo1.yahoo", self.value)


# obj1 = Demo(22)
# obj2 = Demo1(33)
#
# print(dir(Demo))
# print(dir(Demo1))
#
# print(Demo.__dict__)        # apple, yahoo
# print(Demo1.__dict__)       # yahoo
#
# obj1.yahoo()        # Demo.yahoo 22
# obj2.yahoo()        # Demo1.yahoo 33

###############################################################################################

"""
-> Suppose you override a parent method in child class but still want to use it
   in child class, we make use of chaining
-> Constructor Chaining
    - Here we invoke the constructor method of parent class by being there in 
      constructor of child class
    - Syntax:
            super().__init__(args)
            parentclassname.__init__(self/obj, args)
            
-> Method Chaining
    - Here, we invoke the method of parent class by being there in method of 
      child class
    - Syntax:
            super().mname(args)
            parentclassname.mname(self/obj, args)
"""

class Demo:
    def __init__(self, value):
        self.value = value

    def apple(self):
        print("Demo.apple", self.value)

    def yahoo(self):
        print("Demo.yahoo", self.value)


class Demo1(Demo):
    def __init__(self, value, extra_value):
        self.extra_value = extra_value
        # super().__init__(value)
        Demo.__init__(self, value)
    def yahoo(self):
        print("Demo1.yahoo", self.extra_value)
        # super().yahoo()
        Demo.yahoo(self)

# obj1 = Demo(10)
# obj2 = Demo1(11, 22)
#
# obj1.yahoo()        # Demo.yahoo 10
# obj2.yahoo()
"""
Demo1.yahoo 22
Demo.yahoo 11
"""

# create a class of your own choice and demonstrate single level inheritance
#################################################################################

# Multi Level Inheritance
"""
-> Here, we inherit the properties from one class to another class by
   considering multiple levels
-> The last derived class will have the properties from all the previous classes
-> Syntax:
            class C1:
                SB
            class C2(C1):
                SB
            .
            .
            class Cn(Cn-1):
                SB
"""

# class A:
#     a = 10
#     b = 20
#     def __init__(self, p, q):
#         self.p = p
#         self.q = q
#
#
# class B(A):
#     m = 30
#     n = 40
#
# class C(B):
#     x = 100
#
#
# print(dir(A))       # 'a', 'b'
# print(dir(B))       # 'a', 'b', 'm', 'n'
# print(dir(C))       # 'a', 'b', 'm', 'n', 'x'
#
# obj1 = C(7, 8)
#
# print(dir(obj1))    # 'a', 'b', 'm', 'n', 'p', 'q', 'x'
#
# print(C.__dict__)   # 'x': 100
# print(obj1.__dict__)    # {'p': 7, 'q': 8}

################################################################################

class A:
    def demo(self):
        print('A')

class B(A):
    def demo(self):
        super().demo()
        print('B')

class C(B):
    def demo(self):
        print('C')
        super().demo()


# obj1 = C()
# obj1.demo()     # C A B

# create a class of your own choice and demonstrate multi level inheritance

###################################################################################

# Multiple Inheritance
"""
-> Here we inherit the properties from multiple parent class to single child class
-> Syntax:
            class PC1:
                SB
            class PC2:
                SB
            .
            .
            class PCn:
                SB
            class CC(PC1, PC2, ......, PCn):
                SB
"""

# class A:
#     a = 10
#     b = 20
#
# class B:
#     p = 30
#     q = 40
#
# class C:
#     a = 50
#     m = 60
#     n = 70
#
# class CC(A, B, C):
#     x = 80
#     y = 90
#
# obj1 = CC()
# print(dir(CC))      # 'a', 'b', 'm', 'n', 'p', 'q', 'x', 'y'
#
# print(obj1.a)       # 10

#######################################################################################

class A:
    def demo(self):
        print('A')

class B:
    def demo(self):
        print('B')

class C:
    def demo(self):
        print('C')

class CC(A, B, C):
    pass

obj1 = CC()
obj1.demo()     # A

####################################################################################

class A:
    def demo(self):
        print('A')

class B:
    def demo(self):
        print('B')

class C:
    def demo(self):
        print('C')

class CC(A, B, C):
    def demo(self):
        print('CC')


obj1 = CC()
obj1.demo()     # CC

##########################################################################################

class A:
    def demo(self):
        print('A')

class B:
    def demo(self):
        print('B')

class C:
    def demo(self):
        print('C')

class CC(A, B, C):
    def demo(self):
        print('CC')
        # super().demo()      # CC A
        B.demo(self)        # CC B

obj1 = CC()
obj1.demo()

# method resolution order -> attribute lookups
print(obj1.__class__.__mro__)       # (<class '__main__.CC'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>)

print(CC.__mro__)       # CC -> A -> B -> C -> object class


################################################################################

"""
Create a class called calculator, to this method inherit the properties from
ADD, SUB, MUL and DIV classes where add, sub, mul, div are static methods 
respectively
"""

#################################################################################

# 4) Hierarchical Inheritance
"""
-> We derive the properties from one parent class to multiple child classes
-> Syntax:
            class PC:
                SB
            class CC1(PC):
                SB
            class CC2(PC):
                SB
            .
            .
            .
            class CCn(PC):
                SB
"""

class A:
    a1 = 10
    a2 = 20

class B(A):
    b1 = 30
    b2 = 40

class C(A):
    c1 = 50
    c2 = 60


print(dir(C))       # 'a1', 'a2', 'c1', 'c2'
print(dir(B))       # 'a1', 'a2', 'b1', 'b2'

print(B.__dict__)   # 'b1': 30, 'b2': 40
print(C.__dict__)   # 'c1': 50, 'c2': 60

##############################################################################

class Parent:
    def spam(self):
        print('Parent.spam')

class Child1(Parent):
    def spam(self):
        super().spam()
        print('Child1.spam')


class Child2(Parent):
    def spam(self):
        print('Child2.spam')
        super().spam()


obj1 = Child1()
obj2 = Child2()

obj1.spam()
"""
Parent.spam
Child1.spam
"""

obj2.spam()
"""
Child2.spam
Parent.spam
"""

##################################################################################

# 5) Hybrid Inheritance
"""It is a combination of more than 1 type of inheritance"""

