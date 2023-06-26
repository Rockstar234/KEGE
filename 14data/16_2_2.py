for n in range(13, 100):
    a1 = n
    a2 = n
    a3 = n
    s = []
    while a1 > 0:
        s = [a1 % 6] + s
        a1 = a1//6
    b = []
    while a2 > 0:
        b = [a2 % 7] + b
        a2 = a2//7
    c = []    
    while a3 > 0:
        c = [a3 % 13] + c
        a3 = a3//13
    if len(b)==2 and len(s)==3 and c[-1]==3:
        print(n)
