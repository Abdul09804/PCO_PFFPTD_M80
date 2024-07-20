# Copy Operation
"""
-> Copying the contents of one variable to another variable is called copy operation
-> the content can be either variable space or value space
-> 1) General Copy/ Normal Copy
   2) Shallow Copy
   3) Deep Copy
"""

# 1) General Copy
"""
-> We copy the variable space of one variable to another variable
-> Syntax:
        dest_var = source_var
-> Changes wrt one variable will change other variable both incase of nested and
   linear list
"""

# nums = [1, 2, [3, 4]]
# gen_copy = nums
#
# print(id(nums), id(gen_copy))   # 2220785038272 2220785038272
#
# nums[1] = 20
# print(nums)     # [1, 20, [3, 4]]
# print(gen_copy)     # [1, 20, [3, 4]]

#################################################################################

# 2) Shallow Copy
"""
-> In case of shallow copy, value space of one variable will be moved to another
   variable
-> Syntax:
            dest_var = source_var.copy()
-> The changes wrt one list will change another list if it a nested list, in case
   of linear list the changes will not happen.
"""

# nums = [1, 2, [3, 4]]
# shallow_copy = nums.copy()
# print(id(nums), id(shallow_copy))   # 2029811626944 2029811627200
#
# print(id(nums[2]), id(shallow_copy[2]))     # 2366595616256 2366595616256
#
# nums[0] = 10
# print(nums)     # [10, 2, [3, 4]]
# print(shallow_copy)     # [1, 2, [3, 4]]
#
# shallow_copy[2][1] = 30
# print(nums)             # [10, 2, [3, 30]]
# print(shallow_copy)     # [1, 2, [3, 30]]

###################################################################################

# 3) Deep Copy
"""
-> In this case all the values will be copied from one variable to another variable
-> Syntax:
            import copy
            dest_var = copy.deepcopy(source_var)
-> Changes wrt one variable will not change other variable both incase of linear
   and nested list
"""

# import copy
# nums = [1, 2, [3, 4]]
# deep_copy = copy.deepcopy(nums)
# print(id(nums), id(deep_copy))      # -> different
# print(id(nums[2]), id(deep_copy[2]))    # -> different
#
# nums[0] = 10
# print(nums, deep_copy)      # [10, 2, [3, 4]] [1, 2, [3, 4]]
#
# deep_copy[2][1] = 44
# print(nums, deep_copy)      # [10, 2, [3, 4]] [1, 2, [3, 44]]

