s = open('24_6.txt').readline()
k=2
m=0
for i in range(len(s)-2):
    if s[i] == '0' and s[i+1] == '0' and s[i+2] == '0':
        k=2
    else:
        k+=1
        m=max(m,k)
print(m)