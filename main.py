import random

board1 = ['_' for x in range(0, 100)]
board2 = ['_' for z in range(0, 100)]

clean_board = ['_' for y in range(0, 100)]
hidden_board = ['_' for c in range(0, 100)]

list_coord_1 = list(range(0, 100))
list_coord_2 = list(range(0, 100))

ship_list1 = []
ship_list2 = []

attack_coords = list(range(0, 100))


targets_1 = list()
targets_2 = list()
orient = 0

gamemode = int(input('0 for manual, 1 for comp game :'))



# def ship_perimeter(size, orient, coord, board, sym, sym2):
#     """placing the ship and surrounding symbols on the board using given values"""
#
#
#     if orient == 0:
#         board[coord:coord + size] = sym2 * size
#
#         if coord > 10:  # check up
#             board[coord - 10: coord - 10 + size] = sym * size
#         if coord < 90:  # check down
#             board[coord + 10: coord + 10 + size] = sym * size
#         if coord % 10 != 0:  # check left
#             board[coord - 1] = sym
#             if board[coord - 1] == sym:  # check left and:
#                 if board[coord - 10] == sym:  # check up
#                     board[coord - 11] = sym
#                 if coord < 90 and board[coord + 10] == sym:  # fix out of line problem
#                     board[coord + 9] = sym
#         if (coord + size) % 10 != 0:  # check right
#             board[coord + size] = sym
#             if coord + size < 100 and board[coord + size] == sym:  # fix out of line problem
#                 if board[coord + size - 11] == sym:
#                     board[coord + size - 10] = sym
#                 if coord + size < 90 and board[coord + size + 9] == sym:  # fix out of line problem
#                     board[coord + size + 10] = sym
#
#     if orient == 1:
#         board[coord:coord + (size * 10):10] = sym * size
#         if coord % 10 != 0:  # check left
#             board[coord - 1:coord + (size * 10) - 1:10] = sym * size
#         if coord % 10 != 9:  # check right
#             board[coord + 1:coord + (size * 10) + 1:10] = sym * size
#         if coord > 10:  # check up
#             board[coord - 10] = sym
#         if coord + (size * 10) - 10 < 90:  # check down
#             board[coord + (size * 10)] = sym
#         if board[coord - 10] == sym:  # check up and
#             if board[coord - 1] == sym and coord % 10 != 0:
#                 board[coord - 11] = sym
#             if board[coord + 1] == sym and coord % 10 != 9:
#                 board[coord - 9] = sym
#         if coord + (size * 10) < 100 and board[coord + (size * 10)] == sym:  # check down and:. fix out of line problem
#             if board[coord - 1] == sym and coord % 10 != 0:
#                 board[coord + (size * 10) - 1] = sym
#             if board[coord + 1] == sym and coord % 10 != 9:
#                 board[coord + (size * 10) + 1] = sym
#
#     if sym == '*':
#         list_of_value = [orient, size, coord]
#         if board == board2:
#             ship_list2.append(list_of_value)
#         else:
#             ship_list1.append(list_of_value)


def battleship(size, orient, coord, board):
    """placing the ship and surrounding symbols on the board using given values"""

    if orient == 0:
        board[coord:coord + size] = 'S' * size

        if coord > 10:  # check up
            board[coord - 10: coord - 10 + size] = '*' * size
        if coord < 90:  # check down
            board[coord + 10: coord + 10 + size] = '*' * size
        if coord % 10 != 0:  # check left
            board[coord - 1] = '*'
            if board[coord - 1] == '*':  # check left and:
                if board[coord - 10] == '*':  # check up
                    board[coord - 11] = '*'
                if coord < 90 and board[coord + 10] == '*':  # fix out of line problem
                    board[coord + 9] = '*'
        if (coord + size) % 10 != 0:  # check right
            board[coord + size] = '*'
            if coord + size < 100 and board[coord + size] == '*':  # fix out of line problem
                if board[coord + size - 11] == '*':
                    board[coord + size - 10] = '*'
                if coord + size < 90 and board[coord + size + 9] == '*':  # fix out of line problem
                    board[coord + size + 10] = '*'

    if orient == 1:
        board[coord:coord + (size * 10):10] = 'S' * size
        if coord % 10 != 0:  # check left
            board[coord - 1:coord + (size * 10) - 1:10] = '*' * size
        if coord % 10 != 9:  # check right
            board[coord + 1:coord + (size * 10) + 1:10] = '*' * size
        if coord > 10:  # check up
            board[coord - 10] = '*'
        if coord + (size * 10) - 10 < 90:  # check down
            board[coord + (size * 10)] = '*'
        if board[coord - 10] == '*':  # check up and
            if board[coord - 1] == '*' and coord % 10 != 0:
                board[coord - 11] = '*'
            if board[coord + 1] == '*' and coord % 10 != 9:
                board[coord - 9] = '*'
        if coord + (size * 10) < 100 and board[coord + (size * 10)] == '*':  # check down and:. fix out of line problem
            if board[coord - 1] == '*' and coord % 10 != 0:
                board[coord + (size * 10) - 1] = '*'
            if board[coord + 1] == '*' and coord % 10 != 9:
                board[coord + (size * 10) + 1] = '*'

    list_of_value = [orient, size, coord]
    if board == board2:
        ship_list2.append(list_of_value)
    else:
        ship_list1.append(list_of_value)


