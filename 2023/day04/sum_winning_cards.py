
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

count_winning_one_card = [0] * len(entries)
overall_winning_score = 0
won = False
a = len(entries)
added_cards = []

for i in range(len(entries)):
    card_nb, my_numbers, winning_numbers = separate_numbers(entries[i])
    for my_number in my_numbers:
        if my_number in winning_numbers:
            count_winning_one_card[i] = count_winning_one_card[i] + 1
            added_cards.append(card_nb - 1 + count_winning_one_card[i])
            won = True
            continue

i = 0
while i < len(added_cards):
    for j in range(count_winning_one_card[i]):
        added_cards.append(added_cards[i] + j)
        count_winning_one_card.append(count_winning_one_card[i + j - 1])
    i = i + 1

print(len(added_cards) + len(entries))
