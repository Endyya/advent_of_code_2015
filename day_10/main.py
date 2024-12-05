import re



def next_chunk(chunk):
    assert len(set(chunk)) == 1
    return f'{len(chunk)}{chunk[0]}'

def next_line(line):
    same_digit_regex = '1+|2+|3+'
    pattern = re.compile(same_digit_regex)
    to_return = ''
    for chunk in pattern.findall(line):
        to_return += next_chunk(chunk)
    return to_return
        
    
line = '3113322113'
for _ in range(40):
    line = next_line(line)

print('part 1 :', len(line))

for _ in range(10):
    line = next_line(line)

print('part 2 :', len(line))    



    
