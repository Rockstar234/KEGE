for x in range(80):
    s = 3 * 1 + 1 * x**1 + 1 * x**2 + 5 * x**3 + 5 * x**4
    s1 = 5 * 1 + x * 80**1 + x * 80**2 + 7 * 80**3
    r = abs(s - s1)
    if r <= 1000000:
        print(x)
