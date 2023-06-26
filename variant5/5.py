for n in range(1,101):
    r = bin(n)[2::]
    r = str(int(r[::-1]))
    if int(r,2) == 13:
        print(n)