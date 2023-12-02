
with open('input.txt') as file:
    entries = file.readlines()

colors = ['green', 'red', 'blue']
# number_of_games_valid = 0
power = 0

for all_games in entries:
    games_without_des = all_games.split(':')
    game_id = int(games_without_des[0].split(' ')[1])
    games_without_des = games_without_des[1].split(';')
    valid = True
    minimum_values = dict()
    minimum_values['green'] = 0
    minimum_values['red'] = 0
    minimum_values['blue'] = 0

    for game in games_without_des:
        gems_grabbed = game.split(',')
        for gems in gems_grabbed:
            for color in colors:
                if gems.find(color) > -1: # and valid:
                    # if ((color == 'green' and int(gems.split(' ')[1]) > 13)
                            # or (color == 'red' and int(gems.split(' ')[1]) > 12)
                            # or (color == 'blue' and int(gems.split(' ')[1]) > 14)):
                        # valid = False
                    if minimum_values[color] < int(gems.split(' ')[1]):
                        minimum_values[color] = int(gems.split(' ')[1])

    # if valid:
        # number_of_games_valid = number_of_games_valid + game_id
    power = power + minimum_values['green'] * minimum_values['red'] * minimum_values['blue']


print(str(power))
