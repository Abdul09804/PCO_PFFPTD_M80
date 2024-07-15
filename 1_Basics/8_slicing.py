# Slicing
"""
-> Fetch group of values from a collection is called slicing
-> Syntax:
            Var[SI:EI+-1:SV]
            where,
                SI -> Start Index
                EI -> End Index
                SV -> Step Value
                   -> The constant difference between index numbers of 2 consecutive
                      values to be fetched
                   -> if SV == 1,
                            Var[SI:EI+-1]
                EI+1 -> when we want to fetch the values from left to right of the collection
                EI-1 -> when we want to fetch the values from right to left of the collection
"""

st = 'hello universe'
"""
-14	-13	-12	-11	-10	-9	-8	-7	-6	-5	-4	-3	-2	-1
h	e	l	l	o		u	n	i	v	e	r	s	e
0	1	2	3	4	5	6	7	8	9	10	11	12	13
"""

# # hello
# print(st[0:4:1])
# print(st[0:5])
# print(st[-14:-10+1:1])
# print(st[-14:-9])

# # uni
# print(st[6:9:1])
# print(st[6:9])
# print(st[-8:-5:1])
# print(st[-8:-5])

# # universe
# print(st[6:14:1])
# print(st[6:14])

###########################################################################

# slicing by ordered index

# # hlouies
# print(st[0:12+1:2])
# print(st[-14:-2+1:2])

# # eonee
# print(st[1:14:3])


# # esrevinu
# print(st[-1:-8-1:-1])     # st[13:5:-1]
# print(st[13:6-1:-1])

# # l nvre
# print(st[3:13+1:2])

# # universe
# print(st[6:14])
# print(st[-8:0])     # ''    # st[6:0]
# print(st[-8:])      # universe
# print(st[6:])       # universe
#
# # olleh
# print(st[-10:-14-1:-1])
# print(st[4:-1:-1])      # st[4:13:-1]   # ''
# print(st[4::-1])        # olleh
# print(st[-10::-1])      # olleh

"""
-> When we want to fetch the value upto the extreme end(left or right),
   we can ignore writing EI+-1 parameter in slicing syntax
            Var[SI::SV]
"""
#
# # hello
# print(st[0:5])
# print(st[:5])
# print(st[:-9])
# print(st[-14:-9])
#
# # esrevinu
# print(st[13:5:-1])
# print(st[-1:-9:-1])
# print(st[:-9:-1])
# print(st[:5:-1])

"""
-> When we want to fetch the values from the extreme end(right or left)
   we can ignore writing SI parameter
            Var[:EI+-1:SV]
"""

# reverse the given string

# # esrevinu olleh
# print(st[::-1])     # esrevinu olleh
#
# # hello universe
# print(st[::])
# print(st)
#
#
# # first 2 values
# print(st[:2])
#
# # first 5 values
# print(st[:5])

"""
-> To fetch the first 'n' values we make use of the syntax,
            Var[:n]
"""

# last 2 values
# print(st[-2:])
#
# # last 5 values
# print(st[-5:])

"""
-> To get the last 'n' values we make use of the syntax,
            Var[-n:]
"""

##########################################################################################

sam = [4, 9.75, 'hello', ['john', 'steve', 'mary'], {8, 56, 93}, (6, 3)]

# # 9.75
# print(sam[1])
#
# # 'steve'
# print(sam[3][1])
#
# # 'mary'
# print(sam[3][2])
#
# # 'yram'
# print(sam[3][2][::-1])
#
# # (3, 6)
# print(sam[5][::-1])
#
# # ['mary', 'steve']
# print(sam[3][2:0:-1])
#
# # 4
# print(sam[0])
#
# # [4]
# print(sam[0:0+1])

pyspiders = {'development': ['python',
                             'sql',
                             {'web technology': ['html', 'css', 'java script']},
                             'django'],
             'testing': ['python',
                         'sql',
                         {'manual testing': ['sdlc', 'testing', 'stlc']},
                         'automation']
             }

# python
print(pyspiders['development'][0])
print(pyspiders['development'][0])

# sql
print(pyspiders['development'][1])
print(pyspiders['testing'][1])

# html
print(pyspiders['development'][2]['web technology'][0])

# testing
print(pyspiders['testing'][2]['manual testing'][1])

# ssc
print(pyspiders['development'][2]['web technology'][1][::-1])

# clts
print(pyspiders['testing'][2]['manual testing'][2][::-1])

# ognajd
print(pyspiders['development'][3][::-1])

#############################################################################

sam = {'a': ['java', 'python'],
       'b': ('manual', 'automation'),
       'c': {'data', 'sql', 'manual'},
       'd': {'e': {'f': [1, 2, [3, 4]]}}
       }


# automation
# manual
# [4, 3]
# avaj

