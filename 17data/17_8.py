f = [int(x) for x in open('17-7.txt')]
s=[]
for i in range(len(f)):
    sumc=sum(int(x) for x in str(f[i]))
    if sumc % 3 == 0:
        s.append(f[i])
print(len(s), max(s))