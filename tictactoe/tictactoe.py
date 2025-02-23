import pygame
import sys
import math
import time

# Initialize pygame
pygame.init()

# Define Constants
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 10
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 10
CROSS_WIDTH = 15
SPACE = SQUARE_SIZE // 4

# Colors
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
TEXT_COLOR = (255, 255, 255)

# Players
HUMAN = -1  # X (User)
AI = 1       # O (Computer)

# Create Game Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe AI (Unbeatable)")
screen.fill(BG_COLOR)

# Game Board
board = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# Font for displaying the winner
font = pygame.font.Font(None, 60)

def draw_lines():
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == HUMAN:
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
            elif board[row][col] == AI:
                pygame.draw.circle(screen, CIRCLE_COLOR, 
                                   (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)

def is_winner(player):
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def is_board_full():
    return all(board[row][col] != 0 for row in range(BOARD_ROWS) for col in range(BOARD_COLS))

def minimax(board, depth, is_maximizing):
    if is_winner(AI):
        return 1
    if is_winner(HUMAN):
        return -1
    if is_board_full():
        return 0
    
    if is_maximizing:
        best_score = -math.inf
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] == 0:
                    board[row][col] = AI
                    score = minimax(board, depth + 1, False)
                    board[row][col] = 0
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] == 0:
                    board[row][col] = HUMAN
                    score = minimax(board, depth + 1, True)
                    board[row][col] = 0
                    best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -math.inf
    best_move = None
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                board[row][col] = AI
                score = minimax(board, 0, False)
                board[row][col] = 0
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    if best_move:
        board[best_move[0]][best_move[1]] = AI

def display_winner(message):
    global game_over
    text = font.render(message, True, TEXT_COLOR)
    screen.fill(BG_COLOR)
    screen.blit(text, (WIDTH // 4, HEIGHT // 3))
    pygame.display.update()
    time.sleep(5)  # Wait for 5 seconds before closing
    pygame.quit()
    sys.exit()

# Main Game Loop
draw_lines()
game_over = False
player_turn = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and player_turn and not game_over:
            x, y = event.pos
            row, col = y // SQUARE_SIZE, x // SQUARE_SIZE
            if board[row][col] == 0:
                board[row][col] = HUMAN
                if is_winner(HUMAN):
                    display_winner("You Win!")
                elif is_board_full():
                    display_winner("It's a Draw!")
                player_turn = False

    if not player_turn and not game_over:
        ai_move()
        if is_winner(AI):
            display_winner("AI Wins!")
        elif is_board_full():
            display_winner("It's a Draw!")
        player_turn = True

    if not game_over:
        screen.fill(BG_COLOR)
        draw_lines()
        draw_figures()
        pygame.display.update()
