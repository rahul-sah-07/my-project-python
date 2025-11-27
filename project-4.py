# tic tac toe game
import pygame
pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("X / O Game")

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
size = 200

board = [["","",""],
        ["","",""],
        ["","",""]]

player = "X"
history = []
winner = None
font = pygame.font.Font(None, 100)
win_font = pygame.font.Font(None, 70)

def restart():
    global board, player, history, winner
    board = [["","",""],
            ["","",""],
            ["","",""]]
    player = "X"
    history = []
    winner = None

def reverse():
    global player, winner
    if history and not winner:
        r, c, pl = history.pop()
        board[r][c] = ""
        player = pl

def check_win():
    global winner
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2] != "":
            winner = board[r][0]
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] != "":
            winner = board[0][c]
    if board[0][0] == board[1][1] == board[2][2] != "":
        winner = board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        winner = board[0][2]

run = True
while run:
    screen.fill(WHITE)

    pygame.draw.line(screen, BLACK, (200,0), (200,600), 5)
    pygame.draw.line(screen, BLACK, (400,0), (400,600), 5)
    pygame.draw.line(screen, BLACK, (0,200), (600,200), 5)
    pygame.draw.line(screen, BLACK, (0,400), (600,400), 5)

    for row in range(3):
        for col in range(3):
            if board[row][col] != "":
                text = font.render(board[row][col], True, BLACK)
                screen.blit(text, (col * size + 70, row * size + 50))

    if winner:
        msg = f"{winner} WINS!"
        win_text = win_font.render(msg, True, RED)
        screen.blit(win_text, (180, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reverse()
            if event.key == pygame.K_RETURN:
                restart()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if not winner:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                row = mouse_y // 200
                col = mouse_x // 200
                if board[row][col] == "":
                    board[row][col] = player
                    history.append((row, col, player))
                    check_win()
                    if not winner:
                        player = "O" if player == "X" else "X"

    pygame.display.update()

pygame.quit()
