k=0
alp = 'АВОРТ'
for a in alp:
    for b in alp:
        for c in alp:
            for d in alp:
                for e in alp:
                    for f in alp:
                        word = a+b+c+d+e+f
                        k+=1
                        if word == 'ВОРОТА':
                            print(k, word)