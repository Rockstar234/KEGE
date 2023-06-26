k = 0
for n in range(10,18):
    s = []
    a = n
    while a > 0:
        s = [a % 5] + s
        a = a//5
    k = k + s.count(2)
print(k)
