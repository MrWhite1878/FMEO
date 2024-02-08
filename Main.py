# LENGTH Adjustable Super Tic Tac Toe in pygame (Full rules and menu included)
# Author: Michael White
# Date: 10/28/2023
# Description: This is a game of Super Tic Tac Toe in pygame.
#
# Note that the LENGTH variable is used to adjust the size of the game window and can be changed before runtime
# Pressing the X button during the game will return you to the main menu
# Pressing Theme will change the theme (there are 3)

import pygame
import game_logic
import AI
import sys

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TINTED_WHITE = (252, 218, 202)
DAVY_GREY = (85, 85, 85)
LIGHT_BEIGE = (254, 254, 181)
LIGHT_RED = (255, 100, 100)
LIGHT_BLUE = (100, 100, 255)
LIGHT_PURPLE = (64, 33, 103)
TURQUOISE = (99, 216, 255)
BEAN_RED = (245, 93, 89)
CELESTE = (79, 234, 222)
VIOLET = (243, 124, 243)
VIVID_TANGERINE = (248, 166, 125)

# [BACKGROUND, TEXT/BOARD, HIGHLIGHT, PLAYER1, PLAYER2]
theme1 = [WHITE, DAVY_GREY, LIGHT_BEIGE, TURQUOISE, BEAN_RED]
theme2 = [BLACK, WHITE, LIGHT_PURPLE, LIGHT_BLUE, LIGHT_RED]
theme3 = [TINTED_WHITE, DAVY_GREY, VIVID_TANGERINE, CELESTE, VIOLET]
theme = theme1
theme_num = 1

# Define Commonly Used Variables
LENGTH = 700
THIRD = LENGTH // 3
NINTH = LENGTH // 9
SPACING = LENGTH // 50
BIGSPACING = LENGTH // 20

