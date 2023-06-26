s = 44 * '1' + 21 * '2'
while '111' in s:
    s = s.replace('111', '2', 1)
    s = s.replace('22', '1', 1)
print(s)
