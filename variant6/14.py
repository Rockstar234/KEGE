for x in range(1,100):
    left = 2*18**3 + 8*18**2 + x*18**1 + 2*18**0 
    right = 9*12**3 + 3*12**2 + x*12**1 + 5*12**0
    rez = left + right
    if rez % 133 == 0:
        print(rez//133)