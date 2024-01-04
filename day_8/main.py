import codecs

acc = 0
acc_2 = 0
with open('input', encoding = 'utf-8') as f:
    line = f.readline().rstrip()
    while line != '':
       acc += len(line)
       acc -= len(codecs.getdecoder('unicode_escape')(line[1:-1])[0])
       acc_2 += 2 + line.count('"') + line.count('\\')
       line = f.readline().rstrip()

print('part 1 :', acc)
print('part 2 :', acc_2)
