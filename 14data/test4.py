for n in range(4,381):
    if 381 % n == 3 and n**2 <= 381 < n**3:
        print(n)
