def createPassport(lines):
    # creates a passport using the dictionary format

    passport = {}

    for l in lines:
        line = l.split(' ')

        for it in line:
            # kv stands for 'key - value'
            kv = it.split(':')
            passport[kv[0]] = kv[1]
    return passport


def checkPassport(passport, params):
    # returns True if the passport is valid
    res = True

    for k in params:
        # we check if each of the mandatory keys is present
        res = res and (k in passport.keys())

    return res


with open("input.txt", "r") as f:
    lines = f.readlines()
    # c stands for "clean" as we get rid of the '\n' character
    clines = [l.split('\n')[0] for l in lines]
    # this operation is meant to check the last passport in the condition line 41
    clines.append('')

    ilines = []
    params = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    res = 0

    for l in clines:
        # case in which there are no more lines to describe the current passport
        if (l == ''):
            # we create the passport and then check it
            passport = createPassport(ilines)
            if checkPassport(passport, params):
                res += 1

            # reset the passport's lines
            ilines = []

        # case in which the current line still describes the same passport
        else:
            ilines.append(l)

    print(res)
