for n in range(1,100):
    s = 40 * '2' + 40 * '3' + n * '1'
    while '23' in s or '12' in s or '32' in s:
        if '12' in s:
            s = s.replace('12','21',1)
        if '32' in s:
            s = s.replace('32','1',1)
        if '23' in s:
            s = s.replace('23','2',1)
    if (sum(int(l) for l in s)) == 100:
        print(n)
        break