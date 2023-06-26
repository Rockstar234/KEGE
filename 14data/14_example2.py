a = 7**2 + 49**4 - 21
s = []
while a > 0:
    s = [a % 14] + s
    a = a//14
print(s.count(10))
print(s.count(0))
