def countgroup(glines):
    # counts the number of questions the group answered yes, combined

    letters = []

    # for each person
    for p in glines:
        # and for each question they answered
        for l in p:
            # if the question has already been answered yes
            # by someone in the group, we do nothing
            if l in letters:
                pass
            # else, we add it to the list of questions
            else:
                letters.append(l)

    # as no letter appears more than once,
    # the list length corresponds to the number of questions answered yes
    return len(letters)


with open("input.txt", "r") as f:
    lines = f.readlines()
    # c stands for "clean" as we get rid of the '\n' character
    clines = [l.split('\n')[0] for l in lines]
    # this operation is meant to check the last group in the condition line 35
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
