import re


def calculate_all_possible_wins(_time: int, _distance: int):
    possible_win = 0
    for j in range(_time):
        d = (_time - j) * j
        if d > _distance:
            possible_win = possible_win + 1
    return possible_win


with open('input') as f:
    lines = f.readlines()

matched_numbers = []

for line in lines:
    matched_numbers.append(re.findall(r'\d+', line))

all_wins_multiplied = 1
time = ''
distance = ''

for i in range(len(matched_numbers[0])):
    time = time + matched_numbers[0][i]
    distance = distance + matched_numbers[1][i]
all_wins_multiplied = all_wins_multiplied * calculate_all_possible_wins(int(time), int(distance))

print(all_wins_multiplied)