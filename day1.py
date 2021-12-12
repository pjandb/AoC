# Data Import
with open('data.txt', "r") as file:
    depths = []
    for value in file:
        value = value.strip()
        depths.append(int(value))

# Method: Size Comparison

def compare(list):
    x = 0

    counter = 0

    while(x < len(list)-1):
        if list[x+1] > list[x]:
            counter += 1
        x += 1 
    
    return counter


# Part 1 

print(compare(depths))

# Part 2
triples = []

for x in range(len(depths)-2):
    triples.append(depths[x] + depths[x+1] + depths[x+2])

print(compare(triples))