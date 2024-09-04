# file handling

# open() - returns a file object - we get access to a file

sample_path = r"C:\Users\QSP\PycharmProjects\PCO_PFFPTD_M80\10_File_Handling\sample.txt"

# without context manager

# file_obj = open(sample_path)
# print(file_obj)

# # file attributes

# print(file_obj.name)    # C:\Users\QSP\PycharmProjects\PCO_PFFPTD_M80\10_File_Handling\sample.txt
# print(file_obj.mode)    # r
# print(file_obj.readable())  # True
# print(file_obj.writable())  # False
# print(file_obj.closed)      # False
#
# print(file_obj.close())     # None
# print(file_obj.closed)      # True

# # with context manager

# with open(sample_path) as file:
#     print(file.name)        # C:\Users\QSP\PycharmProjects\PCO_PFFPTD_M80\10_File_Handling\sample.txt
#     print(file.mode)        # r
#     print(file.closed)      # False
#
# print(file.closed)          # True

#################################################################################

# modes
"""
1) read - r - default mode
-> It is the default mode used to read from a file
-> If the file is not present control will throw FileNotFoundError

2) write - w
-> If the file is not present, a new file will be created in the same directory
-> If the directory is specified, file will be created in that directory
-> If the file is already existing it will over write the file

3) append(a)
-> It is used to add/ append the data to an existing file
-> If the file is not present, a new file will be created

# 4) create(x)
-> It creates a new file if the file is not existing
-> If the file is existing, it will throw FileExistsError
-> It is used to avoid overwriting of files
"""

# 1) read - r

# without context manager

# file_obj = open(r"sample1.txt")     # FileNotFoundError
# file_obj = open(sample_path)
# print(file_obj.mode)            # r
# print(file_obj.readable())      # True
# print(file_obj.writable())      # False
# print(file_obj.closed)          # False
#
# file_obj.close()
# print(file_obj.closed)          # True

# with context manager

# with open(sample_path) as file:
#     print(file.mode)            # r
#     print(file.closed)          # False
#     print(file.readable())      # True
#
# print(file.closed)      # True

# 2) write(w)

# without context manager
# file_obj = open("sample1.txt", 'w')
# file_obj = open(r"C:\Users\QSP\PycharmProjects\PCO_PFFPTD_M80\7_Functions\sample2.txt", 'w')
# file_obj = open(sample_path, 'w')
# print(file_obj.name)
# print(file_obj.mode)
# print(file_obj.writable())      # True
# print(file_obj.readable())      # False
# print(file_obj.close())
# print(file_obj.closed)          # True

# 3) append(a)

# # file_obj = open("sample2.txt", 'a')
# file_obj = open(sample_path, 'a')
# print(file_obj.readable())      # False
# print(file_obj.writable())      # True
# print(file_obj.mode)            # a
# print(file_obj.closed)          # False
# file_obj.close()
# print(file_obj.closed)          # True

# 4) create(x)
# file_obj = open("sample3.txt", 'x')     # FileExistsError:
# file_obj = open("sample4.txt", 'x')
# print(file_obj.writable())      # True
# print(file_obj.readable())      # False
# print(file_obj.name)
# print(file_obj.closed)          # False
# file_obj.close()
# print(file_obj.closed)          # True
