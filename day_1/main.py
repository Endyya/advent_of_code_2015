with open('input') as f:
    line = f.readline()

floor = line.count('(') - line.count(')')
print('part 1 : ', floor)

floor = 0
count = 0
while floor >= 0:
    if line[0] == '(':
        floor += 1
    elif line[0] == ')':
        floor -= 1
    line = line[1:]
    count += 1

print('part 2 : ', count)

    
