k=0
alp = 'АКЛМНЯ'
for a in alp:
    for b in alp:
        for c in alp:
            for d in alp:
                for e in alp:
                    word = a+b+c+d+e
                    if (a == 'М') and (b == 'Н'):
                        k+=1
print(k-2)