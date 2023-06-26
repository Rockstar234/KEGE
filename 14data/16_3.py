for n in range(3,339):
    a = []
    x = 338
    while x > 0:
        a = [x % n] + a
        x = x//n
    if a[-1]==2 and len(a)==3:
        print(n)
