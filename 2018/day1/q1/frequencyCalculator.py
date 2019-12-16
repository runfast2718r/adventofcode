data = open("input.txt", "r")

frequency = 0;
for line in data:
    operator = line[0];
    change = line[1:-1];
    if operator == '+':
        frequency = frequency + int(change)
    elif operator == '-':
        frequency = frequency - int(change)
    else:
        print("error")
        break
    print(frequency)
print(frequency)
