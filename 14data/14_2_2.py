for x in range (1000, 3000):
    a = 4**2015 + 2**x - 2**2015 + 15
    s = []
    while a > 0:
        s = [a % 2] + s
        a = a//2
    if s.count(1) == 500:
        print(x)
