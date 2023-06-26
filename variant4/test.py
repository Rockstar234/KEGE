from itertools import *
r = set()
for i in product('антиуопяZ', repeat = 7):
    s = ''.join(i)
    if s.count('Z') == 1: 
        r.add(s)
print(len(r))