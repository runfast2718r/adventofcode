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
    overlappingClaims = []
    claims = [["." for x in range(1000)] for y in range(1000)]
    for coord in claimMap:
        row = coord[1]
        col = coord[2]
        if claims[coord[1]][coord[2]] == "#":
            claims[coord[1]][coord[2]] = "X"
        if claims[coord[1]][coord[2]] == ".":
            claims[coord[1]][coord[2]] = "#"
    p2Claims = {str(x): "Valid" for x in range(1300)}
    p2Claims.pop("0")
    for coord in claimMap:
        if p2Claims[str(coord[0])] == "Valid":
            if claims[coord[1]][coord[2]] == "X":
                p2Claims[str(coord[0])] = "Invalid"
    for claim in p2Claims:
        if p2Claims[claim] == "Valid":
            return claim
    return "Nope for some reason"

print(compareClaims(buildClaimMap(data)))
