import random

board = ['_' for x in range(0, 100)]
board2 = ['_' for z in range(0, 100)]

clean_board = ['_' for y in range(0, 100)]

list_h = list(range(0, 100))
list_v = list(range(0, 100))

ship_list1 = []
ship_list2 = []

attack_coords = list(range(0, 100))

targets = list()

orient = 0


# gamemode = int(input('0 for manual, 1 for random ship placement :'))


def battleship(size, orient, coord, board):
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

    counter = 0
    for x in board:
        if counter < 100:
            if x == '*' or x == '_':
                cleanboard[counter] = '.'

            else:
                cleanboard[counter] = x

        counter += 1

def user_choice():
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
    # print(board[coord:coord + (size * 10):10])

def comp_choice(size,board):
    board = board

    orient = random.choice(list(range(0, 2)))

    if orient == 0:
        coord = random.choice(list_h)
        while (coord % 10) + size > 10 or board[coord:coord + size] != list('_' * size):  # check if ship is not out of field and it placed on empty fields
            coord = random.choice(list_h)
        battleship(size, orient, coord, board)  # size, orient, coord, board
        list_h.remove(coord)
    elif orient == 1:
        coord = random.choice(list_v)
        while coord + (size * 10) > 100 or board[coord:coord + (size * 10):10] != list('_' * size):  # check if ship is not out of field and it placed on empty fields
            coord = random.choice(list_v)
        battleship(size, orient, coord, board)  # size, orient, coord, board
        list_v.remove(coord)


    # print('orientation - ', orient, 'size - ', size, 'coord - ', coord)

def ship_placing(board):
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
        # cleanboard(board, board3)
        # gameboard(board,board3)

def user_attack(board):
    attack_coord = int(input('choose the field for the attack: '))

    while attack_coord not in range(0, 100) or board[attack_coord] == 'D' or board[attack_coord] == 'X':
        attack_coord = int(input('choose the CORRECT field for the attack: '))

    if board[attack_coord] == 'S':
        board[attack_coord] = 'D'
    else:
        board[attack_coord] = '#'


def comp_attack(board):
    attack_coord = random.choice(attack_coords)

    while board[attack_coord] == 'D' or board[attack_coord] == 'X':
        attack_coord = random.choice(attack_coords)

    if bool(targets):
        attack_coord = random.choice(targets)
        targets.remove(attack_coord)

        # attack_coords.remove(attack_coord)

    if board[attack_coord] == 'S':
        print('Hit!')


    shoot_conditions(board, attack_coord)

# def shoot_conditions(board, attack_coord):
#
#     if board[attack_coord] == 'S':
#         board[attack_coord] = 'D'
#
#         if board[attack_coord - 1] == 'S':
#             # targets.append(board[attack_coord - 1])
#             targets.append(board.index('D') - 1)
#
#             # board.index('D')
#         if attack_coord < 99 and board[attack_coord + 1] == 'S':
#             targets.append(board.index('D') + 1)
#         if board[attack_coord - 10] == 'S':
#             targets.append(board.index('D') - 10)
#         if attack_coord < 90 and board[attack_coord + 10] == 'S':
#             targets.append(board.index('D') + 10)
#         # else:
#         #     board[attack_coord] = 'X'
#         elif (attack_coord < 99 and board[attack_coord + 1] != 'S') and board[attack_coord - 1] != 'S' and (attack_coord < 90 and board[attack_coord + 10] != 'S') and board[attack_coord - 10] != 'S':
#             board[attack_coord] = 'X'
#             print('ship destroyed! ')
#
#     else:
#         board[attack_coord] = '#'
#     attack_coords.remove(attack_coord)
#
#     print('targets: ', targets, 'att coord: ', attack_coord)

def shoot_conditions(board, attack_coord):

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


    print( 'computer shoot at coord ', attack_coord)

def ship_status(board,ship_list):



    size = 0
    orient = 0

    for ship in ship_list:
        for ind, value in enumerate(ship_list):
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
                if orient == 1:
                    if board[coord: coord * size + 10 : 10] == list('D' * size):
                        board[coord: coord * size + 10 : 10] = list('X' * size)
                    print('ship on coordinates', coord, ' destroyed!')



"""game cycles"""

gamemode = 0
stop_count = 0

while gamemode == 0:
    ship_placing(board)
    ship_placing(board2)
    cleanboard(board, clean_board)
    gameboard(clean_board, board2)

    while stop_count < 5:
        user_attack(board2)
        comp_attack(board)
        cleanboard(board, clean_board)
        gameboard(clean_board, board2)
        ship_status(board, ship_list1)
        ship_status(board2, ship_list2)
        stop_count += 1


while gamemode == 1:
    ship_placing(board)
    while stop_count < 30:
        comp_attack(board)
        cleanboard(board, clean_board)
        gameboard(board, clean_board)
        ship_status(board, ship_list1)
        stop_count += 1


    quit()

