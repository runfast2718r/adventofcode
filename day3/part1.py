with open("input.txt", "r") as f:
    data = [i for i in f]

def buildClaimMap(data):
    claimMap = []
    claimNum = 0
    for line in data:
        claimNum += 1
        claim = []
        stuff = line.split('@ ')[1].split(": ")
        coords = stuff[0].split(",")
        dimensions = stuff[1].split("x")
        x = int(coords[0])
        y = int(coords[1])
        w = int(dimensions[0])
        h = int(dimensions[1])
        for i in range(h):
            for j in range(w):
                claimMap.append([claimNum, x+j, y+i])

    return claimMap
def compareClaims(claimMap):
    overlapCount = 0

    for coord in claimMap:
        for compCoord in claimMap:
            if coord[0] != compCoord[0]:
                if coord[1] == compCoord[1] and coord[2] == compCoord[2]:
                    overlapCount+=1
        # for j in range(len(claimMap)):
        #     claim = claimMap[i]
        #     compClaim = claimMap[j]
        #     if(i != j):
        #         for coord in claim:
        #             for compCoord in compClaim:
        #                 if coord[0] == compCoord[0] and coord[1] == compCoord[1]:
        #                     overlapCount += 1
        print(overlapCount)
# print(compareClaims(buildClaimMap(data)))
print(compareClaims(buildClaimMap(data)))

# TODO: make overlapCount a dict and add coord to that. if the value is in the dict, don't put it in. return len(dict)
