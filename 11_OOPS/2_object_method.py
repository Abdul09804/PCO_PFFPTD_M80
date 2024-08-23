# object method
"""
-> Methods which are used to access and modify the members of the object is called
   object members
-> for all the object members passing self is mandatory to store the address of
   the object
-> To call the object members we make use of the syntax:
        obj_name.mname(args)
        cls_name.mname(obj/self, args)
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    """add value to both x and y """
    def add_value(self, value):
        self.x += value
        self.y += value

    """ add different values to x and y """
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    """ swap the values of x and y"""
    def swap(self):
        self.x, self.y = self.y, self.x

    """reset the values"""
    def reset(self, val=0):
        self.x = val
        self.y = val


p1 = Point(10, 20)
p2 = Point(30, 40)

# p1.add_value(2)
# Point.add_value(p2, 0.5)

# p1.move(2, 3)
# p2.move(1.45, 0.34)

# p1.swap()
# Point.swap(p2)

Point.reset(p1)
p2.reset(4)

print(p1.__dict__)
print(p2.__dict__)

