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

#################################################################################

# read from a file - read, readline, readlines

# 1) read

# with open(sample_path) as file:
#     data = file.read()
#     print(data)
#     print(type(data))
"""
Hello Everyone
Good morning
How are you
It's a long weekend
Festival Week
<class 'str'>
"""

# with open(sample_path) as file:
#     print(file.read(5))
#     print(file.read(14))
#     print(file.read(5))

# with open(sample_path) as file:
#     print(file.tell())      # 0
#     print(file.read(5))
#     print(file.tell())
#     print(file.seek(0))
#     print(file.read(10))
#     print(file.seek(3))
#     print(file.read(10))

# 2) readline - used to read one line at a time

# with open(sample_path) as file:
#     print(file.readline())
#     print(file.readline())
#     print(file.readline(5))
#     print(file.readline(10))
#     print(file.readline())

# 3) readlines - used to read entire file in the form of list of strings

# with open(sample_path) as file:
#     print(file.readlines())


# for loop

# with open(sample_path) as file:
#     for line in file:
#         print(line)
#     file.seek(0)
#     for line in file:
#         print(line)


##############################################################################

# writing into a file -> write(data), writelines(data)

# with open("sample1.txt", 'w') as file:
#     print(file.write("Hello\n"))            # 6
#     print(file.write("Good morning\n"))     # 13
#     print(file.writelines(["Tomorrow is a holiday\n", "It's a long weekend\n"]))   # None

# with open("sample1.txt", 'a') as file:
#     print(file.write("Hello\n"))  # 6
#     print(file.write("Good morning\n"))  # 13
#     print(file.writelines(["Tomorrow is a holiday\n", "It's a long weekend\n"]))

# with open("sample5.txt", "x") as file:
#     print(file.write("Hello\n"))  # 6
#     print(file.write("Good morning\n"))  # 13
#     print(file.writelines(["Tomoorrow is a holiday\n", "It's a long weekend\n"]))

#####################################################################################

"""
w+ -> write and read
r+ -> read and append
"""

###################################################################################

# count the number of lines in sample.log

sample_log_path = r"C:\Users\QSP\PycharmProjects\PCO_PFFPTD_M80\10_File_Handling\sample.log"

with open(sample_log_path) as file:
    count = 0
    for line in file:
        count += 1
    print(count)

# count the number of non-blank lines

with open(sample_log_path) as file:
    count = 0
    for line in file:
        if line.strip():
            count += 1
    print(count)

# count the blank line

with open(sample_log_path) as file:
    count = 0
    for line in file:
        if not(line.strip()):
            count += 1
    print(count)


################################################################################

# capture all the messages in sample.log

with open(sample_log_path) as file:
    messages = []
    for line in file:
        if line.strip():
            words = line.split()
            if words[2] not in messages:
                messages.append(words[2])
    print(messages)     # ['INFO', 'TRACE', 'WARNING', 'EVENT']


# create a dictionary of messages and their occurrences in sample.log

with open(sample_log_path) as file:
    messages = {}
    for line in file:
        if line.strip():
            message = line.split()[2]
            if message not in messages:
                messages[message] = 1
            else:
                messages[message] += 1
    print(messages)

################################################################################

# capture all the ip addresses from access-log file

access_log_path = r"C:\Users\QSP\PycharmProjects\PCO_PFFPTD_M80\10_File_Handling\access-log.txt"

with open(access_log_path) as file:
    ip_addresses = []
    for line in file:
        if line.strip():
            ip = line.split()[0]
            if ip not in ip_addresses:
                ip_addresses.append(ip)
    print(ip_addresses)


# count the number of occurrences of each ip address

with open(access_log_path) as file:
    ip_addresses = {}
    for line in file:
        if line.strip():
            ip = line.split()[0]
            if ip not in ip_addresses:
                ip_addresses[ip] = 1
            else:
                ip_addresses[ip] += 1
    print(ip_addresses)

# write all the unique ips to unique.txt

file_obj = open(access_log_path)
unique_ips = {line.split()[0] for line in file_obj if line.strip()}
print(unique_ips)
file_obj.close()

with open("unique.txt", 'w+') as file:
    for ip in unique_ips:
        file.write(ip + '\n')
    file.seek(0)
    print(file.read())

###############################################################################

# count the number of words in sample.txt

with open(sample_path) as file:
    count = 0
    for line in file:
        if line.strip():
            words = line.split()
            count += len(words)
    print(count)

#################################################################################

# get the list of all countries from football.txt

football_path = r"C:\Users\QSP\PycharmProjects\PCO_PFFPTD_M80\10_File_Handling\football.txt"

with open(football_path, encoding="UTF-8") as file:
    countries = []
    next(file)          # skip the first line
    for line in file:
        if line.strip():
            country = line.split('\t')[1]
            if country not in countries:
                countries.append(country)
    print(countries)


# group the country with their group names

with open(football_path, encoding="UTF-8") as file:
    groups = {}
    file.readline()
    for line in file:
        if line.strip():
            data = line.split('\t')
            group, country = data[0], data[1]
            if group not in groups:
                groups[group] = {country}
            else:
                groups[group].add(country)
    print(groups)




