for x in range (1, 100):
    a = 81**20 - 9**x + 50
    s = []
    while a > 0:
        s = [a % 9] + s
        a = a//9
    if sum(s) == 138:
        print(x)
