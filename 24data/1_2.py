s = open('24_1.txt').readline()
k = 0
m = 0
for x in range(len(s)):
    if s[x] == 'B':
        k+=1
        m=max(m,k)
    else:
        k=0
print(m)