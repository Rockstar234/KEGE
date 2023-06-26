a = 6**203 + 5*6**405 - 3*6**144 + 76
s = []
while a > 0:
    s = [a % 6] + s
    a = a//6
print(sum(s))