def gameboard(board, board2):
    """draw two gameboards"""

    print('   0  1  2  3  4  5  6  7  8  9      0  1  2  3  4  5  6  7  8  9')
    print('0', end='  ')
    counter = 1
    counter2 = 0
    for x in board:

        if counter % 10 == 0:
            print(x, end='')
            print('   ', end='')
            for z in board2[counter2:counter2 + 10]:
                if counter2 % 10 == 0:
                    print(int(counter2 / 10), end='  ')
                print(z, end='  ')
                counter2 += 1
            print('')
            if counter < 91:
                print(int(counter / 10), end='  ')

        else:
            print(x, end='  ')

        counter += 1


def cleanboard(board, cleanboard):
    """make a gameboard look cleaner"""
    counter = 0
    for x in board:
        if counter < 100:
            if x == '*' or x == '_':
                cleanboard[counter] = ' '
            elif x == '#':
                cleanboard[counter] = '.'
            else:
                cleanboard[counter] = x

        counter += 1


def hiddenboard(board, hiddenboard):
    """hide the ships on board from player"""
    counter = 0
    for x in board:
        if counter < 100:
            if x == '*' or x == '_' or x == 'S':
                hiddenboard[counter] = '.'

            else:
                hiddenboard[counter] = x

        counter += 1


def user_choice(board):
    """user choose size, orientation and coordinates of the ship. Then values goes to battleship for placing"""

    orient = int(input('choose ship orientation. 0 for horizontal, 1 for vertical: '))
    while orient not in range(0, 2):
        orient = int(input('choose CORRECT ship orientation. 0 for horizontal, 1 for vertical: '))
    size = int(input('choose the size of your ship: '))
    while size not in range(1, 5):
        size = int(input('choose the CORRECT size of your ship: '))
    coord = int(input('choose the square for your ship: '))
    if orient == 0:
        while (coord % 10) + size > 10 or board[coord:coord + size] != list('_' * size):
            coord = int(input('choose the CORRECT square for your ship: '))

    elif orient == 1:
        while coord + (size * 10) >= 110 or board[coord:coord + (size * 10):10] != list('_' * size):
            coord = int(input('choose the CORRECT square for your ship: '))

    battleship(size, orient, coord, board)  # size, orient, coord, board


def comp_choice(size, board):
    """comp choose size, orientation and coordinates of the ship. Then values goes to battleship for placing"""
    list_coord = 0
    board = board
    if board == board1:
        list_coord = list_coord_1
    elif board == board2:
        list_coord = list_coord_2

    orient = random.randint(0, 1)

    if orient == 0:
        coord = random.choice(list_coord)

        while (coord % 10) + size > 10 or board[coord:coord + size] != list(
                '_' * size):  # check if ship is not out of field and it placed on empty fields
            coord = random.choice(list_coord)
        battleship(size, orient, coord, board)  # size, orient, coord, board
        # list_coord.remove(coord)
    elif orient == 1:
        coord = random.choice(list_coord)
        while coord + (size * 10) > 100 or board[coord:coord + (size * 10):10] != list(
                '_' * size):  # check if ship is not out of field and it placed on empty fields
            coord = random.choice(list_coord)
        battleship(size, orient, coord, board)  # size, orient, coord, board
        list_coord.remove(coord)

    # print('orientation - ', orient, 'size - ', size, 'coord - ', coord)


def ship_placing(board):
    """automatically places 10 ships of different sizes on board"""
    board = board
    count = 0

    while count < 10:

        if count == 0:
            comp_choice(4, board)

        elif count < 3:
            comp_choice(3, board)

        elif count < 6:
            comp_choice(2, board)

        elif count < 10:
            comp_choice(1, board)

        count += 1


def user_attack(board):
    """user makes his move. if ship on the given coordinate - ship  cell turns to 'D' """
    attack_coord = int(input('choose the field for the attack: '))

    while attack_coord not in range(0, 100) or board[attack_coord] in ['D', 'X', '#']:
        attack_coord = int(input('choose the CORRECT field for the attack: '))

    if board[attack_coord] == 'S':
        board[attack_coord] = 'D'
        print('you hit the target!')
    else:
        board[attack_coord] = '#'


def comp_attack(board, targets):
    """comp randomly choose the square for the attack, rechoose if it doesnt pass the conditions. send value to shoot_conditions"""
    attack_coord = random.choice(attack_coords)

    while board[attack_coord] in ['D', 'X', '#']:
        attack_coord = random.choice(attack_coords)

    if targets:
        attack_coord = random.choice(targets)
        targets.remove(attack_coord)

    shoot_conditions(board, attack_coord, targets)


