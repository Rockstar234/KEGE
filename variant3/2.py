print('x y z w')
for x in range(2):
    for y in range (2):
        for z in range(2):
            for w in range(2):
                if ((not(x)==z) <= (y==(w or x)))==False:
                    print(x,y,z,w)




















#debug
# x y z w
# 0 0 1 1
# 1 0 0 0
# 1 0 0 1
#answer
# y x w z
# 0 0 1 1 
# 0 0 1 0 
# 0 1 0 0