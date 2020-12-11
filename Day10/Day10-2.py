def tribo(n):
    # aux function that computes the 'tribonacci' sequence :
    #
    # tribo(0) = 1
    # tribo(1) = 1
    # tribo(2) = 2
    # tribo(n) = tribo(n-1) + tribo(n-2) + tribo(n-3), n > 2

    if n < 2:
        return 1
    elif n == 2:
        return 2
    else:
        return tribo(n-1) + tribo(n-2) + tribo(n-3)


def nbalter(lines):
    # finds the number of alternatives, by following this rule :
    #
    # the number of alternatives rely on steps where there are
    # 2 or more contiguous differences of one.
    #
    # More precisely, in a sub-sequence of n ones,
    # the number of alternatives is tribo(n), with tribo defined line 1.
    #
    # So, we only have to compute tribo(n) to the sequences of ones,
    # and then multiply them all.
    #
    # This one was tough haha

    # initial number of alternatives
    alt = 1

    # first we add the first and the last output
    lines.insert(0, 0)
    l = len(lines)
    lines.append(lines[-1] + 3)

    # list of differences
    diffs = [lines[i+1] - lines[i] for i in range(l)]

    # number of consecutive ones
    nb1 = 0
    for i in diffs:
        if i == 1:
            nb1 += 1
        else:
            alt *= tribo(nb1)
            nb1 = 0

    return alt


with open("input.txt", "r") as f:
    lines = f.readlines()
    clines = [l.split('\n')[0] for l in lines]
    ilines = [int(l) for l in clines]
    slines = sorted(ilines)

    print(nbalter(slines))
