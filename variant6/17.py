f = [int(x) for x in open('17.txt.')]
s=[]
k=0
sum=0
for n in range(len(f)):
    if f[n] % 2 != 0:
        sum = sum + f[n]
        k+=1
sr = sum // k
print(sr)
for i in range(len(f)-1):
    if ((f[i] % 5 == 0) or (f[i+1] % 5 == 0)) and ((f[i] < sr) or (f[i+1] < sr)):
        s.append(f[i]+f[i+1])
print(len(s), max(s))