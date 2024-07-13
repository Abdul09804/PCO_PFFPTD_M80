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
# print(st[-1:-8-1:-1])
# print(st[13:6-1:-1])

# # l nvre
# print(st[3:13+1:2])

"""
-14	-13	-12	-11	-10	-9	-8	-7	-6	-5	-4	-3	-2	-1
h	e	l	l	o		u	n	i	v	e	r	s	e
0	1	2	3	4	5	6	7	8	9	10	11	12	13
"""