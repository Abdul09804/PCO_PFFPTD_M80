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


p1 = Point(4, 2)
p2 = Point(8, 7)

print(p1 + p2)
print(p1 - p2)      # 5

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




emp1 = Employee("John", 34, 30000)
emp2 = Employee("Mary", 34, 40000)

print(emp1 < emp2)
print(emp1 == emp2)

# create a class of your own choice and implement comparison protocol




