for ch in '02468':
    for h in '13579':
        for ch1 in '02468':
            for h1 in '13579':
                for ch2 in '02468':
                    for h2 in '13579':
                        a = int(f'1{ch}{h}{ch1}{h1}{ch2}{h2}')
                        if a % 4023 == 0:
                            print(a, a//4023)
