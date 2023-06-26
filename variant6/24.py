s = open('24.txt').readline()
k=3
m=0
for i in range(len(s)-3):
    if (s[i] == 'X' and s[i+1] == 'Z' and s[i+2] == 'Z' and s[i+3] == 'Y'):
        k=3
    else:
        k+=1
        m=max(m,k)
print(m)