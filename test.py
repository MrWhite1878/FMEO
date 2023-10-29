import pygame

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0 , 0)
BLUE = (0, 0, 255)
LIGHT_RED = (255, 100, 100)
LIGHT_BLUE = (52, 113, 235)

# Define Commonly Used Variables
length = 1000
third = length // 3
ninth = length // 9
spacing = length // 50

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_SIZE = (length, length)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Super Tic Tac Toe")

# Draw the Tic Tac Toe board
def draw_board():
    # Draw big horizontal lines
    pygame.draw.line(screen, WHITE, (0, third), (length, third), length//100)
    pygame.draw.line(screen, WHITE, (0, 2*third), (length, 2*third), length//100)
    # Draw big vertical lines
    pygame.draw.line(screen, WHITE, (third, 0), (third, length), length//100)
    pygame.draw.line(screen, WHITE, (2*third, 0), (2*third, length), length//100)
    # Draw small tic tac toe boards
    x = 1 # honestly i forget what this is but if i remove it the board breaks
    for smallStep in range(6):
            for bigStep in range(3):
                # Draw small horizontal lines
                pygame.draw.line(screen, WHITE, (spacing + third*bigStep, (smallStep+x)*ninth), (third*(bigStep+1) - spacing, (smallStep+x)*ninth), length//200)
                # Draw small vertical lines
                pygame.draw.line(screen, WHITE, ((smallStep+x)*ninth, spacing + third*bigStep), ((smallStep+x)*ninth, third*(bigStep+1) - spacing), length//200)
            if smallStep % 2 == 1:
                x += 1

# Create the game board
board = [[[[0, 0, 0], 
           [0, 0, 0], 
           [0, 0, 0]], [[0, 0, 0], 
                        [0, 0, 0], 
                        [0, 0, 0]], [[0, 0, 0], 
                                     [0, 0, 0], 
                                     [0, 0, 0]]],
         [[[0, 0, 0], 
           [0, 0, 0], 
           [0, 0, 0]], [[0, 0, 0], 
                        [0, 0, 0], 
                        [0, 0, 0]], [[0, 0, 0], 
                                     [0, 0, 0], 
                                     [0, 0, 0]]],
         [[[0, 0, 0], 
           [0, 0, 0], 
           [0, 0, 0]], [[0, 0, 0], 
                        [0, 0, 0], 
                        [0, 0, 0]], [[0, 0, 0], 
                                     [0, 0, 0], 
                                     [0, 0, 0]]]]

# Handle player moves
def handle_move(bigRow, bigCol, smolRow, smolCol, player):
    if board[bigRow][bigCol][smolRow][smolCol] == 0:
        board[bigRow][bigCol][smolRow][smolCol] = player
        return True
    else:
        return False

# Check for a winner
def smol_check_winner(bigRow, bigCol):
    # Check rows
    for row in range(3):
        if board[bigRow][bigCol][row][0] == board[bigRow][bigCol][row][1] == board[bigRow][bigCol][row][2] != 0:
            return board[bigRow][bigCol][row][0]
    # Check columns
    for col in range(3):
        if board[bigRow][bigCol][0][col] == board[bigRow][bigCol][1][col] == board[bigRow][bigCol][2][col] != 0:
            return board[bigRow][bigCol][0][col]
    # Check diagonals
    if board[bigRow][bigCol][0][0] == board[bigRow][bigCol][1][1] == board[bigRow][bigCol][2][2] != 0:
        return board[bigRow][bigCol][0][0]
    if board[bigRow][bigCol][0][2] == board[bigRow][bigCol][1][1] == board[bigRow][bigCol][2][0] != 0:
        return board[bigRow][bigCol][0][2]
    # Check for a tie
    tie = True
    for row in range(3):
        for col in range(3):
            if board[bigRow][bigCol][row][col] == 0:
                tie = False
    if tie:
        return "Tie"
    # No winner yet
    return None

def check_winner():
    # Check rows
    for row in range(3):
        if smol_check_winner(row, 0) == smol_check_winner(row, 1) == smol_check_winner(row, 2) != None:
            return smol_check_winner(row, 0)
    # Check columns
    for col in range(3):
        if smol_check_winner(0, col) == smol_check_winner(1, col) == smol_check_winner(2, col) != None:
            return smol_check_winner(0, col)
    # Check diagonals
    if smol_check_winner(0, 0) == smol_check_winner(1, 1) == smol_check_winner(2, 2) != None:
        return smol_check_winner(0, 0)
    if smol_check_winner(0, 2) == smol_check_winner(1, 1) == smol_check_winner(2, 0) != None:
        return smol_check_winner(0, 2)
    # Check for a tie
    tie = True
    for row in range(3):
        for col in range(3):
            if smol_check_winner(row, col) == None:
                tie = False
    if tie:
        return "Tie"
    # No winner yet
    return None

def display_smol_winner(bigRow, bigCol, winner):
    if winner == 1:
        pygame.draw.circle(screen, RED, (bigCol*third+161, bigRow*third+161), 125, 10)
    elif winner == 2:
        spacing = 50
        pygame.draw.line(screen, BLUE, (bigCol*third+spacing, bigRow*third+spacing), ((bigCol+1)*third-spacing, (bigRow+1)*third-spacing), 20)
        pygame.draw.line(screen, BLUE, ((bigCol+1)*third-spacing, bigRow*third+spacing), (bigCol*third+spacing, (bigRow+1)*third-spacing), 20)

# Display the winner
def display_winner(winner):
    font = pygame.font.Font(None, 100)
    if winner == "Tie":
        text = font.render("Tie!", True, WHITE)
    elif winner == 1:
        text = font.render(f"O wins!", True, RED)
    elif winner == 2:
        text = font.render(f"X wins!", True, BLUE)
    text_rect = text.get_rect(center=(500, 500))
    screen.blit(text, text_rect)

# Game loop
player = 1
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if player == 1:
                bigRow = int(event.pos[1] // third)
                bigCol = int(event.pos[0] // third)
                smolRow = int((event.pos[1]// third//3)%3)
                smolCol = int((event.pos[0]// third//3)%3)
                if handle_move(bigRow, bigCol, smolRow, smolCol, player):
                    player = 2
            else:
                bigRow = int(event.pos[1] // third)
                bigCol = int(event.pos[0] // third)
                smolRow = int((event.pos[1]// third//3)%3)
                smolCol = int((event.pos[0]// third//3)%3)
                if handle_move(bigRow, bigCol, smolRow, smolCol, player):
                    player = 1
            dubCol, dubRow = 0, 0
            for i in range(3):
                for j in range(3):
                    smol_winner = smol_check_winner(i,j)
                    if smol_winner != None:
                        display_smol_winner(i, j, smol_winner)
            winner = check_winner()
            if winner != None:
                display_winner(winner)
                game_over = True
    # Draw the game board
    draw_board()
    for bigRow in range(3):
        for bigCol in range(3):
            for smolRow in range(3):
                for smolCol in range(3):
                    if board[bigRow][bigCol][smolRow][smolCol] == 1:
                        pygame.draw.circle(screen, LIGHT_RED, (50+bigCol*third+smolCol*third//3, 50+bigRow*third+smolRow*third//3), 25, 5)
                    elif board[bigRow][bigCol][smolRow][smolCol] == 2:
                        pygame.draw.line(screen, LIGHT_BLUE, (20+bigCol*third+smolCol*third//3, 20+bigRow*third+smolRow*third//3), (100+bigCol*third+smolCol*third//3, 100+bigRow*third+smolRow*third//3), 5)
                        pygame.draw.line(screen, LIGHT_BLUE, (100+bigCol*third+smolCol*third//3, 20+bigRow*third+smolRow*third//3), (20+bigCol*third+smolCol*third//3, 100+bigRow*third+smolRow*third//3), 5)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.time.wait(800)
pygame.quit()