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

# accessing the values

print(Point.x)      # 10
print(Point.y)      # 20
print(p1.x)         # 10
print(p2.y)         # 20

# modifying the values wrt class
""" 
modification wrt class will change the class as well as object created for
the class
"""
Point.x = 100
print(Point.x)      # 100
print(p1.x)         # 100
print(p2.x)         # 100

# modifying the values wrt object
"""
modification wrt object will change only that particular object but not other objects
or the class
"""
print(p1.__dict__)      # {}
p1.x = 11
print(p1.__dict__)      # {'x': 11}
print(p1.x)     # 11
print(p2.x)     # 100
print(Point.x)  # 100

###################################################################################

"""
Generic Members or Class Members
-> These are the members which are common for each and every object created for
   the class.
-> These members are created inside the class
-> Class Variables

Specific Members or Object Members
-> These members will be different for different objects
"""

class Company:
    Comp_name = "ABC"
    Comp_loc = "Bengaluru"
    Comp_CEO = "Mr.Ram"


emp1 = Company()
emp2 = Company()

print(Company)      # <class '__main__.Company'>
print(emp1)         # <__main__.Company object at 0x000001BF5CB246D0>
print(emp2)         # <__main__.Company object at 0x000001BF5CB24710>

print(dir(Company))
print(dir(emp1))
print(dir(emp2))

print(Company.__dict__)     # 'Comp_name': 'ABC', 'Comp_loc': 'Bengaluru', 'Comp_CEO': 'Mr.Ram'
print(emp1.__dict__)        # {}
print(emp2.__dict__)        # {}

emp1.name = "John"
emp1.emp_id = "ABC123"
emp1.salary = 60000

emp2.name = "Mary"
emp2.emp_id = "ABC124"
emp2.salary = 80000

print(dir(Company))     # 'Comp_CEO', 'Comp_loc', 'Comp_name'
print(dir(emp1))        # 'Comp_CEO', 'Comp_loc', 'Comp_name', 'emp_id', 'name', 'salary'
print(dir(emp2))        # 'Comp_CEO', 'Comp_loc', 'Comp_name', 'emp_id', 'name', 'salary'

print(Company.__dict__)     # 'Comp_name': 'ABC', 'Comp_loc': 'Bengaluru', 'Comp_CEO': 'Mr.Ram'
print(emp1.__dict__)        # {'name': 'John', 'emp_id': 'ABC123', 'salary': 60000}
print(emp2.__dict__)        # {'name': 'Mary', 'emp_id': 'ABC124', 'salary': 80000}


# create a class of your own choice with 3 class members and 3 object members

class School:
    school_name = "Indus Valley"
    school_principal = "Mr.Ram"
    school_location = "Rajajinagar"

st1 = School()
st2 = School()

st1.name = "Milana"
st1.marks = 98
st1.phno = 9191919191

st2.name = "Akash"
st2.marks = 97
st2.phno = 9292929292


###################################################################################

# Constructor Method or Initialisation Method
"""
-> __init__
-> we use constructor to initialise the members of the object 
-> we can reduce the number of instructions 
-> control will invoke this method by default during object creation, we need 
   not have to call it separately
-> self will store the address of the object
"""

li = [10, 20, 30]
li.append(87)
print(li)
list.append(li, 90)
print(li)   # [10, 20, 30, 87, 90]

class Company:
    Comp_name = "ABC"
    Comp_loc = "Bengaluru"
    Comp_CEO = "Mr.Ram"

    def __init__(self, emp_name, emp_id, emp_sal):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_sal = emp_sal

emp1 = Company("Mary", "ABC123", 30000)
emp2 = Company("John", "ABC234", 25000)

print(dir(Company))
print(dir(emp1))
print(dir(emp2))

print(Company.__dict__)
print(emp1.__dict__)
print(emp2.__dict__)