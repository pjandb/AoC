# Data Import
positions = []
with open('C:/Users/Paul/OneDrive/Code/AoC/AoC/day2/data2.txt', 'r') as file:
    for x in file.read().splitlines():
        positions.append(x.split())

# Part 1
depth = 0
position = 0

for x in positions:
    if x[0] == 'forward':
        position += int(x[1])
    elif x[0] == 'down':
        depth += int(x[1])
    else:
        depth -= int(x[1])

print(depth*position)

# Part 2
aim = 0
depth2 = 0
position2 = 0

for y in positions: 
    if y[0] == 'forward':
        position2 += int(y[1])
        depth2 += aim * int(y[1])
    elif y[0] == 'down':
        aim += int(y[1])
    elif y[0] == 'up':
        aim -= int(y[1])
    else:
        print('Error Roger Over')

print(depth2*position2)