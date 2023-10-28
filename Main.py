# Length Adjustable Super Tic Tac Toe in pygame (Full rules and menu included)
# Author: Michael White
# Date: 10/28/2023
# Description: This is a game of Super Tic Tac Toe in pygame.

import pygame

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (100, 100, 100)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHT_RED = (255, 100, 100)
LIGHT_BLUE = (100, 100, 255)

# Define Commonly Used Variables
length = 1200 
third = length // 3
ninth = length // 9
spacing = length // 50
bigSpacing = length // 20

# Define font
font = pygame.font.Font(None, length//10)

# Set up the game window
WINDOW_SIZE = (length, length)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Super Tic Tac Toe")

# Define menu options
menu_options = ["Start Game", "Instructions", "Quit"]

# Define function to display menu options
def display_menu():
    # Clear the screen
    screen.fill(BLACK)

    # Display the title
    title = font.render("Super Tic Tac Toe", True, WHITE)
    title_rect = title.get_rect(center=(length//2, length//4))
    screen.blit(title, title_rect)

    # Display the menu options
    for i, option in enumerate(menu_options):
        text = font.render(option, True, WHITE)
        text_rect = text.get_rect(center=(length//2, length//2 + i*length//10))
        screen.blit(text, text_rect)

    # Update the display
    pygame.display.update()

def display_instructions():
    # Clear the screen
    screen.fill(BLACK)

    # Set font and font size
    headerFont = pygame.font.Font(None, length//10)
    font = pygame.font.Font(None, length//35)

    # Create text objects
    title_text = headerFont.render("Instructions", True, WHITE)
    rules = [
        "1. The game is played on a 3x3 grid of 3x3 grids.",
        "2. The first player is O and the second player is X.",
        "3. The player must play in the grid corresponding to the last played cell.",
        "4. The player wins a grid by getting three in a row.",
        "5. The player wins the game by winning three grids in a row.",
        "6. If a player is forced to play in a grid that has already been won, they can play in any grid.",
        "7. If a player is forced to play in a grid that has no empty cells, they can play in any grid.",
        "8. The game ends in a tie if all grids are full and there is no winner.",
        "9. Press the 'Return to Menu' button to return to the main menu."
    ]
    rule_texts = [font.render(rule, True, WHITE) for rule in rules]

    # Set text positions
    title_pos = title_text.get_rect(center=(length//2, length//10))
    rule_pos = [rule_texts[i].get_rect(topleft=(length//20, length//5 + i*(font.get_height()+spacing))) for i in range(len(rules))]

    # Draw text objects on screen
    screen.blit(title_text, title_pos)
    for i, rule_text in enumerate(rule_texts):
        screen.blit(rule_text, rule_pos[i])

    # Draw return button
    font = pygame.font.Font(None, length//20)
    return_button = font.render("Return to Menu", True, WHITE)
    return_rect = return_button.get_rect(center=(length//2, length//1.2))
    screen.blit(return_button, return_rect)

    # Update the display
    pygame.display.update()

    # Wait for user input
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if return_rect.collidepoint(event.pos):
                    menu_screen()

# Define function to quit the game
def quit_game():
    pygame.quit()
    quit()

# Define function to handle user input
def handle_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the position of the mouse click
            pos = pygame.mouse.get_pos()

            # Check if the mouse click is on a menu option
            for i, option in enumerate(menu_options):
                text_rect = font.render(option, True, BLACK).get_rect(center=(length//2, length//2 + i*length//10))
                if text_rect.collidepoint(pos):
                    return option

    return None

# Draw the Tic Tac Toe board
def draw_board():
    # Draw big horizontal lines
    pygame.draw.line(screen, WHITE, (0, third), (length, third), length//100)
    pygame.draw.line(screen, WHITE, (0, 2*third), (length, 2*third), length//100)
    # Draw big vertical lines
    pygame.draw.line(screen, WHITE, (third, 0), (third, length), length//100)
    pygame.draw.line(screen, WHITE, (2*third, 0), (2*third, length), length//100)
    # Draw small tic tac toe boards
    x = 1 # Honestly, I forgot what this is, but if I remove it the board breaks
    for smallStep in range(6):
            for bigStep in range(3):
                # Draw small horizontal lines
                pygame.draw.line(screen, WHITE, (spacing + third*bigStep, (smallStep+x)*ninth), (third*(bigStep+1) - spacing, (smallStep+x)*ninth), length//200)
                # Draw small vertical lines
                pygame.draw.line(screen, WHITE, ((smallStep+x)*ninth, spacing + third*bigStep), ((smallStep+x)*ninth, third*(bigStep+1) - spacing), length//200)
            if smallStep % 2 == 1:
                x += 1

# Create the game board
#It's staggered like this because python cares about whitespace, and this is the easiest way to visualize it
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
    if board[bigRow][bigCol][smolRow][smolCol] == 0 and smol_check_winner(bigRow, bigCol) == None:
        board[bigRow][bigCol][smolRow][smolCol] = player
        return True
    else:
        return False

# Check for a winner in a small board
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

# Check for a winner in the big board
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

# Display the winner of a small board
def display_smol_winner(bigRow, bigCol, winner):
    if winner == 1:
        # Draw a circle
        pygame.draw.circle(screen, RED, (bigCol*third + ninth+bigSpacing, bigRow*third + ninth+bigSpacing), length//8, length//100)
    elif winner == 2:
        # Draw an X
        # Top left to bottom right 
        pygame.draw.line(screen, BLUE, (bigCol*third + bigSpacing, bigRow*third + bigSpacing), ((bigCol+1)*third - bigSpacing, (bigRow+1)*third - bigSpacing), spacing)
        # Bottom left to top right
        pygame.draw.line(screen, BLUE, ((bigCol+1)*third - bigSpacing, bigRow*third + bigSpacing), (bigCol*third + bigSpacing, (bigRow+1)*third - bigSpacing), spacing)

# Display the winner
def display_winner(winner):
    # Display the winner
    font = pygame.font.Font(None, length//10)
    if winner == "Tie":
        text = font.render("Tie!", True, WHITE)
    elif winner == 1:
        text = font.render(f"O wins!", True, RED)
    elif winner == 2:
        text = font.render(f"X wins!", True, BLUE)
    text_rect = text.get_rect(center=(length//2, length//2))
    screen.blit(text, text_rect)

def start_game():
    # Clear the screen
    screen.fill(BLACK)
    # Game loop
    player = 2 # 1 = O, 2 = X
    forceRow = -1
    forceCol = -1
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if player == 1:
                    bigRow = int(event.pos[1] // third)
                    bigCol = int(event.pos[0] // third)
                    smolRow = int((event.pos[1] // ninth) % 3)
                    smolCol = int((event.pos[0] // ninth) % 3)
                    if bigCol == forceCol and bigRow == forceRow:
                        if handle_move(bigRow, bigCol, smolRow, smolCol, player):
                            player = 2
                            if smol_check_winner(smolRow, smolCol) == None:
                                forceRow = smolRow
                                forceCol = smolCol
                            else:
                                forceRow = -1
                                forceCol = -1
                    elif forceRow == -1 and forceCol == -1:
                        if handle_move(bigRow, bigCol, smolRow, smolCol, player):
                            player = 2
                            if smol_check_winner(smolRow, smolCol) == None:
                                forceRow = smolRow
                                forceCol = smolCol
                            else:
                                forceRow = -1
                                forceCol = -1
                else:
                    bigRow = int(event.pos[1] // third)
                    bigCol = int(event.pos[0] // third)
                    smolRow = int((event.pos[1] // ninth) % 3)
                    smolCol = int((event.pos[0] // ninth) % 3)
                    if bigCol == forceCol and bigRow == forceRow:
                        if handle_move(bigRow, bigCol, smolRow, smolCol, player):
                            player = 1
                            if smol_check_winner(smolRow, smolCol) == None:
                                forceRow = smolRow
                                forceCol = smolCol
                            else:
                                forceRow = -1
                                forceCol = -1
                    elif forceRow == -1 and forceCol == -1:
                        if handle_move(bigRow, bigCol, smolRow, smolCol, player):
                            player = 1
                            if smol_check_winner(smolRow, smolCol) == None:
                                forceRow = smolRow
                                forceCol = smolCol
                            else:
                                forceRow = -1
                                forceCol = -1
                dubCol, dubRow = 0, 0 # dub for W for winner
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
                            pygame.draw.circle(screen, LIGHT_RED, (bigSpacing+bigCol*third+smolCol*ninth, bigSpacing+bigRow*third+smolRow*ninth), bigSpacing - spacing, length//200)
                        elif board[bigRow][bigCol][smolRow][smolCol] == 2:
                            pygame.draw.line(screen, LIGHT_BLUE, (spacing+bigCol*third+smolCol*ninth, spacing+bigRow*third+smolRow*ninth), (length//10+bigCol*third+smolCol*ninth, length//10+bigRow*third+smolRow*ninth), length//200)
                            pygame.draw.line(screen, LIGHT_BLUE, (length//10+bigCol*third+smolCol*ninth, spacing+bigRow*third+smolRow*ninth), (spacing+bigCol*third+smolCol*ninth, length//10+bigRow*third+smolRow*ninth), length//200)

        # Update the display
        pygame.display.update()
        pass

# Define menu screen function
def menu_screen():
    while True:
        # Display the menu options
        display_menu()

        # Handle user input
        option = handle_input()

        # Call the appropriate function based on user input
        if option == "Start Game":
            start_game()
        elif option == "Instructions":
            display_instructions()
        elif option == "Quit":
            pygame.quit()

# Call the menu screen function to start the game
menu_screen()