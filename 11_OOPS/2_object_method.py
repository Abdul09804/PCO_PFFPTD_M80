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


# p1 = Point(10, 20)
# p2 = Point(30, 40)

# p1.add_value(2)
# Point.add_value(p2, 0.5)

# p1.move(2, 3)
# p2.move(1.45, 0.34)

# p1.swap()
# Point.swap(p2)

# Point.reset(p1)
# p2.reset(4)
#
# print(p1.__dict__)
# print(p2.__dict__)

###############################################################################

class Calculator:
    def add(self, a, b):
        if type(a) == int and type(b)== int:
            return a + b
        raise Exception ("Only integers can be added")

    def sub(self, a, b):
        if type(a) == int and type(b) == int:
            return a - b
        raise Exception

    def mul(self, a, b):
        return a * b

# c1 = Calculator()
# # print(c1.add(9, 7))
# print(c1.mul('hai', 2))
# # print(c1.mul('hai', 'hai'))     # TypeError

##############################################################################

class Library:
    books = []
    def __init__(self, title, category, author):
        self.title = title
        self.category = category
        self.author = author
        Library.books.append(self)

    def display(self):
        print('*' * 50)
        print(f"Title : {self.title}")
        print(f"Category : {self.category}")
        print(f"Author : {self.author}")
        print('*' * 50)


b1 = Library("Wings Of Fire", "Autobiography", "Abdul Kalam")
b2 = Library("One Indian Girl", "Novel", "Chetan Bhagat")
b3 = Library("A Suitable Boy", "Novel", "Vikram Seth")
b4 = Library("Ghosts of the Silent Hills", "Horror", "Anita Krishan")
b5 = Library("The Girl in Room 105", "Love Story", "Chetan Bhagat")

books = Library.books
for book in books:
    print(book.title)


# print the title of all novels
for book in books:
    if book.category == "Novel":
        print(book.title)

# print the details of all the books
for book in books:
    book.display()

# print the details of Chetan Bhagat's books
for book in books:
    if book.author == "Chetan Bhagat":
        book.display()

# create a class of your choice with 3 class members, 3 object members and 3 object methods
