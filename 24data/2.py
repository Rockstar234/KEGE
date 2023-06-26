s = open('24_2.txt').readline()
s = s.replace('Z', ' ')

print(max(len(l) for l in s.split()))
#print(s)