for n in range(4,1000):
    s = bin(n)[2:]
    if n % 3 == 0:
        s = s + s[-3] + s[-2] + s[-1]
    else:
        o = (n % 3) * 3
        z = bin(o)[2:]
        s = s+z
    if int(s,2) < 100:
        print(n)