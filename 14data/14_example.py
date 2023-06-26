a = 125 + 25**3 + 5**9
s = []
while a > 0:
    s = [a % 5] + s
    a = a//5
print(s.count(0))
