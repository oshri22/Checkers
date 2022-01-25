import pygame
import sys


pygame.init()


WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800

WHITE_CHAR = 'W'
BLACK_CHAR = 'B'

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)



display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
img = pygame.image.load('./background.png')

board = [[None for i in range(WINDOW_WIDTH // 100)] for i in range(WINDOW_HEIGHT // 100)]


def fillBoard():
    for (posY, i) in enumerate(board):
        for posX in range(len(i)):
            if posY < 3:
                if posY % 2 == 0 and posX % 2 == 1:
                    board[posY][posX] = BLACK_CHAR
                elif posY % 2 == 1 and posX % 2 == 0:
                    board[posY][posX] = BLACK_CHAR
            
            elif posY > 4:
                if posY % 2 == 0 and posX % 2 == 1:
                    board[posY][posX] = WHITE_CHAR
                elif posY % 2 == 1 and posX % 2 == 0:
                    board[posY][posX] = WHITE_CHAR
            
                
def draw():
    display.blit(img, (0, 0))
    for (posY, i) in enumerate(board):
        for posX in range(len(i)):
            if i[posX]:
                color = WHITE
                if i[posX] == BLACK_CHAR:
                    color = BLUE
                pygame.draw.circle(display, color, (posX * 100 + 50, posY * 100 + 50), 50)

    pygame.display.update()


def checkMove(posXFrom, posYFrom, posXTo, posYTo, isWhite) -> bool:
    print("checking move")
    if not isWhite:
        if posYFrom + 2 == posYTo and abs(posXTo - posXFrom) == 2:
            print("eating")
            if posYFrom + 1 < 8 and posXFrom + 1 < 8 and board[posYFrom + 1][posXFrom + 1] == WHITE_CHAR:
                board[posYFrom + 1][posXFrom + 1] = None
                print("on my right")
                return True
            elif posYFrom + 1 < 8 and posXFrom - 1 < 8 and board[posYFrom + 1][posXFrom - 1] == WHITE_CHAR: 
                print("on my left")
                board[posYFrom + 1][posXFrom - 1] = None
                return True

        elif posYFrom + 1 != posYTo:
            return False
    else:
        if posYFrom - 2 == posYTo and abs(posXTo - posXFrom) == 2:
            print("eating")
            if posYFrom - 1 < 8 and posXFrom + 1 < 8 and board[posYFrom - 1][posXFrom + 1] == BLACK_CHAR:
                board[posYFrom - 1][posXFrom + 1] = None
                print("on my right")
                return True

            elif posYFrom - 1 < 8 and posXFrom - 1 < 8 and board[posYFrom - 1][posXFrom - 1] == BLACK_CHAR:
                board[posYFrom - 1][posXFrom - 1] = None
                print("on my left")
                return True

        elif posYFrom - 1 != posYTo:
            return False
        
    if abs(posXTo - posXFrom) != 1:
        return False
    else:
        return True



def main():
    global board
    fillBoard()
    draw()
    isWhite = True
    isPick = True
    posXFrom = 0
    posYFrom = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    isPick = True
                    print("canceling move")
                elif event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if isPick:
                        posXFrom = pos[0] // 100
                        posYFrom = pos[1] // 100
                        
                        if (isWhite and board[posYFrom][posXFrom] == WHITE_CHAR) or (not isWhite and board[posYFrom][posXFrom] == BLACK_CHAR):
                            print(posXFrom, posYFrom)
                            isPick = False

                        else:
                            posXFrom = -1
                            posYFrom = -1

                    else: #moveing
                        posXTo = pos[0] // 100
                        posYTo = pos[1] // 100
                        
                        if board[posYTo][posXTo] == None:
                            if checkMove(posXFrom, posYFrom, posXTo, posYTo, isWhite):
                                board[posYTo][posXTo] = board[posYFrom][posXFrom]
                                board[posYFrom][posXFrom] = None
                                draw()
                                isWhite = not isWhite
                                isPick = True

    

if __name__ == '__main__':
    main()