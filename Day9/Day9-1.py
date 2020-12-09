def issumof(nb, ilist):
    # checks if a number 'nb' can be obtained by the sum
    # of two numbers of a list 'ilist'

    l = len(ilist)

    # for each different pair of i,j
    for i in range(l):
        ni = ilist[i]
        for j in range(i+1, l):
            nj = ilist[j]

            # we check if the sum of the two values is equal to nb
            if ni+nj == nb:
                return True

    # this return statement is only reached if no pair has been found
    return False


def invalidnumber(preamble, ilist):
    # returns the first number not to check the sum rule.
    # 'preamble' is the size of the preamble.

    l = len(ilist)
    # list of the predecessors
    pre = ilist[:preamble]

    # for each number after the preamble
    for i in range(preamble, l):
        nb = ilist[i]

        # if the condition is satisfied, we do nothing
        if issumof(nb, pre):
            pass

        # otherwise we return the number
        else:
            return nb

        # we update the predecessors list
        del pre[0]
        pre.append(nb)


with open("input.txt", "r") as f:

    lines = f.readlines()
    clines = [l.split('\n')[0] for l in lines]
    ilines = [int(l) for l in clines]

    print(invalidnumber(25, ilines))
