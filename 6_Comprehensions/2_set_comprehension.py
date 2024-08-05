# Set comprehension

res = {i for i in range(10, 201) if i % 10 == 0 }
print(res)      # {130, 10, 140, 20, 150, 30, 160, 40, 170, 50, 180, 60, 190, 70, 200, 80, 90, 100, 110, 120}

st = 'hello world'
res1 = [ch for ch in st]
res2 = {ch for ch in st}
print(res1)
print(res2)
"""
['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
{' ', 'w', 'o', 'h', 'r', 'e', 'l', 'd'}
"""