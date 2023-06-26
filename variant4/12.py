r=0
for n in range(10,100):
    s = '1' + n * '0'
    while '10' in s:
        if '10' in s:
            s = s.replace('10', '001', 1)
        if '1' in s:
            s = s.replace('1', '01', 1)
    dlina = len(s)
    k=0
    for y in range(1, dlina+1): 
        if dlina % y == 0:
            k+=1 
    if k == 2:
        print(dlina)
        r+=1
print('Ответ:', r)