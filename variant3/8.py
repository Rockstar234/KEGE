import itertools
s=[]
a = "РУСЛАН" 
glasnie = "УА"
perestanovka = itertools.permutations(a)
for i in perestanovka:
    s.append(list(i))
k=0
for i in s:
    flag = True
    for y in range(len(i)-1):
        if i[y] in glasnie and i[y+1] in glasnie:
            flag = False
    if flag:
        k+=1
print(k)