count = 0
for i in range(1, 1000000001):
    if bin(i).count('1') == 2:
        count += 1

print(count)