def shoot_conditions(board, attack_coord, targets):

    """checks if shot hits the ship, print the shooting coordinates"""
    if board[attack_coord] == 'S':
        board[attack_coord] = 'D'

        if board[attack_coord - 1] == 'S':
            targets.append(attack_coord - 1)
        if attack_coord < 99 and board[attack_coord + 1] == 'S':
            targets.append(attack_coord + 1)
        if board[attack_coord - 10] == 'S':
            targets.append(attack_coord - 10)
        if attack_coord < 90 and board[attack_coord + 10] == 'S':
            targets.append(attack_coord + 10)

    else:
        board[attack_coord] = '#'



    if gamemode == 1:
        if board == board1:
            print('Comp 1 shoot at the coordinate', attack_coord, end='.')
            if board[attack_coord] == 'D':
                print(' Hit!')
            else:
                print(' Miss!')
        else:
            print('Comp 2 shoot at the coordinate', attack_coord, end='.')
            if board[attack_coord] == 'D':
                print(' Hit!')
            else:
                print(' Miss!')
    else:
        print('Computer shoot at the coordinate', attack_coord, end='.')
        if board[attack_coord] == 'D':
            print(' Hit!')
        else:
            print(' Miss!')

def ship_status(board, ship_list):
    """check if all ship squares are damaged, then replace it with X squares """
    size = 0
    orient = 0
    coord = 0

    for ship in ship_list:
        for ind, value in enumerate(ship):
            if ind == 0:
                orient = value
            if ind == 1:
                size = value

            if ind == 2:
                coord = value

                if orient == 0:
                    if board[coord: coord + size] == list('D' * size):
                        board[coord: coord + size] = list('X' * size)
                        print('ship on coordinates', coord, ' destroyed!')

                        if coord > 10:  # check up
                            board[coord - 10: coord - 10 + size] = '#' * size
                        if coord < 90:  # check down
                            board[coord + 10: coord + 10 + size] = '#' * size
                        if coord % 10 != 0:  # check left
                            board[coord - 1] = '#'
                            if board[coord - 1] == '#':  # check left and:
                                if board[coord - 10] == '#':  # check up
                                    board[coord - 11] = '#'
                                if coord < 90 and board[coord + 10] == '#':  # fix out of line problem
                                    board[coord + 9] = '#'
                        if (coord + size) % 10 != 0:  # check right
                            board[coord + size] = '#'
                            if coord + size < 100 and board[coord + size] == '#':  # fix out of line problem
                                if board[coord + size - 11] == '#':
                                    board[coord + size - 10] = '#'
                                if coord + size < 90 and board[coord + size + 9] == '#':  # fix out of line problem
                                    board[coord + size + 10] = '#'
                if orient == 1:
                    if board[coord:coord + (size * 10):10] == list('D' * size):
                        board[coord:coord + (size * 10):10] = list('X' * size)
                        print('ship on coordinates', coord, ' destroyed!')

                        if coord % 10 != 0:  # check left
                            board[coord - 1:coord + (size * 10) - 1:10] = '#' * size
                        if coord % 10 != 9:  # check right
                            board[coord + 1:coord + (size * 10) + 1:10] = '#' * size
                        if coord > 10:  # check up
                            board[coord - 10] = '#'
                        if coord + (size * 10) - 10 < 90:  # check down
                            board[coord + (size * 10)] = '#'
                        if board[coord - 10] == '#':  # check up and
                            if board[coord - 1] == '#' and coord % 10 != 0:
                                board[coord - 11] = '#'
                            if board[coord + 1] == '#' and coord % 10 != 9:
                                board[coord - 9] = '#'
                        if coord + (size * 10) < 100 and board[
                            coord + (size * 10)] == '#':  # check down and:. fix out of line problem
                            if board[coord - 1] == '#' and coord % 10 != 0:
                                board[coord + (size * 10) - 1] = '#'
                            if board[coord + 1] == '#' and coord % 10 != 9:
                                board[coord + (size * 10) + 1] = '#'



"""game cycles"""

while gamemode == 0:
    ship_placing(board1)
    ship_placing(board2)
    cleanboard(board1, clean_board)
    hiddenboard(board2, hidden_board)
    gameboard(clean_board, hidden_board)

    while 'S' in board1 or 'S' in board2:
        user_attack(board2)
        comp_attack(board1, targets_1)
        ship_status(board1, ship_list1)
        ship_status(board2, ship_list2)
        cleanboard(board1, clean_board)
        hiddenboard(board2, hidden_board)
        gameboard(clean_board, hidden_board)

        if 'S' not in board1:
            print('game over!')
            quit()
        if 'S' not in board2:
            print('you won!')
            quit()

while gamemode == 1:

    ship_placing(board1)
    ship_placing(board2)
    cleanboard(board1, clean_board)
    cleanboard(board2, hidden_board)
    gameboard(clean_board, hidden_board)

    while 'S' in board1 or 'S' in board2:
        comp_attack(board1,targets_1)
        comp_attack(board2, targets_2)
        ship_status(board1, ship_list1)
        ship_status(board2, ship_list2)
        cleanboard(board1, clean_board)
        cleanboard(board2, hidden_board)
        gameboard(clean_board, hidden_board)

        if 'S' not in board1:
            print('comp2 won!')
            quit()
        if 'S' not in board2:
            print('comp1 won!')
            quit()
