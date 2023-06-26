s = open('2_24.txt').readline()
k=1
m=0
for i in range(len(s)-1):
    if (s[i] in 'NOP' and s[i+1] in 'NOP'):
        k=1
    else:
        k+=1
        m=max(m,k)
print(m)