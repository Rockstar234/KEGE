a = 4 * 343**5 + 6*49**8 - 50
s = []
while a > 0:
    s = [a % 7] + s
    a = a//7
print(s.count(6))