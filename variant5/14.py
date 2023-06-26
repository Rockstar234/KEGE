a = 4**2013 + 2**2012 - 16
s = []
while a > 0:
    s = [a % 2] + s
    a = a//2
print(s.count(1))