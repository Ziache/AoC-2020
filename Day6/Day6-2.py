def countgroup(glines):
    # counts the number of questions all the group answered yes

    # the initial value is the questions answered by the first person
    letters = [l for l in glines[0]]

    # we only have to test these questions, as the other questions
    # have been answered no by at least the first person
    for l in glines[0]:
        # for each person
        for p in glines:
            # the second condition is in case the letter
            # has already been removed by another person
            if l in p or (not l in letters):
                pass
            else:
                letters.remove(l)

    # as no letter appears more than once, the list length
    # corresponds to the number of questions answered yes collectively
    return len(letters)


with open("input.txt", "r") as f:
    lines = f.readlines()
    # c stands for "clean" as we get rid of the '\n' character
    clines = [l.split('\n')[0] for l in lines]
    # this operation is meant to check the last group in the condition line 36
    clines.append('')

    res = 0
    glines = []

    for l in clines:
        # case in which there are no more lines to describe the current group
        if (l == ''):
            # we add the number of questions answered in the group to the result
            res += countgroup(glines)

            # reset the group's lines
            glines = []

        # case in which the current line still describes the same group
        else:
            glines.append(l)

    print(res)
