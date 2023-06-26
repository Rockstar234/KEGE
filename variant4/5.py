for n in range(1,1000):
    spisok=[]
    s = bin(n)[2:]
    s = s[1:]
    if s.count('1') % 2 == 0:
        s = '10' + s
    else:
        s = '1' + s + '0'
    r = int(s, 2)
    if r < 450:
        spisok.append(r)
    print(max(spisok))