# Define font
FONT = pygame.font.Font(None, LENGTH // 10)

# Set up the game window
WINDOW_SIZE = (LENGTH, LENGTH)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Super Tic Tac Toe")

# Define menu options
menu_options = ["Start Game", "Instructions", "Theme", "Quit"]

# Create the game board
# It's staggered like this because python cares about whitespace, and this is the easiest way to visualize it
board = [
    [
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    ],
    [
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    ],
    [
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    ],
]


# Define function to display menu options
def display_menu():
    # Check if the Pygame display is still open
    if pygame.display.get_surface() is None:
        return

    # Clear the screen
    screen.fill(theme[0])

    # Display the title
    title = FONT.render("Super Tic Tac Toe", True, theme[1])
    title_rect = title.get_rect(center=(LENGTH // 2, LENGTH // 4))
    screen.blit(title, title_rect)

    # Display the menu options
    for i, option in enumerate(menu_options):
        text = FONT.render(option, True, theme[1])
        text_rect = text.get_rect(center=(LENGTH // 2, LENGTH // 2 + i * LENGTH // 10))
        screen.blit(text, text_rect)

    # Update the display
    pygame.display.update()


# Define function to display instructions
def display_instructions():
    # Clear the screen
    screen.fill(theme[0])

    # Set font and font size
    font = pygame.font.Font(None, LENGTH // 35)

    # Create text objects
    title_text = FONT.render("Instructions", True, theme[1])
    rules = [
        "1. The game is played on a 3x3 grid of 3x3 grids.",
        "2. The first player is O and the second player is X.",
        "3. The player must play in the grid corresponding to the last played cell.",
        "4. The player wins a grid by getting three in a row.",
        "5. The player wins the game by winning three grids in a row.",
        "6. If a player is forced to play in a grid that has already been won, they can play in any grid.",
        "7. If a player is forced to play in a grid that has no empty cells, they can play in any grid.",
        "8. The game ends in a tie if all grids are full and there is no winner.",
        "9. Press the 'Return to Menu' button to return to the main menu.",
    ]
    rule_texts = [font.render(rule, True, theme[1]) for rule in rules]

    # Set text positions
    title_pos = title_text.get_rect(center=(LENGTH // 2, LENGTH // 10))
    rule_pos = [
        rule_texts[i].get_rect(
            topleft=(LENGTH // 20, LENGTH // 5 + i * (font.get_height() + SPACING))
        )
        for i in range(len(rules))
    ]

    # Draw text objects on screen
    screen.blit(title_text, title_pos)
    for i, rule_text in enumerate(rule_texts):
        screen.blit(rule_text, rule_pos[i])

    # Draw return button
    font = pygame.font.Font(None, LENGTH // 20)
    return_button = font.render("Return to Menu", True, theme[1])
    return_rect = return_button.get_rect(center=(LENGTH // 2, LENGTH // 1.2))
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


# Define function to change the theme
def change_theme():
    global theme_num
    if theme_num == 1:
        theme_num = 2
        return theme2
    elif theme_num == 2:
        theme_num = 3
        return theme3
    elif theme_num == 3:
        theme_num = 1
        return theme1


# Define function to quit the game
def quit_game():
    pygame.quit()
    quit()


# Draw the Tic Tac Toe board
def draw_board():
    # Draw big horizontal lines
    pygame.draw.line(screen, theme[1], (0, THIRD), (LENGTH, THIRD), LENGTH // 100)
    pygame.draw.line(
        screen, theme[1], (0, 2 * THIRD), (LENGTH, 2 * THIRD), LENGTH // 100
    )
    # Draw big vertical lines
    pygame.draw.line(screen, theme[1], (THIRD, 0), (THIRD, LENGTH), LENGTH // 100)
    pygame.draw.line(
        screen, theme[1], (2 * THIRD, 0), (2 * THIRD, LENGTH), LENGTH // 100
    )
    # Draw small tic tac toe boards
    x = 1  # Honestly, I forgot what this is, but if I remove it the board breaks
    for smallStep in range(6):
        for bigStep in range(3):
            # Draw small horizontal lines
            pygame.draw.line(
                screen,
                theme[1],
                (SPACING + THIRD * bigStep, (smallStep + x) * NINTH),
                (THIRD * (bigStep + 1) - SPACING, (smallStep + x) * NINTH),
                LENGTH // 200,
            )
            # Draw small vertical lines
            pygame.draw.line(
                screen,
                theme[1],
                ((smallStep + x) * NINTH, SPACING + THIRD * bigStep),
                ((smallStep + x) * NINTH, THIRD * (bigStep + 1) - SPACING),
                LENGTH // 200,
            )
        if smallStep % 2 == 1:
            x += 1


# Define function to handle user input
def handle_input():
    # Check if the Pygame display is still open
    if pygame.display.get_surface() is None:
        return

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the position of the mouse click
            pos = pygame.mouse.get_pos()

            # Check if the mouse click is on a menu option
            for i, option in enumerate(menu_options):
                text_rect = FONT.render(option, True, theme[0]).get_rect(
                    center=(LENGTH // 2, LENGTH // 2 + i * LENGTH // 10)
                )
                if text_rect.collidepoint(pos):
                    return option
    return None


# Handle player moves
def handle_move(bigRow, bigCol, smolRow, smolCol, player):
    if (
        board[bigRow][bigCol][smolRow][smolCol] == 0
        and game_logic.smol_check_winner(board, bigRow, bigCol) == None
    ):
        board[bigRow][bigCol][smolRow][smolCol] = player
        return True
    else:
        return False


# Get a list of playable small boards
def playable_smol_boards(forceRow, forceCol):
    smol_boards = []
    if forceRow == -1 and forceCol == -1:
        for i in range(3):
            for j in range(3):
                if game_logic.smol_check_winner(board, i, j) == None:
                    smol_boards.append([i, j])
    else:
        smol_boards.append([forceRow, forceCol])
    return smol_boards



# Display the winner of a small board
def display_smol_winner(bigRow, bigCol, winner):
    if winner == 1:
        # Draw a circle
        pygame.draw.circle(
            screen,
            theme[4],
            (bigCol * THIRD + NINTH + BIGSPACING, bigRow * THIRD + NINTH + BIGSPACING),
            LENGTH // 8,
            LENGTH // 100,
        )
    elif winner == 2:
        # Draw an X
        # Top left to bottom right
        pygame.draw.line(
            screen,
            theme[3],
            (bigCol * THIRD + BIGSPACING, bigRow * THIRD + BIGSPACING),
            ((bigCol + 1) * THIRD - BIGSPACING, (bigRow + 1) * THIRD - BIGSPACING),
            SPACING,
        )
        # Bottom left to top right
        pygame.draw.line(
            screen,
            theme[3],
            ((bigCol + 1) * THIRD - BIGSPACING, bigRow * THIRD + BIGSPACING),
            (bigCol * THIRD + BIGSPACING, (bigRow + 1) * THIRD - BIGSPACING),
            SPACING,
        )



# Display the winner
def display_winner(winner):
    # Display the winner
    if winner == "Tie":
        text = FONT.render("Tie!", True, theme[1])
    elif winner == 1:
        text = FONT.render(f"O wins!", True, theme[4])
    elif winner == 2:
        text = FONT.render(f"X wins!", True, theme[3])
    text_rect = text.get_rect(center=(LENGTH // 2, LENGTH // 2))
    screen.blit(text, text_rect)
    draw_board()
    pygame.display.update()


# declared variables outside of function to prevent them from resetting every time the function is called
player = 2  # 1 is O, 2 is X
forceRow, forceCol = (
    -1,
    -1,
)  # -1 means no force, and they correspond to the move that the next player must make


def start_game():
    ai = AI.CPU()
    # Clear the screen
    screen.fill(theme[0])
    # Game loop
    global player, forceRow, forceCol
    game_over = False
    while not game_over:
        for event in pygame.event.get():  # aka whenever there's an event
            if event.type == pygame.QUIT:
                game_over = True
            if player == 1:
                AI_move = ai.getMove(board, 2, forceRow, forceCol)
                bigRow = AI_move[0]
                bigCol = AI_move[1]
                smolRow = AI_move[2]
                smolCol = AI_move[3]
                print(AI_move)
                if (
                    bigCol == forceCol and bigRow == forceRow
                ):  # essentially, if the player in the highlighted board
                    if handle_move(bigRow, bigCol, smolRow, smolCol, player):
                        player = 2  # switch players
                        # this next part is self explanatory right?
                        if game_logic.smol_check_winner(board, smolRow, smolCol) == None:
                            forceRow = smolRow
                            forceCol = smolCol
                        else:
                            forceRow = -1
                            forceCol = -1
                elif forceRow == -1 and forceCol == -1:
                    if handle_move(bigRow, bigCol, smolRow, smolCol, player):
                        player = 2
                        if game_logic.smol_check_winner(board, smolRow, smolCol) == None:
                            forceRow = smolRow
                            forceCol = smolCol
                        else:
                            forceRow = -1
                            forceCol = -1
            elif event.type == pygame.MOUSEBUTTONDOWN:  # click
                bigRow = int(event.pos[1] // THIRD)
                bigCol = int(event.pos[0] // THIRD)
                smolRow = int((event.pos[1] // NINTH) % 3)
                smolCol = int((event.pos[0] // NINTH) % 3)
                if bigCol == forceCol and bigRow == forceRow:
                    if handle_move(bigRow, bigCol, smolRow, smolCol, player):
                        player = 1
                        if game_logic.smol_check_winner(board, smolRow, smolCol) == None:
                            forceRow = smolRow
                            forceCol = smolCol
                        else:
                            forceRow = -1
                            forceCol = -1
                elif forceRow == -1 and forceCol == -1:
                    if handle_move(bigRow, bigCol, smolRow, smolCol, player):
                        player = 1
                        if game_logic.smol_check_winner(board, smolRow, smolCol) == None:
                            forceRow = smolRow
                            forceCol = smolCol
                        else:
                            forceRow = -1
                            forceCol = -1
        # Draw the game board
        screen.fill(theme[0])
        for bigRow in range(3):
            for bigCol in range(3):
                # checks if there's a winner in the small board and displays it
                if game_logic.smol_check_winner(board, bigRow, bigCol) != None:
                    display_smol_winner(
                        bigRow, bigCol, game_logic.smol_check_winner(board, bigRow, bigCol)
                    )
                # makes highlighted board
                for i in playable_smol_boards(forceRow, forceCol):
                    if [bigRow, bigCol] == i:
                        pygame.draw.rect(
                            screen,
                            theme[2],
                            (
                                bigCol * THIRD + SPACING - 5,
                                bigRow * THIRD + SPACING - 5,
                                THIRD - 2 * SPACING + 10,
                                THIRD - 2 * SPACING + 10,
                            ),
                        )

                # draws the pieces
                for smolRow in range(3):
                    for smolCol in range(3):
                        # draws O's
                        if board[bigRow][bigCol][smolRow][smolCol] == 1:
                            pygame.draw.circle(
                                screen,
                                theme[4],
                                (
                                    BIGSPACING + bigCol * THIRD + smolCol * NINTH,
                                    BIGSPACING + bigRow * THIRD + smolRow * NINTH,
                                ),
                                BIGSPACING - SPACING,
                                LENGTH // 200,
                            )
                        # draws X's
                        elif board[bigRow][bigCol][smolRow][smolCol] == 2:
                            pygame.draw.line(
                                screen,
                                theme[3],
                                (
                                    SPACING + bigCol * THIRD + smolCol * NINTH,
                                    SPACING + bigRow * THIRD + smolRow * NINTH,
                                ),
                                (
                                    LENGTH // 10 + bigCol * THIRD + smolCol * NINTH,
                                    LENGTH // 10 + bigRow * THIRD + smolRow * NINTH,
                                ),
                                LENGTH // 200,
                            )
                            pygame.draw.line(
                                screen,
                                theme[3],
                                (
                                    LENGTH // 10 + bigCol * THIRD + smolCol * NINTH,
                                    SPACING + bigRow * THIRD + smolRow * NINTH,
                                ),
                                (
                                    SPACING + bigCol * THIRD + smolCol * NINTH,
                                    LENGTH // 10 + bigRow * THIRD + smolRow * NINTH,
                                ),
                                LENGTH // 200,
                            )

        # Check for win
        if game_logic.check_winner(board):
            display_winner(game_logic.check_winner(board))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    sys.exit()
        draw_board()
        # print(theme)

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
        global theme
        if option == "Start Game":
            start_game()
        elif option == "Instructions":
            display_instructions()
        elif option == "Theme":
            theme = change_theme()
        elif option == "Quit":
            pygame.quit()
            sys.exit()


# Call the menu screen function to start the game
menu_screen()
