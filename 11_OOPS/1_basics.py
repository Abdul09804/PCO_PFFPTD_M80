# store the data 10 and 20
# a = 10  # instance of integer
# b = 20  # instance of integer
#
# nums = [10, 20]
# t = (10, 20)
# s = {10, 20}
# d = {'a': 10, 'b': 20}
"""
-> advantage of storing the values in the form of dictionary is that, we can access
   them using keys and also can store the values in a organised manner
"""

# access the values from nums
# print(nums[0], nums[1])

# access the values from t
# print(t[0], t[1])

# access the values from s
# print(s[0])     # TypeError:

###################################################################################

# modify the values
# nums[0] = 100
# print(nums)     # [100, 20]

# t[0] = 100      # TypeError

# add the values
# nums.append(98)
# print(nums)     # [100, 20, 98]

# t.append(97)    # AttributeError

# s.append(9)     # AttributeError
#
# s.add(9)
# print(s)

# concatenation
#
# print([1, 2] + [3, 4])
# print((1, 2) + ('a', 'b'))
# # print({1, 2} + {'a'})       # TypeError

################################################################################

# print(dir(list))
# print(dir(nums))
# print(dir(tuple))
# print(dir(set))
# print(dir(int))

####################################################################################

nums = [10, 20]
# nums.swap()     # AttributeError

# nums.reset()        # AttributeError

# nums.append(30)
# # list.append(30)     # TypeError\
# list.append(nums, 30)   #
# print(nums)     # [10, 20, 30, 30]
"""all the functionalities of a class can be applied only to objects"""

####################################################################################

"""
Class
-> Class is a container which has all functionalities that can be performed on an
   object created for the class
-> Class is a blueprint which has properties and functionalities of a real time entity
-> Class is a collection of functions which carry out the various operations on 
   instances
   
Object
-> Instance of class (memory reference)
-> It is a variable created for a particular class
"""

##################################################################################

# User Defined Class
"""
-> Syntax:
        class cname:
            SB
        obj = cname(args)
-> We can create 'n' number of objects for a single class
"""

# d = dict(a=1, b=2, c=3)
# print(d)    # {'a': 1, 'b': 2, 'c': 3}
#
# li = list((10, 20, 30))
# print(li)   # [10, 20, 30]

# User Defined  class

class Point:
    """class variables"""
    x = 10
    y = 20

print(Point)        # <class '__main__.Point'>
print(Point())      # <__main__.Point object at 0x00000141F7424150>

p1 = Point()
p2 = Point()
print(p1)       # <__main__.Point object at 0x0000020EADDE41D0>
print(p2)       # <__main__.Point object at 0x000001AF66A94210>

print(dir(Point))   # few methods will be derived by default from object dictionary
print(Point.__dict__)   # 'x': 10, 'y': 20

print(dir(p1))
print(p1.__dict__)      # {}

print(dir(p2))
print(p2.__dict__)      # {}

