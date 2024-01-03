import numpy as np
import re

np.set_printoptions(edgeitems = 15)

def parse_line(line):
    order = re.split(r'[0-9]{1,3},[0-9]{1,3}', line)[0].strip()
    values = re.findall(r'[0-9]{1,3},[0-9]{1,3}', line)
    start_values = values[0].split(',')
    end_values = values[1].split(',')
    start_values = [int(i) for i in start_values]
    end_values = [int(i) for i in end_values]
    return order, start_values, end_values

lights_1 = np.zeros((1000, 1000))
lights_2 = np.zeros((1000, 1000))

with open('input') as f:
    line = f.readline()

    while line != '':
        order, start, end = parse_line(line)

        min_x = min(start[0], end[0])
        min_y = min(start[1], end[1])
        max_x = max(start[0], end[0])
        max_y = max(start[1], end[1])

        
        if order == 'turn on':
            lights_1[min_x:max_x + 1, min_y:max_y + 1] = 1
            lights_2[min_x:max_x + 1, min_y:max_y + 1] += 1
        elif order == 'turn off':
            lights_1[min_x:max_x + 1, min_y:max_y + 1] = 0
            lights_2[min_x:max_x + 1, min_y:max_y + 1] -= 1
            lights_2[lights_2 == -1] = 0
        elif order == 'toggle':
            lights_1[min_x:max_x + 1, min_y:max_y + 1] = (
                1 - lights_1[min_x:max_x + 1, min_y:max_y + 1])
            lights_2[min_x:max_x + 1, min_y:max_y + 1] += 2            
        else:
            raise Exception


        line = f.readline()


print('part 1 : ', int(np.sum(lights_1)))
print('part 2 : ', int(np.sum(lights_2)))
