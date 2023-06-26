a = '1234567890abcde'
for i in a:
    x1 = '123' + i + '5'
    x2 = '1' + i + '233'
    r = int(x1, 15) + int(x2,15)
    if r % 14 == 0:
        print(i, r//14)