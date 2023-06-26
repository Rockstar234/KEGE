s = '5' * 500 
count = 0 
while s.count('555') or s.count('333'): 
    if s.count('333'): 
        count+=3 
        s = s.replace('333','5', 1) 
    else: 
        s = s.replace('555','3', 1) 
print(count) 
