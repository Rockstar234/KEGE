f = [int(x) for x in open('17-243.txt')]
s = []
#j = []
#for h in f:
#    if h % 49 == 0:
#        for g in str(h):
#            j.append(int(g))
summa=sum(int(b) for x in f if x % 49 == 0 for b in str(x))
for i in range(len(f)-1):
#    if ((f[i] > sum(j)) and f[i+1] % 10 == 7 and not(f[i+1] > sum(j))) or ((f[i+1] > sum(j)) and f[i] % 10 == 7 and not(f[i] > sum(j))):
    if ((f[i] > summa) and f[i+1] % 10 == 7 and not(f[i+1] > summa)) or ((f[i+1] > summa) and f[i] % 10 == 7 and not(f[i] > summa)):
        s.append(f[i]+f[i+1])
print(len(s), min(s))