def nbdiff(lines):
    # returns the number of differences of 1 and 3 between
    # successive numbers in a sorted list

    # first we add the first and the last output
    lines.insert(0, 0)
    l = len(lines)
    lines.append(lines[-1] + 3)

    diff1 = 0
    diff3 = 0

    for i in range(l):
        curr = lines[i]
        succ = lines[i+1]

        diff = succ - curr

        # 1-jolt difference
        if diff == 1:
            diff1 += 1

        # 3-jolt difference
        elif diff == 3:
            diff3 += 1

        # should not be reached
        else:
            pass

    return diff1, diff3


with open("input.txt", "r") as f:
    lines = f.readlines()
    clines = [l.split('\n')[0] for l in lines]
    ilines = [int(l) for l in clines]
    slines = sorted(ilines)

    d1, d3 = nbdiff(slines)
    print(d1 * d3)
