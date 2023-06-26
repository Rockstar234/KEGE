for n in range(1,100):
    s = bin(n)[2:]
    if n % 5 == 0:
        s = s + s[-3:]
    else:
        s1 = (n % 5)*5
        s1bin = bin(s1)[2:]
        s = s1bin + s
    if int(s,2) > 512:
        print(n)
        break