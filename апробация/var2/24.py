s = open('24_1.txt').readline()
s = s.replace('O', 'N').replace('P', 'N')
while 'NN' in s:
    s = s.replace('NN', 'N N')
print(s)    
print(max(len(l) for l in s.split()))