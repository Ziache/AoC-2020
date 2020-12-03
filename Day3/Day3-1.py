def nextij(i, j, grid, di, dj):
    # computes the next step's coordinates

    nj = len(grid[0])

    # we go back to the left of the grid once we've reached the right bound
    return (i + di, (j + dj) % nj)


def count(i0, j0, grid, di=1, dj=3, tree='#'):
    # counts the trees encountered. We put default parameters in case the (1,3) movement changes

    (i, j) = (i0, j0)
    ni = len(grid)

    res = 0

    # now let's explore the grid
    while (i < ni-1):
        (i, j) = nextij(i, j, grid, di, dj)
        if (grid[i][j] == tree):
            res += 1

    return res


with open("input.txt", "r") as f:
    lines = f.readlines()

    # c stands for "clean" as we get rid of the '\n' character
    clines = [l.split('\n')[0] for l in lines]
    (i0, j0) = (0, 0)

    res = count(i0, j0, clines)

    print(res)
