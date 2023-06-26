def d(x):
    s = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            s.add(i)
            s.add(x//i)
    return sorted(s)

for y in range(193136, 193223+1):
    a = d(y)
    if len(a) == 6:
        print(a)