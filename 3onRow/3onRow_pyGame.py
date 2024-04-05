import pygame
import sys
black=(0,0,0)
white=(255,255,255)
red = (255,0,0)
blue = (0,0,255)

sqrSide=100
corners =[10,120,230,330]

pygame.init()
pygame.display.set_caption("3 on ROW")
res= (340,380)
screen = pygame.display.set_mode(res)
screen.fill(black)


#=========== GAME LOGIC ================

mx = [["0","1","0"],["0","0","0"],["0","2","0"]]
options = {"0":"X","1":"O","2":" "}
global turn 

# Show actual state of game
def showGame():
    print("")
    line="|"
    for i in range(0,3):
        for j in range(0,3):
            line += options.get(mx[i][j],"NF")
            line += "|"
        print(line)
        line="|"

# Generate/reset game
def resetGame(): 
    for i in range(0,3):
        for j in range(0,3):
            mx[i][j]="2" 

# Set the player move by position
def playerMove(pos,turn):
    x=pos[1]
    y=pos[0]
    if(checkEmptySpace(x,y)):
        player=turn%2
        mx[x][y] = str(player)
        drawPlayer(pos,player)
        checkWin(pos,player)
        turn+=1
        return turn
    return turn
    
    


# -CHECK WIN-
def checkWin(pos,player):
    if(checkRow(pos,player) or checkColumn(pos,player) or checkDiagonal(pos,player)):
        print("Player "+str(player)+" WINS")
        stillPlaying = False
        return True
#Check columns for a win
def checkColumn(pos,player):
    for i in range(0,3):
        if(mx[0][i]==str(player) and mx[0][i]==mx[1][i] and mx[0][i]==mx[2][i]):
            print("column"+str(i))
            drawWin(pos,0)
            return True
    return False

#Check rows for a win
def checkRow(pos,player):
    for i in range(0,3):
        if(mx[i][0]==str(player) and mx[i][0]==mx[i][1] and mx[i][0]==mx[i][2]):
            print("row"+str(i))
            drawWin(pos,1)
            return True
    return False

#Check diagonals for a win
def checkDiagonal(pos,player):
    #from TopLeft to BottomRight
    if(mx[0][0]==str(player) and mx[0][0]==mx[1][1] and mx[0][0]==mx[2][2]):
        print("TL")
        drawWin(pos,2)
        return True
    #form TopRight to BottomLeft  
    if(mx[0][2]==str(player) and mx[0][2]==mx[1][1] and mx[0][2]==mx[2][0]):
        print("TR")
        drawWin(pos,3)
        return True
    return False

#---------------------------------------
# Upgrade
# Check move is empty on matrix
def checkEmptySpace(x,y):
    if(mx[x][y]=="2"):
        return True
    return False

#============= DRAW GAME ===============
def resetMatrix():
    for x in range(3):
        for y in range(3):
            pygame.draw.rect(screen,white,[corners[x],corners[y],sqrSide,sqrSide])
            pygame.display.update() 

def getSquare(pos):
    x=pos[0]
    y=pos[1]
    cuadrante=0
    for i in range(3):
        if(x>corners[i] and x<corners[i+1]):
            x=cuadrante
        if(y>corners[i] and y<corners[i+1]):
            y=cuadrante
        cuadrante+=1
    print("click: "+str(x)+","+str(y))
    posMatrix=(x,y)
    return posMatrix

def drawPlayer(pos,player):
    if(player==0):
        drawX(pos)
    if(player==1):
        drawO(pos)
  
def drawX(pos):
    x=pos[0]
    y=pos[1]
    pygame.draw.line(screen,black,[corners[x]+10,corners[y]+10],[corners[x]+90,corners[y]+90],7)
    pygame.draw.line(screen,black,[corners[x]+90,corners[y]+10],[corners[x]+10,corners[y]+90],7)
    return None

def drawO(pos):
    x=pos[0]
    y=pos[1]
    pygame.draw.circle(screen,blue,[corners[x]+50,corners[y]+50],40,5)
    return None

def drawWin(pos,case):
    x=pos[0]
    y=pos[1]
    if(case==0):#column
        pygame.draw.line(screen,red,[corners[x]+50,corners[0]+5],[corners[x]+50,corners[0]+315],7)
    if(case==1):#row
        pygame.draw.line(screen,red,[corners[0]+5,corners[y]+50],[corners[0]+315,corners[y]+50],7)
    if(case==2):#tl-br
        pygame.draw.line(screen,red,[corners[0]+10,corners[0]+10],[corners[3]-10,corners[3]-10],9)
    if(case==3):#tr-bl
        pygame.draw.line(screen,red,[corners[3]-10,corners[0]+10],[corners[0]+10,corners[3]-10],9)

def runGame():
    running = True  
    turn=0
    resetMatrix() 
    resetGame()
    # game loop 
    while running: 
        pygame.display.update() 
    # for loop through the event queue   
        for event in pygame.event.get(): 
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                turn=playerMove(getSquare(pos),turn)
                showGame()
                #drawO(getSquare(pos))
                #drawX(getSquare(pos))
                #drawWin(getSquare(pos),2)
                

            # Check for QUIT event       
            if event.type == pygame.QUIT: 
                running = False

runGame()