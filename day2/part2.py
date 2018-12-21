with open('input.txt', 'r') as f:
    data = [i for i in f]

def findRightBoxes(data):
    for id in data:
        for compID in data:
            diffCharCount = 0
            for x in range(len(id)):
                if (id[x] != compID[x]):
                    diffCharCount += 1
            if(diffCharCount == 1):
                return id + " " + compID

print(findRightBoxes(data))
