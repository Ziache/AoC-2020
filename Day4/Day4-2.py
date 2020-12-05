import string


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

    # once the first condition is valid, we check the new conditions
    if res:
        # 'byr' condition
        byr = int(passport['byr'])
        res = res and (byr <= 2002 and byr >= 1920)

        # 'iyr' condition
        iyr = int(passport['iyr'])
        res = res and (iyr <= 2020 and iyr >= 2010)

        # 'eyr' condition
        eyr = int(passport['eyr'])
        res = res and (eyr <= 2030 and eyr >= 2020)

        # 'hgt' condition
        hgt = passport['hgt']
        dim = hgt[-2:]
        if (dim == 'cm'):
            ihgt = int(hgt[:-2])
            res = res and (ihgt <= 193 and ihgt >= 150)
        elif (dim == 'in'):
            ihgt = int(hgt[:-2])
            res = res and (ihgt <= 76 and ihgt >= 59)
        else:
            res = False

        # 'hcl' condition
        hcl = passport['hcl']
        if (hcl[0] == '#' and len(hcl) == 7):
            for c in hcl[1:]:
                res = res and (c in string.hexdigits)
        else:
            res = False

        # 'ecl' condition
        ecl = passport['ecl']
        eyecolors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        res = res and (ecl in eyecolors)

        # 'pid' condition (woohoo)
        pid = passport['pid']
        for c in pid:
            res = res and (c in string.digits)
        res = res and (len(pid) == 9)

        return res


with open("input.txt", "r") as f:
    lines = f.readlines()
    # c stands for "clean" as we get rid of the '\n' character
    clines = [l.split('\n')[0] for l in lines]
    # this operation is meant to check the last passport in the condition line 92
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
