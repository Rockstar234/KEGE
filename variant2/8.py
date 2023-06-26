import itertools
a = "ПОЛИНА" # алфавит
sgl = "ПЛН" # согласные
glas = "ОИА" # гласные
ar = itertools.permutations(a) # перестановка 
s = []
for e in ar:
    s.append(list(e))
count = 0
for e in s:
    flag = True
    for i in range(len(e)-1):
        if (e[i] in sgl and e[i+1] in sgl) or (e[i+1] in glas and e[i] in glas):
            flag = False
    if flag:
        count += 1
print(count)