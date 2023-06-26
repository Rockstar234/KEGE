a = 36**7 + 6**19 - 18
s = []
while a > 0:
    s = [a % 6] + s
    a = a//6
print(s.count(5))