def convert_string_to_numbers(string: str):
    numbers = {
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'}

    for index, number in numbers.items():
        found = True
        while found:
            try:
                string.index(number)
            except:
                found = False
                continue

            string = string[:string.find(number) + 2] + index + string[string.find(number) + 2:]

    return string


with open('input') as file:
    entries = file.readlines()

summed = 0

for entry in entries:
    digits = []
    entry = convert_string_to_numbers(entry)
    for i in range(0, len(entry)):
        if entry[i].isdigit():
            digits.append(entry[i])
    summed = summed + int(digits[0] + digits[len(digits)-1])

print(summed)
