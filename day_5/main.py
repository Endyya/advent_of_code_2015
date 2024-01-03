def is_nice(string, part = 1):
    vowels = ['a', 'e', 'i', 'o', 'u']

    vowel_number = len(''.join(char for char in string if char in vowels))
    vowel_contains = vowel_number >= 3

    twins = [string[i] == string[i + 1] for i in range(len(string) - 1)]
    twice = any(twins)

    wrong_words = ['ab', 'cd', 'pq', 'xy']
    is_wrong = [string[i:i + 2] in wrong_words for i in range(len(string) - 1)]
    wrong = any(is_wrong)

    find_pairs = [(string[i:i + 2] in string[:i]
                   or string[i:i + 2] in string[i + 2:])
                  for i in range(len(string))]
    pair_letter = any(find_pairs)
    
    
    find_between = [string[i] == string[i + 2] for i in range(len(string) - 2)]
    between = any(find_between)
    
    if part == 1:
        return vowel_contains and twice and not wrong
    elif part == 2:
        return pair_letter and between
    else:
        raise Exception

count_1 = 0
count_2 = 0
with open('input') as f:
    line = f.readline()

    while line != '':

        if is_nice(line, part = 1):
            count_1 += 1
        if is_nice(line, part = 2):
            count_2 += 1


        line = f.readline()


print('part 1 : ', count_1)
print('part 2 : ', count_2)
