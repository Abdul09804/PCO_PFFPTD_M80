# output_statement
"""
-> It is used to display the result
-> Syntax:
        print(Val1, Val2, ..., Valn, sep=" ", end="\n")
        where, sep and end are default parameters
"""
# print(10, 20, 30, 40, 50)   # 10 20 30 40 50
#
# print(10, 20, 30, 40, 50, sep="\n")
# """
# 10
# 20
# 30
# 40
# 50
# """
#
# print(1, 2, 3, 4, 5, sep="")    # 12345
# print(1, 2, 3, 4, 5, sep='\t')  # 1	  2   3   4   5

print(10, 20, 30, 40, 50)
print(60, 70, 80, 90)
"""
10 20 30 40 50
60 70 80 90
"""

# print(10, 20, 30, 40, 50, end=" ")
# print(60, 70, 80, 90)
"""
10 20 30 40 50 60 70 80 90
"""
# print(10, 20, 30, 40, 50, end=" ")
# print(60, 70, 80, 90, end=" ")


# a b c d e
print('a', 'b', 'c', 'd', 'e')

# a$b$c$e$f@
print('a', 'b', 'c', 'd', 'e', 'f', sep='$', end='@\n')

