paper_surf = 0
ribbon_len = 0

with open('input') as f:
    line = f.readline()

    while line != '':
        l, w, h = line.split('x')
        l, w, h = int(l), int(w), int(h)
        sides_surf = [l * w, l * h, w * h]

        # part 1
        paper_surf += 2 * sum(sides_surf) + min(sides_surf)

        # part 2
        sides = [l, w, h]
        min_1 = min(sides)
        sides.pop(sides.index(min_1))
        min_2 = min(sides)

        bow = l * w * h

        ribbon_len += bow + 2 * (min_1 + min_2)
        
        

        line = f.readline()

print('part 1 : ', paper_surf)
print('part 2 : ', ribbon_len)
