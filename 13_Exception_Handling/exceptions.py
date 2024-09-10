# exception handling

a = 10
b = '20'
# print(a + b)    # TypeError

l = [1, 2, 3]
# l.extend(5)     # TypeError
# l.extend('hai')

# l.add(45)       # AttributeError

# l.remove(8)     # ValueError
# l.remove(2)

s = {1, 2}
s.add(3)
# s.add([5, 7])       # TypeError

# if 5:
#             # IndentationError

# if 5        # SyntaxError

# a, b, c, d = 1, 2, 3, 4, 5      # ValueError

t = (1, 2)
# t.append(7)     # AttributeError

# t[0] = (1, 2)       # TypeError

# print(5/0)      # ZeroDivisionError

# with open('sample.txt') as file:        # FileNotFoundError
#     pass

# with open('sample1.txt', 'x') as file:      # FileExistsError
#     pass

