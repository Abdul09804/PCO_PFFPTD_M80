# nested if
"""
-> Syntax:
            if <cond1>:
                if <cond2>:
                    TSB2
                else:
                    FSB2
            else:
                FSB1
"""
"""
1) WAP to check if a given list has mid-value, if it has mid-value then check if it is
   an integer
"""

li = [1, 2, 'a', 4, 5]
if len(li) % 2 != 0:
    print('List has a mid value')
    if type(li[len(li)//2]) == int:
        print('The value is an intger')
    else:
        print('The value is not an integer')
else:
    print('List does not have a mid value')

"""
2) WAP to check if a given data is an integer, if it is an integer then check if it is 
   divisible by 8
"""

# data = 'hai'
# if type(data) == int:
#     print('The given data is an integer')
#     if data % 8 == 0:
#         print('It is divisible by 8')
#     else:
#         print('NOt divisible by 8')
# else:
#     print('The given data is not an integer')

# 3) WAP to check if a user can log in to his/her instagram account

# original_username = "admin"
# original_password = "admin123"
# username = input('Enter the username : ')
# if username == original_username:
#     password = input('Enter the password : ')
#     if password == original_password:
#         print('Login Successful')
#     else:
#         print('Password Incorrect')
# else:
#     print('Invalid Username')

"""
4)  WAP to take input for 6 subject marks of a student, check if the student has 
    scored more than 35 in all the subjects, if he has scored more than 35 in all
    subjects calculate the total marks and print the result along with percentage.
    if the student has scored less than 35 in any one of teh subject then print FAIL
    result -> distinction, first class, second class, pass class, FAIL
"""

# 5) WAP to find the second highest among 3 distinct numbers

num1 = int(input())
num2 = int(input())
num3 = int(input())
if num1 > num2 and num1 > num3:
    if num2 > num3:
        print('num2 is greater')
    else:
        print('num3 is greater')
elif num2 > num3:
    if num3 > num1:
        print('num3 is greater')
    else:
        print('num1 is greater')
else:
    if num1 > num2:
        print('num1 is greater')
    else:
        print('num2 is greater')

# 6) WAP to find the second lowest among 4 distinct numbers

