import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battleship Game Board")

# Set up colors
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Set up font
font = pygame.font.SysFont(None, 25)

# Set up board dimensions
BOARD_SIZE = 10
CELL_SIZE = WIDTH // BOARD_SIZE
BOARD_MARGIN = (WIDTH - (CELL_SIZE * BOARD_SIZE)) // 2
BOARD_TOP_MARGIN = (HEIGHT - (CELL_SIZE * BOARD_SIZE)) // 2
CELL = 30

# Set up board state
board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
board = [[x for x in range(10),y for y in range(10)]]
# board = [[x,y], GRAY]

# Draw the board
# def draw_board():
#     screen.fill(WHITE)
#     pygame.draw.rect(screen, BLACK, (BOARD_MARGIN, BOARD_TOP_MARGIN, CELL_SIZE * BOARD_SIZE, CELL_SIZE * BOARD_SIZE), 2)
#     for row in range(BOARD_SIZE):
#         for col in range(BOARD_SIZE):
#             cell_color = BLUE if board[row][col] == 1 else GRAY
#             if cell_color == GREEN:
#                 cell_color = BLUE
#             pygame.draw.rect(screen, cell_color,
#                              (BOARD_MARGIN + col * CELL_SIZE, BOARD_TOP_MARGIN + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
#             pygame.draw.rect(screen, BLACK,
#                              (BOARD_MARGIN + col * CELL_SIZE, BOARD_TOP_MARGIN + row * CELL_SIZE, CELL_SIZE, CELL_SIZE),
#                              1)
#             if board[row][col] == 1:
#                 text = font.render("X", True, WHITE)
#                 text_rect = text.get_rect(center=(
#                 BOARD_MARGIN + col * CELL_SIZE + CELL_SIZE // 2, BOARD_TOP_MARGIN + row * CELL_SIZE + CELL_SIZE // 2))
#                 screen.blit(text, text_rect)

def draw_board():
    for row in range(10):
        for col in range(10):
            pygame.draw.rect(screen,GRAY,[CELL,CELL, (CELL * col), (CELL*row)])

# Highlight a cell when the mouse moves over it
def highlight_cell(mouse_pos, board):
    x, y = mouse_pos
    col = (x - BOARD_MARGIN) // CELL_SIZE
    row = (y - BOARD_TOP_MARGIN) // CELL_SIZE
    if col >= 0 and col < BOARD_SIZE and row >= 0 and row < BOARD_SIZE:
        board[row][col] = 2
    else:
        board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    draw_board()
    pygame.draw.rect(screen, GREEN,
                     (BOARD_MARGIN + col * CELL_SIZE, BOARD_TOP_MARGIN + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))


# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # elif event.type == pygame.MOUSEMOTION:
        #     highlight_cell(pygame.mouse.get_pos(), board)

    # Update screen
    draw_board()
    pygame.display.flip()

# Quit Pygame
pygame.quit()