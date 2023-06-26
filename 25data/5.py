def d(x):
    s = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            s.add(i)
            s.add(x//i)
    return sorted(s)

for y in range(550001, 550101):
    a = d(y)
    if len(a) != 0:
        f = sum(a)//len(a)
    if f % 31 == 13:
        print(y, f)



#
# int(x**0.5)**2 == x # проверка на наличие нечет кол-ва делителей
#
