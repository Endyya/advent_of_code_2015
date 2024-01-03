import hashlib as hl

with open('input') as f:
    line = f.readline()

    cur_hash = ''
    counter_1 = 0
    while not cur_hash.startswith('00000'):
        message = bytes((line + str(counter_1)).encode())
        cur_hash = hl.md5(message).hexdigest()
        counter_1 += 1
    counter_2 = counter_1
    while not cur_hash.startswith('000000'):
        message = bytes((line + str(counter_2)).encode())
        cur_hash = hl.md5(message).hexdigest()
        counter_2 += 1

print('part 1 : ', counter_1 - 1)
print('part 2 : ', counter_2 - 1)
