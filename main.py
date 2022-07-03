# https://www.helloworld.cc - Heft 1 - Seite 52
# Scary cave game -- Original Version CC BY-NC-SA 3.0
# Diese modifizierte Version (C) 2022 Roland Härter r.haerter@wut.de

north = {'R0': None, 'R1': None, 'R2': 'R0', 'R3': 'R1'}
south = {'R0': 'R2', 'R1': 'R3', 'R2': None, 'R3': None}
east = {'R0': 'R1', 'R1': None, 'R2': None, 'R3': None}
west = {'R0': None, 'R1': 'R0', 'R2': None, 'R3': None}

compass = {
    'go north': north,
    'go south': south,
    'go east': east,
    'go west': west
}

allowed_commands = [
    'go north', 'go south', 'go east', 'go west', 'help', 'quit'
]

description = {
    'R0': 'You are in the kitchen. Seems to be abandonned.',
    'R1': 'You are in the living room. An old armor stands in one corner.',
    'R2': 'You are in a pantry. It is cold in here.',
    'R3': 'Hallway. Here is the exit from this house.'
}


def hilfe():
    print('You may use the following commands: ', end='')
    for befehl in allowed_commands:
        print(f"'{befehl}' ", end='')
    print('')


current_room = 'R0'
final_room = 'R3'

print('	*** Welcome to Ravenswood Manor ***')
hilfe()

command = ''
while (current_room is not None):
    print(description[current_room])
    command = input('What do you want to do? ').lower()
    while command not in allowed_commands:
        command = input('No such command. What do you want to do? ').lower()
    if command == 'help':
        hilfe()
    elif command == 'quit':
        current_room = None
    elif compass[command][current_room] is not None:
        current_room = compass[command][current_room]
        if current_room == final_room:
            print(description[current_room])
            print('You found the final room. Game Over.')
            current_room = None
    else:
        print('There is no path in that direction. ', end='')
