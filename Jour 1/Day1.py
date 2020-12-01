with open("input.txt", "r") as f:
    lines = f.readlines()

    # c stands for "clean", as we remove the '\n' character
    clines = [i.split('\n')[0] for i in lines]

    # i stands for "integer"
    ilines = [int(i) for i in clines]

    l = len(ilines)

    for i in range(l):
        li = ilines[i]
        for j in range(i+1, l):
            lj = ilines[j]
            for k in range(j+1, l):
                lk = ilines[k]
                if (li + lj + lk == 2020):
                    print(li*lj*lk)
