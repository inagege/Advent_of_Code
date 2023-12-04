import re


def check_is_part_number(pos_in_word: int, index_line: int, numb: str, all_lines: list[str]):
    add_before = add_after = 1
    if (pos_in_word - len(numb)) == 0:
        add_before = 0
    if pos_in_word == len(all_lines[index_line]):
        add_after = 0

    row_to_proof = []

    if index_line > 0:
        row_to_proof.append(all_lines[index_line - 1])

    if index_line < len(all_lines) - 1:
        row_to_proof.append(all_lines[index_line + 1])

    row_to_proof.append(all_lines[index_line])

    for element in row_to_proof:
        if re.search('[^0-9.]+', element[pos_in_word - len(numb) - add_before: pos_in_word + add_after]) is not None:
            return True

    return False


with open('input') as f:
    lines = f.readlines()

part_number = 0
is_part_number = False

for a in range(len(lines)):
    line = lines[a]
    line = line[:-1]
    for i in range(len(line)):
        number = ''
        while line[i].isdigit():
            number = number + line[i]
            line = line[:i] + "." + line[i+1:]
            if i + 1 < len(line):
                i = i + 1
            else:
                continue
        lines[a] = line
        if number.isdigit():
            if check_is_part_number(i, a, number, lines):
                part_number = part_number + int(number)

print(part_number)
