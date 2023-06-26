for n in range(2,71):
    s = []
    x = 70
    while x > 0:
        s = [x % n] + s
        x = x//n
    if len(s)==3:
        print(n)

#for n in range(2,71):
#    if n**2 <= 70 < n**3:
#        print(n)
