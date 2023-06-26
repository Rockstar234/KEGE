for x in '0123456789ABCDEFGHIJKL':
    for y in '012345689ABC':
        s = int(x + '23' + x + '5', 22)
        s1 = int('67' + y + '9' + y, 13)    
        r = s - s1
        if r % 57 == 0:
            print(r//57, x+y)
