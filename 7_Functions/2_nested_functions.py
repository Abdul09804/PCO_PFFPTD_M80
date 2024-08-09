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


