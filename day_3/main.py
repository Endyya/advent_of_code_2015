

cur_pos = [0, 0]
houses_delivered = {'[0, 0]': 1}

cur_pos_santa = [0, 0]
cur_pos_bot = [0, 0]
houses_del_2 = {'[0, 0]': 2}

santa_turn = True

def update_pos(pos, order):
    if order == '>':
        pos[0] += 1
    elif order == '<':
        pos[0] -= 1
    elif order == 'v':
        pos[1] -= 1
    elif order == '^':
        pos[1] += 1
    else:
        raise Exception

    return pos

with open('input') as f:
    line = f.readline()

while len(line) > 0:
    cur_move = line[0]

    # part 1
    cur_pos = update_pos(cur_pos, cur_move)

    if str(cur_pos) in houses_delivered.keys():
        houses_delivered[str(cur_pos)] += 1
    else:
        houses_delivered[str(cur_pos)] = 0

    # part 2
    if santa_turn:
        cur_pos_santa = update_pos(cur_pos_santa, cur_move)
        if str(cur_pos_santa) in houses_del_2.keys():
            houses_del_2[str(cur_pos_santa)] += 1
        else:
            houses_del_2[str(cur_pos_santa)] = 0
    else:
        cur_pos_bot = update_pos(cur_pos_bot, cur_move)
        if str(cur_pos_bot) in houses_del_2.keys():
            houses_del_2[str(cur_pos_bot)] += 1
        else:
            houses_del_2[str(cur_pos_bot)] = 0        
    santa_turn = not santa_turn
    

    line = line[1:]


print('part 1 : ', len(houses_delivered.keys()))
print('part 2 : ', len(houses_del_2.keys()))
