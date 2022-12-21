import random

board = ['_' for x in range(0, 100)]
board2 = ['_' for z in range(0, 100)]
board3 = ['_' for y in range(0, 100)]

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
        if (coord + size) % 10 != 0:  # check right
            board[coord + size] = '*'
        if board[coord - 1] == '*':  # check left and:
            if board[coord - 10] == '*':  # check up
                board[coord - 11] = '*'
            if coord < 90 and board[coord + 10] == '*':  # fix out of line problem
                board[coord + 9] = '*'
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
        if coord + (size * 10) < 90:  # check down
            board[coord + (size * 10)] = '*'
        if board[coord - 10] == '*':  # check up and
            if board[coord - 1] == '*':
                board[coord - 11] = '*'
            if board[coord + 1] == '*':
                board[coord - 9] = '*'
        if coord + (size * 10) < 90 and board[coord + (size * 10)] == '*':  # fix out of line problem
            if board[coord - 1] == '*':
                board[coord + (size * 10) - 1] = '*'
            if board[coord + 1] == '*':
                board[coord + (size * 10) + 1] = '*'


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
        if x == '*':
            cleanboard[counter] = '_'

        else: cleanboard[counter] = x

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
        while (coord % 10) + size > 10 or board[coord:coord + size] != (
                list('_' for x in
                     range(coord, coord + size))):  # check if ship is not out of field and it placed on empty fields
            coord = int(input('choose the CORRECT square for your ship: '))

    elif orient == 1:
        while coord + (size * 10) >= 110 or board[coord:coord + (size * 10):10] != (
                list('_' for x in
                     range(coord, coord + size))):  # check if ship is not out of field and it placed on empty fields
            coord = int(input('choose the CORRECT square for your ship: '))

    battleship(size, orient, coord, board)  # size, orient, coord, board
    print(board[coord:coord + (size * 10):10])


def comp_choice(size):
    orient = random.choice(list(range(0, 2)))
    # size = random.choice(list(range(1, 5)))
    coord = random.choice(list(range(0, 100)))
    print(board[coord:coord + size])
    print('2', list('_' for x in range(coord, coord + size)))
    if orient == 0:
        while (coord % 10) + size > 10 and board[coord:coord + size] != (
                list('_' for x in
                     range(coord, coord + size))):  # check if ship is not out of field and it placed on empty fields
            coord = random.choice(list(range(0, 100)))
        battleship(size, orient, coord, board)  # size, orient, coord, board
    elif orient == 1:
        while coord + (size * 10) > 100 and board[coord:coord + (size * 10):10] != (
                list('_' for x in
                     range(coord, coord + size))):  # check if ship is not out of field and it placed on empty fields
            coord = random.choice(list(range(0, 100)))
        battleship(size, orient, coord, board)  # size, orient, coord, board


targets = list(set(list()))

def ship_placing():
    count = 0

    while count < 7:

        if count == 0:
            comp_choice(4)

        elif count < 3:
            comp_choice(3)

        elif count < 6:
            comp_choice(2)

        count += 1





def attack(board):
    attack_coord = int(input('choose the field for the attack: '))

    if attack_coord in targets:
        targets.remove(attack_coord)

    while attack_coord not in range(0, 100) or board[attack_coord] == 'D' or board[attack_coord] == 'X':
        attack_coord = int(input('choose the CORRECT field for the attack: '))

    if board[attack_coord] == 'S':
        board[attack_coord] = 'D'

        if board[attack_coord - 1] == 'S':
            # targets.append(board[attack_coord - 1])
            targets.append(board.index('D') - 1)

            # board.index('D')
        if board[attack_coord + 1] == 'S':
            targets.append(board.index('D') + 1)
        if board[attack_coord - 10] == 'S':
            targets.append(board.index('D') - 10)
        if board[attack_coord + 10] == 'S':
            targets.append(board.index('D') + 10)
        else:
            board[attack_coord] = 'X'

    else:
        board[attack_coord] = '#'


    print('targets: ', targets)



"""game cycles"""

gamemode = 1
while gamemode == 0:
    user_choice()
    # battleship(4, 0, 33, board)

    gameboard(board, board2)
    while True:
        attack(board)
        gameboard(board, board2)

stop_count = 0
while gamemode == 1:
    ship_placing()
    cleanboard(board, board3)
    gameboard(board, board3)




    quit()


while gamemode == 2:
    size = 1
    comp_choice(size)
    size = 2
    comp_choice(size)
    gameboard(board, board2)
    stop_count += 1
    if stop_count == 2:
        quit()
