with open("input.txt", "r") as f:
    data = [int(i) for i in f]

def findSecondFrequency(data):
    frequency = 0
    frequencySet = set([0])
    while True:
        for delta in data:
            frequency += delta
            if frequency in frequencySet:
                return frequency
            else:
                frequencySet.add(frequency)
    return frequency

print(findSecondFrequency(data))
