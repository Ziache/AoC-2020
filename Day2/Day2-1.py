def countLetters(charac, password):
    # counts the number of occurrences of the character 'charac' in the string 'password'
    res = 0
    for i in password:
        if (i == charac):
            res += 1
    return res


def checkline(line):
    # checks is a password is correct

    # c stands for 'clean' : we get rid of the '\n' character
    cline = line.split("\n")[0]
    # s stands for 'split'
    sline = cline.split(" ")

    # we separate the data
    bounds = sline[0]
    charac = sline[1].split(':')[0]  # we want 'a' instead of 'a:'
    password = sline[2]

    # we convert the bound into integers
    sbounds = bounds.split("-")  # s stands for 'split'
    l_bound = int(sbounds[0])
    h_bound = int(sbounds[1])

    nbOccur = countLetters(charac, password)

    # we check the condition
    return ((l_bound <= nbOccur) and (nbOccur <= h_bound))


with open("input.txt", "r") as f:
    lines = f.readlines()

    res = 0
    for l in lines:
        if checkline(l):
            res += 1

    print(res)
