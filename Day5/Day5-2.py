def missingel(slist):
    # returns the missing element of a sorted list

    # considering mini and maxi variables, we fix the "front and back seats" issue
    mini = slist[0]
    maxi = slist[-1]

    for i in range(mini, maxi):
        if not (i in slist):
            return i

    # this should not be reached
    return(-1)


def getid(board):
    # returns a boarding pass's id

    # we separate the two components
    row = board[:-3]
    col = board[-3:]

    # we replace the letters with binary digits
    row = row.replace('F', '0')
    row = row.replace('B', '1')
    col = col.replace('L', '0')
    col = col.replace('R', '1')

    # now we simply convert them
    irow = int(row, 2)
    icol = int(col, 2)

    return(8*irow + icol)


with open("input.txt", "r") as f:
    lines = f.readlines()
    # c stands for "clean" as we get rid of the '\n' character
    clines = [l.split('\n')[0] for l in lines]

    # we build the list of the ids and then we sort it
    id = [getid(l) for l in clines]
    sortedid = sorted(id)

    print(missingel(sortedid))
