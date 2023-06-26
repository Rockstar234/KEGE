for n in range(2,325):
    s = []
    x = 325
    while x > 0:
        s = [x % n] + s
        x = x//n
    if s[-1]==1 and len(s)==3:
        print(n)