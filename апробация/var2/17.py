f = [int(x) for x in open('17_27052.txt')]
s=[]
for i in range(len(f)):
    if (100 <= f[i] < 1000) and (f[i] % 10 == 5):
        s.append(f[i])
z = min(s)
s1=[]
for i in range(len(f)-1):
    if ((f[i]+f[i+1]) % z == 0) and (((100 <= f[i] < 1000) and (not((100 <= f[i+1] < 1000)))) or ((100 <= f[i+1] < 1000) and (not((100 <= f[i] < 1000))))):
        s1.append(f[i]+f[i+1])
print(len(s1),min(s1))
