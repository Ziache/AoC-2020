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

    # initial index and accumulator
    idx = 0
    acc = 0

    # list of already computed lines
    computed = [0 for i in range(l)]

    # while we did not reach the bottom of the file
    while(idx < l):
        # if it has already been computed, we exit of the loop
        if computed[idx]:
            break

        # otherwise we compute it
        else:
            computed[idx] = 1
            (idx, acc) = next(clines[idx], idx, acc)

    return acc


with open("input.txt", "r") as f:
    lines = f.readlines()
    clines = [l.split('\n')[0] for l in lines]

    print(compute(clines))
