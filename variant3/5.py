for i in range(1,100):
    s = bin(i)[2:]
    if s.count('1') % 2 == 0:
        n = s + '00'
    else:
        n = s + '10'
    if int(n, 2) > 97:
        print(int(n, 2))
        break