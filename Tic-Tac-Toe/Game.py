import AI
import pygame

# Intialize the pygame
pygame.init()

# Define colors
TINTED_WHITE = (252, 218, 202)
DAVY_GREY = (85,85,85)
VIVID_TANGERINE = (248,166,125)
CELESTE = (79,234,222)
VIOLET = (243,124,243)

# Define Commonly Used Variables
LENGTH = 500
THIRD = LENGTH // 3
SPACING = LENGTH // 50

# Define the font
FONT = pygame.font.Font('freesansbold.ttf', LENGTH // 10)

# Set up the game window
WINDOW_SIZE = (LENGTH, LENGTH)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Super Tic Tac Toe")

# Board
board = [[0,0,0],[0,0,0],[0,0,0]]

# Draws the board
def draw_board():
    screen.fill(TINTED_WHITE)
    for i in range(1,3):
        pygame.draw.line(screen, DAVY_GREY, (i*THIRD, 0), (i*THIRD, LENGTH), SPACING)
        pygame.draw.line(screen, DAVY_GREY, (0, i*THIRD), (LENGTH, i*THIRD), SPACING)
    pygame.display.update()

# Handles the player moves
def handle_move(player):
    while True:
         # Check if the Pygame display is still open
        if pygame.display.get_surface() is None:
            return
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x = pos[0] // THIRD
                y = pos[1] // THIRD
                if board[y][x] == 0:
                    board[y][x] = player
                    display_move(x, y, player)
                    return

# Displays moves on the board
def display_move(x, y, player):
    if player == 1:
        pygame.draw.circle(screen, VIVID_TANGERINE, (x*THIRD + THIRD//2, y*THIRD + THIRD//2), THIRD//2 - SPACING, SPACING)
    elif player == 2:
        pygame.draw.line(screen, VIOLET, (x*THIRD + SPACING, y*THIRD + SPACING), (x*THIRD + THIRD - SPACING, y*THIRD + THIRD - SPACING), SPACING)
        pygame.draw.line(screen, VIOLET, (x*THIRD + THIRD - SPACING, y*THIRD + SPACING), (x*THIRD + SPACING, y*THIRD + THIRD - SPACING), SPACING)
    pygame.display.update()

# Checks for a winner
def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != 0:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]
    # Check for tie
    if sum(board[0]) + sum(board[1]) + sum(board[2]) == 14:
        return "Tie"
    return 0

# Displays the winner
def display_winner(winner):
    if winner == "Tie":
        text = FONT.render("Tie!", True, DAVY_GREY)
    elif winner == 1:
        text = FONT.render(f"O wins!", True, DAVY_GREY)
    elif winner == 2:
        text = FONT.render(f"X wins!", True, DAVY_GREY)
    text_rect = text.get_rect(center=(LENGTH//2, LENGTH//2))
    screen.blit(text, text_rect)
    pygame.display.update()

# Main game loop
def main():
    ai = AI.AI(1)
    player = 2
    draw_board()
    while True:
        print(board)
        if player == 1:
            # Get the AI's move
            move = ai.get_move(board)
            board[move[1]][move[0]] = player
            display_move(move[0], move[1], player)
            if winner != 0:
                display_winner(winner)
                break
            player = 2
        else:
            handle_move(player)
            winner = check_winner()
            if winner != 0:
                display_winner(winner)
                break
            player = 1

# Start the game
if __name__ == '__main__':
    main()
