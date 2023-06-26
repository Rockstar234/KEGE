a = 43*7**103 - 21*7**57 + 98
s = []
while a > 0:
    s = [a % 7] + s
    a = a//7
b = sum(s)
print(b)
