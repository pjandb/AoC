# Data Import

binary = []
binary2 = []
binary3 = []
with open('C:/Users/Paul/OneDrive/Code/AoC/AoC/day3/data3.txt', 'r') as file:
    for line in file.readlines():
        binary.append(line.strip())
        binary2.append(line.strip())
        binary3.append(line.strip())

# Counting Method 

def count(list, x):
    ones = 0
    zeroes = 0

    for y in list:
        if y[x] == '0':
            zeroes += 1
        elif y[x] == '1':
            ones += 1
        else:
            print("Error")
        
    if zeroes > ones:
        return('0')
    else: 
        return('1')


# CO2
while(len(binary3) > 1):
    for x in range(len(binary3[0])):
        if(count(binary3, x) == '1'):
            binary3 = [num for num in binary3 if num[x] == '0']
        elif(count(binary3, x) == '0'):
            binary3 = [num for num in binary3 if num[x] == '1']

print(binary3)

cgr = binary3[0]

print(cgr)
