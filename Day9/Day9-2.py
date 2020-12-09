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


def sumofN(nb, ilist):
    # checks if a number 'nb' can be obtained by the sum
    # of N contiguous numbers of a list 'ilist'.
    #
    # returns the list of these numbers if they exist.

    l = len(ilist)

    # initial parameters
    res = 0
    reslist = []
    j = 0

    # for each 'first' number i
    for i in range(l):
        # while 'nb' is not reached
        while res < nb:
            n = ilist[i+j]
            res += n
            reslist.append(n)

            # if 'nb' is reached, we return the list
            if res == nb:
                return reslist

            # otherwise we keep on adding numbers
            j += 1

        # if the previous step did not find a result,
        # we reset the parameters
        res = 0
        reslist.clear()
        j = 0

    # this return statement is only reached if no match has been found
    return []


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

    # the invalid number from part one
    invalid = invalidnumber(25, ilines)

    # the numbers that sum that 'invalid' number
    slist = sumofN(invalid, ilines)

    # I personnaly prefer sorting the list rather than taking
    # min and max, but this perfectly works too
    sort = sorted(slist)

    # The first and last elements are the min and max of the list
    print(sort[0] + sort[-1])
