from itertools import product
a = 0
for b in 'ИВАН':
    for c in 'ИВАН':
        for d in 'ИВАН':
            for e in 'ИВАН':
                for f in 'ИВАН':
                    s = b+c+d+e+f
                    if s.count('И') >= 1:
                        a += 1
print(a)
