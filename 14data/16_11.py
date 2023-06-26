for n in range(2,280):
    s = []
    x = 280
    while x > 0:
        s = [x % n] + s
        x = x//n
    if s[-1]==0 and len(s)==3:
        print(n)