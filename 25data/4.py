def d(x):
    s = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            s.add(i)
            s.add(x//i)
    return sorted(s)

for y in range(135790, 163228+1):
    a = d(y)
    if sum(a) > 460000:
        print(len(a), sum(a))

#
# int(x**0.5)**2 == x # проверка на наличие нечет кол-ва делителей
#
