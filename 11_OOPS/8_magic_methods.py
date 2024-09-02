# Magic Methods

# 1) Number Protocol
""" add, sub, mul, div, etc"""

# class Point:
#     def __init__(self, a):
#         self.a = a
#
#     def __add__(self, other):
#         return self.a + other.a
#         # return "Hello World"
#         # return self.a * other.a
#
#     def __sub__(self, other):
#         return self.a - other.a


# p1 = Point(4)
# p2 = Point(6)
# print(p1 + p2)      # p1.__add__(p2)
# print(p1 - p2)


class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        # return self.a + self.b + other.a + other.b      # 21
        # return self.a + other.a         # 12
        return self.b + other.b             # 9

    def __sub__(self, other):
        return abs(self.b - other.b)


# p1 = Point(4, 2)
# p2 = Point(8, 7)
#
# print(p1 + p2)
# print(p1 - p2)      # 5

# create a class of your choice and implement all the number protocols

#################################################################################

# 2) Comparison Protocol

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __gt__(self, other):
        # return self.x > other.x and self.y > other.y
        raise TypeError ("Objects of Point can not be compared")



# p1 = Point(3, 8)
# p2 = Point(7, 3)
#
# print(p1 < p2)
# print(p2 > p1)
#
# p3 = Point(10, 20)
# print(p1 < p3)      # p3 > p1   -> True

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.salary = salary
        self.age = age

    def __lt__(self, other):
        return self.salary < other.salary

    def __eq__(self, other):
        return self.age == other.age




# emp1 = Employee("John", 34, 30000)
# emp2 = Employee("Mary", 34, 40000)
#
# print(emp1 < emp2)
# print(emp1 == emp2)

# create a class of your own choice and implement comparison protocol

##################################################################################

# 3) container protocol

# st = 'hello'
# print('e' in st)      # True
# print(st.__contains__('e'))     # True
#
# print(len(st))
# print(st.__len__())
#
# print(st[2])
# print(st.__getitem__(2))
#
# # st[2] = 'L'     # TypeError
#
# li = [1, 2, 3]
# li[1] = 20
# print(li)       # [1, 20, 3]
# li.__setitem__(0, 100)
# print(li)       # [100, 20, 3]
#
# del li[0]
# print(li)       # [20, 3]
#
# li.__delitem__(1)
# print(li)       # [20]

# print(dir(str))
# print(dir(list))

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __len__(self):
#         # return 2
#         return len(self.__dict__)
#
#     def __contains__(self, item):
#         # if self.x == item or self.y == item:
#         #     return True
#         # return False
#         return item in p1.__dict__.values()
#
#     def __getitem__(self, item):
#         if item == 0:
#             return self.x
#         elif item == 1:
#             return self.y
#         else:
#             raise IndexError
#
#     def __setitem__(self, key, value):
#         if key == 0:
#             self.x = value
#         elif key == 1:
#             self.y = value
#         else:
#             raise IndexError
#
#     def __delitem__(self, key):
#         if key == 0:
#             del self.x
#         elif key == 1:
#             del self.y
#         else:
#             raise IndexError
#
#
# p1 = Point(4, 7)
# print(len(p1))
#
# print(7 in p1)
# print(p1.__dict__)
#
# print(p1[0])    #
# # print(p1[3])        # IndexError
#
# p1[0] = 8
# print(p1.__dict__)
#
# del p1[0]
# print(p1.__dict__)
#
# print(len(p1))

# d = {'name': "John", "age": 40, "phone_no": 9191919191}
# print(d['phone_no'])

#################################################################################

class Employee:
    def __init__(self, name, age, phone_no):
        self.name = name
        self.age = age
        self.phone_no = phone_no

    def __getitem__(self, item):
        if item in self.__dict__:
            return self.__dict__[item]
        raise KeyError


# emp1 = Employee("John", 34, 9191919191)
# emp2 = Employee("Mary", 35, 9292929292)
#
# print(emp1['name'])
# print(emp2['phone_no'])

#################################################################################

# 4) Attribute Protocol
"""
__getattribute__
__setattr__
__delattr__
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getattribute__(self, item):
        # return self.item
        return "In get attribute"


# p1 = Point(4, 3)
# print(p1.x)
# print(p1.z)
# print(p1.spam)

###############################################################################

# point class to take only positive values
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __setattr__(self, key, value):
        if value < 0:
            raise ValueError ("Value can not be less than 0")
        super().__setattr__(key, value)


# p1 = Point(-3, 90)      # ValueError: Value can not be less than 0
# p1 = Point(3, 98)
# print(p1.__dict__)

###############################################################################

# make the attributes as immutable

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __setattr__(self, key, value):
        if key not in self.__dict__:
            super().__setattr__(key, value)
        else:
            raise ValueError("Values can not be modified")


# p1 = Point(4, 3)
# p1.z = 5
# print(p1.__dict__)      # {'x': 4, 'y': 3, 'z': 5}

# p1.z = 3        # ValueError: Values can not be modified

##############################################################################

# should not be able to add a new object member or delete a object member

class Point:
    def __init__(self, x, y):
        # self.x = x
        # self.y = y
        """This doesn't work because self.x = x redirects to __setattr__,
        so chain it with __setattr__ of object method"""
        super().__setattr__("x", x)
        super().__setattr__("y", y)

    def __setattr__(self, key, value):
        raise AttributeError ("Values can not be modified or added")

    def __delitem__(self, key):
        raise AttributeError ("Object members can not be deleted")


# p1 = Point(4, 5)
# print(p1.x)
# p1.x = 57           # AttributeError: Values can not be modified or added

###############################################################################

class Point:
    def __init__(self, x):
        self.x = x

    # def __getattribute__(self, item):
    #     return "In get attribute"

    def __getattr__(self, item):
        return "In get attr"


p1 =  Point(4)
print(p1.x)
print(p1.y)
"""
__getattr__ will be called only if attribute is not present or if __getattribute__
is not explicitly mentioned
"""

