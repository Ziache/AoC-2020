def clean(line):
    # cleans a line.
    # Example :
    # (in1)  'light gold bags contain 2 light lime bags,
    #         1 faded green bag, 3 clear olive bags, 2 dim bronze bags'
    #
    # (out1) ['light gold', 'light lime', 2, 'faded green', 1,
    #         'clear olive', 3, 'dim bronze', 2]
    #
    # (in2)  'clear brown bags contain no other bags'
    #
    # (out1) ['clear brown']

    # c stands for "clean" as we get rid of the '\n' character, and the dot
    cline1 = line.split('.\n')[0]
    # now we get rid of the "contain" word
    cline2 = cline1.split(' contain ')

    # now we get rid of the 'bags' word in the first entry...
    cline31 = [(cline2[0].split(' bags'))[0]]
    # ... and of the ', ' in the other entries
    cline32 = cline2[1].split(', ')

    if 'no other' in cline32[0]:
        return cline31

    # now we get rid of the word 'bag(s)' in the second entries
    cline42 = [ent.split(' bag')[0] for ent in cline32]

    # now we rearrange the numbers and the colors
    cline52 = [[ent[2:], int(ent[0])] for ent in cline42]

    # finally we flatten the list
    cline62 = [it for ent in cline52 for it in ent]

    return cline31 + cline62


def colorlist(clines):
    # returns all the possible bag colors
    return [l[0] for l in clines]


def gor(boollist):
    # returns a generalized 'or' of a list of boolean propositions

    res = False
    for b in boollist:
        res = res or b

    return res


def createinclusiondict(clines):
    # creates the initial dictionary of inclusion, in which
    # the keys are the colors and the values are -1

    incdict = {}
    colors = colorlist(clines)

    for c in colors:
        incdict[c] = -1

    return incdict


def lsuccessors(cline):
    # returns the list of the 'successor' colors of a line

    l = len(cline)
    return [cline[2*i+1] for i in range(l//2)]


def color2line(clines, color):
    # returns the line corresponding to the color
    for l in clines:
        if l[0] == color:
            return l


def computeoneinclusion(incdict, clines, color, target):
    # computes one step of the computeinclusion function.
    # 'target' is the color we want to be included, whereas
    # 'color' is the key we want the value to be computed.

    cline = color2line(clines, color)
    l = len(cline)

    # if this is a 'final' bag color (contains no other bag),
    # our target bag is not included in the current bag
    if l == 1:
        incdict[color] = 0
        return incdict
    # else
    else:
        # we look for the successors
        succ = lsuccessors(cline)

        # we check is our target is a direct successor
        # if so, our target bag is included in the current bag
        if target in succ:
            incdict[color] = 1
            return incdict

        else:
            # we check if all the successors' values have been computed
            undefined = [incdict[col] == -1 for col in succ]

            # if at least one successor's value is not computed yet
            if gor(undefined):
                # we compute all the successors' values
                for c in succ:
                    # if it has not been computed yet, we call the function again
                    if incdict[c] == -1:
                        incdict = computeoneinclusion(
                            incdict, clines, c, target)
                    # else, we do nothing
                    else:
                        pass

            # at that point, all the successors' values have been computed.
            # if at least one successor has a value of 1, the result is 1 as well.
            valsucc = [incdict[col] for col in succ]
            incdict[color] = gor(valsucc)
            return incdict


def computeinclusion(clines, color):
    # fills the dictionary of inclusion.
    # incdict[color] = 1 if the bag contained the 'color' bag
    # incdict[color] = 0 if it doesn't

    colors = colorlist(clines)
    incdict = createinclusiondict(clines)

    # for each color
    for col in colors:
        # if its value is not computed yet, we compute it
        if incdict[col] == -1:
            incdict = computeoneinclusion(incdict, clines, col, color)
        # else, we do nothing
        else:
            pass

    return incdict


def bigsum(ilist):
    # returns the sum of an int list's elements.
    # (this function may already exist, idk)

    res = 0
    for i in ilist:
        res += i

    return res


with open("input.txt", "r") as f:
    lines = f.readlines()

    clines = [clean(l) for l in lines]

    incdict = computeinclusion(clines, 'shiny gold')

    print(bigsum(incdict.values()))
