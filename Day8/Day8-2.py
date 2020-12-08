def val(insval):
    # returns the integer conversion of an instruction

    sign = insval[0] == '+'
    intval = int(insval[1:])

    # this expression is equal to intval if 'sign' is positive,
    # and -intval if 'sign' is negative
    res = 2*sign*intval - intval

    return res


def next(line, iline, acc):
    # returns the number of the line which has to be executed next,
    # and the value of 'acc'.
    #
    # 'line' is the current line
    # 'iline' is the index of the current line
    # 'acc' is the value of the accumulator

    # we separate the two different parts of the instruction
    inst = line.split(' ')
    insname = inst[0]
    insval = inst[1]

    # 'nop' case
    if insname == 'nop':
        return (iline+1, acc)

    # 'acc' case
    elif insname == 'acc':
        acc += val(insval)
        return (iline+1, acc)

    # 'jmp' case
    elif insname == 'jmp':
        iline += val(insval)
        return (iline, acc)

    # This should not be reached
    else:
        return (iline, acc)


def compute(clines):
    # computes the whole file

    l = len(clines)

    terminated = True

    # initial index and accumulator
    idx = 0
    acc = 0

    # list of already computed lines
    computed = [0 for i in range(l)]

    # while we did not reach the bottom of the file
    while(idx < l):
        # if it has already been computed, we exit of the loop
        if computed[idx]:
            # we indicate the execution has ended abnormally
            terminated = False
            break

        # otherwise we compute it
        else:
            computed[idx] = 1
            (idx, acc) = next(clines[idx], idx, acc)

    return acc, terminated


def debug(clines):
    # fixes the corruption issue in the file by trying to replace each
    # possible mistake

    l = len(clines)

    # for each line
    for i in range(l):

        # we create a copy of the original clines
        flines = clines.copy()
        line = clines[i].split(' ')

        # if there is a 'nop' operation, we replace it with a 'jmp'
        if line[0] == 'nop':
            nline = 'jmp' + ' ' + line[1]
            flines[i] = nline

        # if there is a 'jmp' operation, we replace it with a 'nop'
        elif line[0] == 'jmp':
            nline = 'nop' + ' ' + line[1]
            flines[i] = nline

        # else, we do not change anything
        else:
            pass

        # then we compute as usual, with the replaced line
        acc, ter = compute(flines)

        if ter:
            return acc


with open("input.txt", "r") as f:
    lines = f.readlines()
    clines = [l.split('\n')[0] for l in lines]

    print(debug(clines))
