for x in range(0,44):
    left = 1 * 44**3 + x*44**2 + 2 * 44**1 + 3 * 44**0
    right = 3 * 44**3 + 2 * 44**2 + x*44**1 + 1 * 44**0
    r = left + right
    if r % 42 == 0:
        print(r//42)
