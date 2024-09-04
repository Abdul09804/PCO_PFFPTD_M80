# file handling

# open() - returns a file object - we get access to a file

sample_path = r"C:\Users\QSP\PycharmProjects\PCO_PFFPTD_M80\10_File_Handling\sample.txt"

# without context manager

file_obj = open(sample_path)
print(file_obj)

# file attributes
print(file_obj.name)    # C:\Users\QSP\PycharmProjects\PCO_PFFPTD_M80\10_File_Handling\sample.txt
print(file_obj.mode)    # r
print(file_obj.readable())  # True
print(file_obj.writable())  # False
print(file_obj.closed)      # False

print(file_obj.close())     # None
print(file_obj.closed)      # True

# with context manager
with open(sample_path) as file:
    print(file.name)        # C:\Users\QSP\PycharmProjects\PCO_PFFPTD_M80\10_File_Handling\sample.txt
    print(file.mode)        # r
    print(file.closed)      # False

print(file.closed)          # True

