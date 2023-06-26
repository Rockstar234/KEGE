for i in range(200, 300):
    s = i * '1'
    a = []
    while '1111' in s:
        s = s.replace('1111', '22', 1)
        s = s.replace('222', '1', 1)
        b = s.count('1')
        a = [b, i]
    print(a)