from fnmatch import *
for i in range(0, 10**10,11071):
    if fnmatch(str(i), '?136*1') and str(i)[0] in '13579' and (str(i)[-2] in '02468' or len(str(i)) == 5):
        print(i, i//11071)