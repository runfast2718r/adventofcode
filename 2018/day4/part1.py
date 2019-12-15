import re

with open("input.txt", "r") as f:
    data = [i for i in f]

days = {}
for line in data:
    date = line[6:11]
    if line[12:14] == "23":
        time = "00"
        date = 
    else:
        time = line[15:17]
    action = line[19:]
    if action[0:5] == "Guard":
        num = re.compile("#\\d{3,4} ").search(action)[0][1:]
        days[date] = [num, ["." for i in range(60)],{}]
print(days['04-25'])
for line in data:
    date = line[6:11]
    if line[12:14] == "23":
        time = "00"
    else:
        time = line[15:17]
    action = line[19:]

    days[date][2][time] = [action,time]


print(days['11-01'])
