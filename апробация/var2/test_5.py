n = 4
s = bin(n)[2:]
print(s)
if n % 3 == 0:
    s = s + s[-3] + s[-2] + s[-1]
else:
    o = (n % 3) * 3
    z = bin(o)[2:]
    s = s+z
print(int(s,2))