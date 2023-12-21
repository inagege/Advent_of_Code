def separate_numbers(line):
    line = line.split(':')
    card_number = line[0].split(' ')
    card_number = card_number[len(card_number)-1]
    numbers = line[1].split('|')
    for i in range(len(numbers)):
        numbers[i] = numbers[i].split(' ')
        for a in range(len(numbers[i])):
            try:
                numbers[i].remove('')
            except:
                continue
    numbers[1][len(numbers[1])-1] = numbers[1][len(numbers[1])-1][:-1]
    return int(card_number), numbers[0], numbers[1]


with open('input') as f:
    entries = f.readlines()

count_winning_one_card = 0
overall_winning_score = 0
won = False
i = 0

while i < len(entries):
    card_nb, my_numbers, winning_numbers = separate_numbers(entries[i])
    for my_number in my_numbers:
        if my_number in winning_numbers:
            count_winning_one_card = count_winning_one_card + 1
            entries.append(entries[card_nb - 1 + count_winning_one_card])
            won = True
            continue

    if won:
        overall_winning_score = overall_winning_score + pow(2, count_winning_one_card - 1)
        count_winning_one_card = 0
        won = False
    print(i)
    i = i + 1

print(overall_winning_score)
