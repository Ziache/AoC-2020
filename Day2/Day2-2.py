def checkline(line):
    # checks is a password is correct

    # c stands for 'clean' : we get rid of the '\n' character
    cline = line.split("\n")[0]
    # s stands for 'split'
    sline = cline.split(" ")

    # we separate the data (no bounds anymore, these are now postions)
    poses = sline[0]
    charac = sline[1].split(':')[0]  # we want 'a' instead of 'a:'
    password = sline[2]

    # we convert the positions into integers
    sposes = poses.split("-")  # s stands for 'split'
    pos1 = int(sposes[0])
    pos2 = int(sposes[1])

    # we check the two conditions : one should be True and one should be False
    cond1 = password[pos1-1] == charac
    cond2 = password[pos2-1] == charac

    # we use '^', which is the XOR operator in python, to check the condition
    return (cond1 ^ cond2)


with open("input.txt", "r") as f:
    lines = f.readlines()

    res = 0
    for l in lines:
        if checkline(l):
            res += 1

    print(res)
