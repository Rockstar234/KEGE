for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((y and (not(x))) or (x==z) or (not(w)))==False:
                    print(x,y,z,w)