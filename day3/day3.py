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


# PART 1

gamma = ''


for x in range(len(binary[0])):
    gamma += count(binary, x)


# Reverse Gamma
epsilon = ''.join('10'[int(c)] if c in '01' else c for c in gamma)


# Binary to Decimal
def binaryToDecimal(n):
    return int(n,2)

gamma_decimal = binaryToDecimal(gamma)
epsilon_decimal = binaryToDecimal(epsilon)

powerConsumption = gamma_decimal * epsilon_decimal

print(powerConsumption)


# PART 2
# Oxygen
for x in range(len(binary2[0])):
    if(count(binary2, x) == '0'):
        binary2 = [num for num in binary2 if num[x] == '0']
    elif(count(binary2, x) == '1'):
        binary2 = [num for num in binary2 if num[x] == '1']
    if(len(binary2) == 1):
        break

print(binary2)

ogr = binary2[0]

print(ogr)

print(binaryToDecimal(ogr))

# CO2
for x in range(len(binary3[0])):
    if(count(binary3, x) == '1'):
        print("hallo" , binary3)
        binary3 = [num for num in binary3 if num[x] == '0']
    elif(count(binary3, x) == '0'):
        print("tschüss", binary3)
        binary3 = [num for num in binary3 if num[x] == '1']
    if(len(binary3) == 1):
        break

print(binary3)

cgr = binary3[0]

print(cgr)

print(binaryToDecimal(cgr))

print(binaryToDecimal(ogr) * binaryToDecimal(cgr))