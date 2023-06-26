s = open('24_3_.txt').readline()
k=1
m=0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        k += 1
        m=max(m,k)
    else:
        k=1
print(m)