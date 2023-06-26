s = open('24_5.txt').readline()
k=1
m=0
for i in range(len(s)-1):
    if (s[i] == 'P' and s[i+1] == 'P'):
        k=1
    else:
        k+=1
        m=max(m,k)
print(m)