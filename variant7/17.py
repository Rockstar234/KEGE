f = [int(x) for x in open('17.txt')]
s=[]
k=0
for i in range(len(f)):
    sumc = sum(int(l) for l in str(f[i]))
    s.append(sumc)
s1=[]
for i in range(len(f)-1):
    if (((f[i] % 100 == 10) and (f[i+1] % 100 != 10)) and (f[i]+f[i+1] < sum(s))) or (((f[i+1] % 100 == 10) and (f[i] % 100 != 10)) and (f[i]+f[i+1] < sum(s))):
        s1.append(f[i]+f[i+1])
print(len(s1), min(s1))