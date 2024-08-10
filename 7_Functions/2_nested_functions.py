# nested functions
"""
-> Calling a function inside another function is called nested function
-> Syntax:
            def func1(args):
                -----------
                -----------
                def func2(args):
                    ------------
                    ------------
                func2()
                -------------
                return values

            func1(args)
                    or

            def func1(args):
                -----------
                -----------
                return values
            def func2(args):
                -----------
                -----------
                func1(args)
                return values
            func2(args)
"""

def extract_vowels(st):
    vowels = ''
    for ch in st:
        if ch in 'aeiouAEIOU':
            vowels += ch
    return vowels


li = ['good', 'morning', 'how', 'are', 'you']
# o/p = ['oo', 'oi', 'o', 'ae', 'ou']

def result(li):
    res = []
    for word in li:
        res += [extract_vowels(word)]
    return res


print(result(li))

##########################################################################################

# WAP to get the following output

nums = [86, 2, 986, 37, 8608]
# o/p = [68, 2, 689, 73, 8068]

def rev(num):
    rev = 0
    while num != 0:
        rev = rev * 10 + num % 10
        num = num // 10
    return rev


def res(li):
    res = []
    for num in li:
        res += [rev(num)]
    print(res)


res(nums)

