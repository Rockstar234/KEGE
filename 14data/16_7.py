for n in range(11, 100):
    a1 = n
    a2 = n
    a3 = n
    s = []
    while a1 > 0:
        s = [a1 % 6] + s
        a1 = a1//6
    b = []
    while a2 > 0:
        b = [a2 % 5] + b
        a2 = a2//5
    c = []    
    while a3 > 0:
        c = [a3 % 11] + c
        a3 = a3//11
    if len(b)==3 and len(s)==2 and c[-1]==1:
        print(n)
