coord = [0, 0]
for_table = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ]
roll = 1
winner = 1


def run():
    while True:
        coordinates()
        set_coord()
        rotation()
        table()
        win()
        if winner == 'X':
            print('X wins')
            input()
            break
        elif winner == 'O':
            print('O wins')
            input()
            break
        elif for_table.count(' ') == 0:
            print('Draw')
            input()
            break


def coordinates():
    global coord
    while (coord[0] != 1 or coord[0] != 2 or coord[0] != 3) \
            and (coord[1] != 1 or coord[1] != 2 or coord[1] != 3
    ):
        enter_coord = input('Enter the coordinates: ').split(' ')
        temp = []
        if len(enter_coord) == 2:
            if enter_coord[0].isdigit() and enter_coord[1].isdigit() == True:
                if 1 <= int(enter_coord[0]) <= 3:
                    enter_coord[0] = int(enter_coord[0])
                    temp.append(enter_coord[0])
                if 1 <= int(enter_coord[1]) <= 3:
                    enter_coord[1] = int(enter_coord[1])
                    temp.append(enter_coord[1])
                if len(temp) == 2:
                    coord[0], coord[1] = temp[0], temp[1]
                    temp.clear()
                    return coord
                else:
                    print("Coordinates should be from 1 to 3!")
            else:
                print("You should enter numbers!")
        else:
            print('Incorrect entry of coordinates')

def rotation():
    global roll
    roll += 1
    return roll


def set_coord():
    global coord
    a = coord[0]
    b = coord[1]
    global for_table
    global roll
    if (a == 1) and (b == 1):
        if (for_table[6] == ' '):
            if roll % 2 == 0:
                for_table[6] = 'O'
            elif roll % 2 != 0:
                for_table[6] = 'X'
        else:
            print("This cell is occupied! Choose another one!")
            run()
    if (a == 1) and (b == 2):
        if (for_table[7] == ' '):
            if roll % 2 == 0:
                for_table[7] = 'O'
            elif roll % 2 != 0:
                for_table[7] = 'X'
        else:
            print("This cell is occupied! Choose another one!")
            run()
    if (a == 1) and (b == 3):
        if (for_table[8] == ' '):
            if roll % 2 == 0:
                for_table[8] = 'O'
            elif roll % 2 != 0:
                for_table[8] = 'X'
        else:
            print("This cell is occupied! Choose another one!")
            run()
    if (a == 2) and (b == 1):
        if (for_table[3] == ' '):
            if roll % 2 == 0:
                for_table[3] = 'O'
            elif roll % 2 != 0:
                for_table[3] = 'X'
        else:
            print("This cell is occupied! Choose another one!")
            run()
    if (a == 2) and (b == 2):
        if (for_table[4] == ' '):
            if roll % 2 == 0:
                for_table[4] = 'O'
            elif roll % 2 != 0:
                for_table[4] = 'X'
        else:
            print("This cell is occupied! Choose another one!")
            run()
    if (a == 2) and (b == 3):
        if (for_table[5] == ' '):
            if roll % 2 == 0:
                for_table[5] = 'O'
            elif roll % 2 != 0:
                for_table[5] = 'X'
        else:
            print("This cell is occupied! Choose another one!")
            run()
    if (a == 3) and (b == 1):
        if (for_table[0] == ' '):
            if roll % 2 == 0:
                for_table[0] = 'O'
            elif roll % 2 != 0:
                for_table[0] = 'X'
        else:
            print("This cell is occupied! Choose another one!")
            run()
    if (a == 3) and (b == 2):
        if (for_table[1] == ' '):
            if roll % 2 == 0:
                for_table[1] = 'O'
            elif roll % 2 != 0:
                for_table[1] = 'X'
        else:
            print("This cell is occupied! Choose another one!")
            run()
    if (a == 3) and (b == 3):
        if (for_table[2] == ' '):
            if roll % 2 == 0:
                for_table[2] = 'O'
            elif roll % 2 != 0:
                for_table[2] = 'X'
        else:
            print("This cell is occupied! Choose another one!")
            run()
    return for_table


def table():
    global roll
    global for_table
    print('---------')
    print(f'| {for_table[0]} {for_table[1]} {for_table[2]} |')
    print(f'| {for_table[3]} {for_table[4]} {for_table[5]} |')
    print(f'| {for_table[6]} {for_table[7]} {for_table[8]} |')
    print('---------')
    if roll % 2 == 0:
        print('Next O')
    else:
        print('Next X')


def win():
    global winner
    if (for_table[0] + for_table[1] + for_table[2] == 'XXX') \
            or (for_table[3] + for_table[4] + for_table[5] == 'XXX') \
            or (for_table[6] + for_table[7] + for_table[8] == 'XXX') \
            or (for_table[0] + for_table[3] + for_table[6] == 'XXX') \
            or (for_table[1] + for_table[4] + for_table[7] == 'XXX') \
            or (for_table[2] + for_table[5] + for_table[8] == 'XXX') \
            or (for_table[0] + for_table[4] + for_table[8] == 'XXX') \
            or (for_table[2] + for_table[4] + for_table[6] == 'XXX'):
        winner = 'X'
        return winner
    elif (for_table[0] + for_table[1] + for_table[2] == 'OOO') \
            or (for_table[3] + for_table[4] + for_table[5] == 'OOO') \
            or (for_table[6] + for_table[7] + for_table[8] == 'OOO') \
            or (for_table[0] + for_table[3] + for_table[6] == 'OOO') \
            or (for_table[1] + for_table[4] + for_table[7] == 'OOO') \
            or (for_table[2] + for_table[5] + for_table[8] == 'OOO') \
            or (for_table[0] + for_table[4] + for_table[8] == 'OOO') \
            or (for_table[2] + for_table[4] + for_table[6] == 'OOO'):
        winner = 'O'


def tutorial():
    for_table = [ '3_1 |', '3_2 |', '3_3 |', '2_1 |', '2_2 |', '2_3 |','1_1 |', '1_2 |', '1_3 |']
    print('How to enter coordinates')
    print('-------------------')
    print(f'| {for_table[0]} {for_table[1]} {for_table[2]} ')
    print(f'| {for_table[3]} {for_table[4]} {for_table[5]} ')
    print(f'| {for_table[6]} {for_table[7]} {for_table[8]} ')
    print('-------------------')
    print("Now let's start the battle!")


tutorial()
table()
run()
