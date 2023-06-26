def d(x):
    s = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            s.add(i)
            s.add(x//i)
    return sorted(s)

for y in range(81234, 134689+1):
    a = d(y)
    if len(a) == 3:
        print(min(a), max(a))

#
# int(x**0.5)**2 == x # проверка на наличие нечет кол-ва делителей
#
