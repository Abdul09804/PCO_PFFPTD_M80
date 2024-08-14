# decorators

def sam(some_val):
    return some_val


print(sam(18))      # 18
print(sam("hello"))     # hello

a = 'hello world'
b = sam(a)
print(b)

def add(a, b):
    return a + b

print(add)      # <function add at 0x00000250A190AF20>
print(add(3, 4))    # 7

a = sam(add)
print(a)        # <function add at 0x0000016262D2AF20>

b = add
print(b)        # <function add at 0x000001EADF82AF20>

print(add(33, 44))      # 77
print(a(33, 44))        # 77
print(b(3, 4))      # 7