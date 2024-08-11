import pygame
import sys
 
 
pygame.init()
 
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 10
BOARD_ROWS = 3
BOARD_COLS = 3
CIRCLE_RADIUS = 45
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55

# Colors
BG_COLOR = (28, 28, 30)  # Jet Black
LINE_COLOR = (44, 44, 46)  # Slate Gray
CIRCLE_COLOR = (10, 132, 255)  # Sky Blue
CROSS_COLOR = (255, 69, 58)  # Neon Red
 

font = pygame.font.Font(None, 36) 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_COLOR)
 
board = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
 
def draw_lines():
    
    pygame.draw.line(screen, LINE_COLOR, (0, 100), (300, 100), 15)
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (300, 200), 15)
   
    pygame.draw.line(screen, LINE_COLOR, (100, 0), (100, 300), 15)
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 300), 15)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * 100 + 50), int(row * 100 + 50)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.lines(screen, CROSS_COLOR, True, [(col * 100 +5 ,row * 100 +5 ),((col+1) * 100 -5 ,(row+1) * 100 -5)], 15)
                pygame.draw.lines(screen, CROSS_COLOR, True, [(col * 100 +5,(row+1) * 100 -5 ),((col+1) * 100  -5,row * 100 +5 )], 15)
def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True
def check_tie():
    if  not check_win(1) and not check_win(2) and is_board_full():
        return True
    else:
        return False
 

def check_win(player):
     
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
             return True
 
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
             return True

     
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
         return True

   
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
         return True

    return False
def endgame(running):
    if check_win(player) :
        pygame.display.update()
        pygame.time.wait(1000)
        
        screen.fill(BG_COLOR)
        
        text = font.render(f"Player {player} Wins", True, (255,255,255))
         
        screen.blit(text, (WIDTH//2 - text.get_width()//2, 10))  
        pygame.display.update()
        pygame.time.wait(2000)
        
        
        pygame.quit()
        running = False
    if check_tie() :
        pygame.display.update()
        pygame.time.wait(1000)
        
        screen.fill(BG_COLOR)
        
        text = font.render("Tie", True, (255,255,255))
         
        screen.blit(text, (WIDTH//2 - text.get_width()//2, 10))  
        pygame.display.update()
        pygame.time.wait(2000)
        
        
        pygame.quit()
        running = False
        
def minimax(board,ismaxi):
    if check_tie():
        return 0
    elif check_win(1):
        return -1
    elif check_win(2):
        return 1
    
    
    if ismaxi:
        
        best  = -1000
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if available_square(row, col):
                    mark_square(row, col, 2)
                    
                    score = minimax(board, False)
                    
                    board[row][col] = 0
                    
                    best =max(best,score)
        return best
    if  not ismaxi:
        
        best  = 1000
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if available_square(row, col):
                    mark_square(row, col, 1)
                    
                    score = minimax(board, True)
                    
                    board[row][col] = 0
                    
                    best =min(best,score)
        return best
def computer_turn():
    endgame(running)
    best=-1000
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if available_square(row, col):
                mark_square(row, col, 2)
                
                score = minimax(board, False)
                
                board[row][col] = 0
                if(score > best):
                    best= score
                    move = [row,col]
    board[move[0]][move[1]] = 2
    draw_figures()
    pygame.display.update()
     
    
                
                
                
                
    

 
player = 1   
 

draw_lines()
running = True
while running:
    for event in pygame.event.get():
         
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN :
            mouseX = event.pos[0]  # x
            mouseY = event.pos[1]  # y

            clicked_row = int(mouseY // 100)
            clicked_col = int(mouseX // 100)

            if available_square(clicked_row, clicked_col):
                
                
                if(player==1):
                    mark_square(clicked_row, clicked_col, player)
                    draw_figures()
                    endgame(running)
                    
                    player=2
                    
        if(player==2):
            computer_turn()
            endgame(running)
            player=1
                
               

        

    pygame.display.update()
