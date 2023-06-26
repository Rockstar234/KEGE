s = open('24_4.txt').readline()
k=1
m=0
for i in range(len(s)-1):
    if (s[i] in '123' and s[i+1] in 'ABC') or (s[i] in 'ABC' and s[i+1] in '123'):
        k+=1
        m=max(m,k)
    else:
        k=1
print(m)