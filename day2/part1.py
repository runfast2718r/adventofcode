with open('input.txt', 'r') as f:
    data = [i for i in f]

def getCheckSum(data):
    twice = 0
    thrice = 0
    for id in data:
        counts = {}
        fullID = ''
        for s in id:
            fullID += s
            if s in counts:
                counts[str(s)] += 1
            else:
                counts[str(s)] = 1
        print(counts)
        twiceBool = False
        thriceBool = False
        for c in counts:
            if counts[c] == 2:
                twiceBool = True
            elif counts[c] == 3:
                thriceBool = True
        print(str(twiceBool) + " " + str(thriceBool))
        if twiceBool:
            twice += 1
        if thriceBool:
            thrice +=1
        print(str(twice) + " " + str(thrice))
    return twice * thrice

print(getCheckSum(data))
