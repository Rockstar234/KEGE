s = 1 * '4' + 79 * '6' + 1 * '4'
while '63' in s or '664' in s or '6665' in s:
    if '63' in s:
        s = s.replace('63', '4', 1)
    else:
        if '664' in s:
            s = s.replace('664', '5', 1)
        else:
            if '6665' in s:
                s = s.replace('6665', '3', 1)
print(s)
