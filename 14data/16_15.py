for a in range(1,26):
    s=[]
    x=a
    while x > 0:
        s = [x % 6] + s
        x = x//6
    if s[0] == 4:
        print(a)