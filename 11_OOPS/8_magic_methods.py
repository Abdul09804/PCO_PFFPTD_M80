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

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        # return 2
        return len(self.__dict__)

    def __contains__(self, item):
        # if self.x == item or self.y == item:
        #     return True
        # return False
        return item in p1.__dict__.values()

    def __getitem__(self, item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        else:
            raise IndexError

    def __setitem__(self, key, value):
        if key == 0:
            self.x = value
        elif key == 1:
            self.y = value
        else:
            raise IndexError

    def __delitem__(self, key):
        if key == 0:
            del self.x
        elif key == 1:
            del self.y
        else:
            raise IndexError


p1 = Point(4, 7)
print(len(p1))

print(7 in p1)
print(p1.__dict__)

print(p1[0])    #
# print(p1[3])        # IndexError

p1[0] = 8
print(p1.__dict__)

del p1[0]
print(p1.__dict__)

print(len(p1))