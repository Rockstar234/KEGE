f = [int(x) for x in open('17-257.txt')]
s = []
for i in range(len(f)):
    if f[i] % 2 != 0:
        s.append(f[i])
sumc=max(s)+min(s)
s2=[]
for i in range(len(f)-1):
    if (f[i]+f[i+1]) % 2 == 0 and (f[i]+f[i+1]) > sumc:
        s2.append(f[i]+f[i+1])
print(len(s2), min(s2))