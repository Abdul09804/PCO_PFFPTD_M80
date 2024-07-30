# range
"""
-> This is used to generate the numbers between specified limits
-> Syntax:
            range(SV, EV+-1, SV)
-> By default the value of updation is equal to 1
            range(SV, EV+-1)
"""

print(range(1, 11))     # range(1, 11)
print(type(range(1, 11)))   # <class 'range'>

"""
-> range class do not have a proper structure to display the output, so we make use of 
   typecasting
"""

print(list(range(1, 11)))       # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(tuple(range(2, 21, 2)))   # (2, 4, 6, 8, 10, 12, 14, 16, 18, 20)

print(set(range(-1, -11, -1)))  # {-2, -9, -8, -7, -6, -5, -4, -3, -1, -10}

"""
if SV=0 and up=1
        range(EV+1)
"""

print(list(range(11)))      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(range(5, 50, 5)))    # [5, 10, 15, 20, 25, 30, 35, 40, 45]

