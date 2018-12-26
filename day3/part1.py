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
    overlap = 0
    claims = [["." for x in range(1000)] for y in range(1000)]
    for coord in claimMap:
        print("claim: " + str(coord[0]))
        row = coord[1]
        col = coord[2]
        if claims[coord[1]][coord[2]] == "#":
            claims[coord[1]][coord[2]] = "X"
        if claims[coord[1]][coord[2]] == ".":
            claims[coord[1]][coord[2]] = "#"

    for row in range(1000):
        for col in range(1000):
            if claims[row][col] == "X":
                overlap +=1
    return overlap

print(compareClaims(buildClaimMap(data)))
