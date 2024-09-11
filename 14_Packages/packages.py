# packages
"""
* module - a file that contains python code such as functions, classes and variables
* package - are folders that contain multiple modules.
* Ex for modules - math, time, csv, etc
* import - a keyword which is used to import the module or get access to the module
* dir - get all the functions of a module in the form of list of strings
* using import we can import the module into a file but to use the functions present in it
  we have to make use of the syntax,
        modulename.function_name(args)
* from - it is a keyword which is used to import a particular functions or functions
         from the module
* '*' - used to import all the functions which are present inside the module and
        use it as it is, func_name(args)
* as - we can give new name to the module using 'as' keyword
"""
# import math

# import math
#
# print(dir(math))
"""
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 
'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 
'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 
'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 
'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 
'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 
'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 
'trunc', 'ulp']
"""
# print(math.factorial(8))    # 40320
# print(math.lcm(3, 9))   # 9

###############################################################################

# import math as m
#
# # print(math.factorial(9))    # NameError
#
# print(m.factorial(8))   # 40320
# print(m.gcd(3, 6))

###################################################################################

# from math import factorial, sqrt, gcd
# print(factorial(4))
# print(sqrt(87))
# print(gcd(3, 7))

##################################################################################

from math import *

print(factorial(8))
print(e)
print(pow(2, 9))
print(sin(pi/6))

