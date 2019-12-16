import math

with open("input.txt", "r") as f:
    data = [int(i) for i in f]

def getFuel(modules):
    totalFuel = 0
    for module in modules:
        amt = math.floor(module / 3) - 2
        if amt >= 0:
            totalFuel += amt + recursiveFuel(amt)
    return totalFuel

def recursiveFuel(fuel):
    recAmt = 0
    amt = 0
    amt = math.floor(fuel / 3) - 2
    if amt > 0:
        recAmt = recursiveFuel(amt)
    return amt + recAmt

print(getFuel(data))
