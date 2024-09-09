# csv file -> comma separated values
# we have to import csv module to handle csv files

import csv
example_path = r"C:\Users\QSP\PycharmProjects\PCO_PFFPTD_M80\12_CSV_File_Handling\example.csv"

# reading a file
"""
-> We can read a file in 2 ways
1) list of strings - csv.reader(file_obj)
2) dictionary - csv.DictReader(file_obj)
"""

# Reader
with open(example_path) as file:
    reader_obj = csv.reader(file)
    print(reader_obj)
    next(reader_obj)
    for line in reader_obj:
        print(line)

"""
['John', 'TY123', 'Bengaluru']
['Mary', 'TY124', 'Chennai']
['Joseph', 'TY125', 'Hyderabad']
['Steve', 'TY126', 'Mumbai']
['Alex', 'TY127', 'Bengaluru']
['Bob', 'TY128', 'Hyderabad']
"""

# DictReader

with open(example_path) as file:
    reader_obj = csv.DictReader(file)
    for data in reader_obj:
        print(data)

"""
{'name': 'John', 'emp_id': 'TY123', 'place': 'Bengaluru'}
{'name': 'Mary', 'emp_id': 'TY124', 'place': 'Chennai'}
{'name': 'Joseph', 'emp_id': 'TY125', 'place': 'Hyderabad'}
{'name': 'Steve', 'emp_id': 'TY126', 'place': 'Mumbai'}
{'name': 'Alex', 'emp_id': 'TY127', 'place': 'Bengaluru'}
{'name': 'Bob', 'emp_id': 'TY128', 'place': 'Hyderabad'}
"""

################################################################################

# write into a csv file
"""
-> To write into a csv file we have to create a writer object by passing file 
   object to it
->      1) writer
            writer_obj = csv.writer(file_obj)
                -> writerow() - list of data
                -> writerows() - nested lists of data
        2) DictWriter
            writer_obj = csv.DictWriter(file_obj)
                -> writeheader() - to write fieldnames
                -> writerow() - dictionary
                -> writerows() - list of dictionaries
"""

# writer
path = r"C:\Users\QSP\PycharmProjects\PCO_PFFPTD_M80\12_CSV_File_Handling\sample.csv"

with open(path, 'w') as file:
    writer_obj = csv.writer(file)
    data = ['name', 'phno', 'salary']
    writer_obj.writerow(data)
    writer_obj.writerows([
        ['Ram', '9191919191', '70000'],
        ['Sita', '9292929292', '60000'],
        ['Lakshman', '9393939393', '650000']
    ])



