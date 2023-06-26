for n in range(1, 100):
    s = bin(n)[2:]
    if n % 3 == 0:
        s = s + s[-3:]
    else:
        s1 = (n % 3) * 3
        sb = bin(s1)[2:]
        s = s + sb
    r = int(s,2)
    if r < 76:
        print(n)