# Vars needed
#   - matrix for the game
#       + each set of arrays is a height
#   - array for height of each row
#   - player icons or colors (more then 1 var)
#
# BASIC Logic
#   - 1 turn each player
#   - on turn, select a colum and the icon sets on top of the last one in the same column
#   - each turn, update matrix and array_height
#

# Vars needed
#   - BOARD = 7x6 empty(0) matrix for game
board=[[1,0,0,0,0,0,0],[1,0,0,0,0,0,3],[1,0,2,2,2,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[4,4,4,4,4,4,4]]
#   - COL_HEIGHT = actual height of eachr colum during thew game
col_height=[0,0,0,0,0,0,0]
#   - PLAYERS = number code for each player // 0-empty  1-Player1  2-Player2
players=[0,1,2] 
#   - DIMENSIONS = height and width of the matrix
height= 5   # total height=6 // max index=5
width = 6   # total width =7 // max index=6


#=============================================
# METHODS TO MODIFY THE BOARD
#=============================================


def showBoard():
    line=""
    for x in board:
        for y in x:
           line=line+str(y)+" "
        print(line)
        line=""
    return 0

# =====\ resetBoard() \=====
# 1- 
def resetBoard():
    for x in range(height+1):
        for y in range(width+1):
           board[x][y]=8

# =====\ playTurn(playerCode) \=====
# 1- ask for colum to play until its able
# 2- set the player move on the lowest row of that colum
# 2.1- to set the row we take height value and subtract the checkHight value
def playTurn(player):
    col=int(input("Select colum: "))
    #col=3
    row=checkHeight(col)
    if(row<0):
        playTurn(player)
    else:
        board[height-row][col] = player
        
        return 0

#=============================================
# METHODS TO SIMPLIFY 
#=============================================
# =====\ checkHeight(colum) \=====
# 1- save the able position as solution and return it
# 2- set the next able position
# 3- if position is 6 the colum is full is not able
def checkHeight(col):
    solution=col_height[col] 
    if(solution==6):
        #print(-1)
        return -1
    else:
        col_height[col]+=1
        #print(solution)
        return solution
    
def checkWin():
    
    return 0


# EXECUTE PROGRAM
#showBoard()
#checkHeight(0)
#playTurn(8)
#resetBoard()
#showBoard()

#=============================================
#       RUN GAME
#=============================================
def runGame():
    resetBoard()
    showBoard()
    for i in range(4):
        playTurn(i%2)
        showBoard()
    print("WIP")

runGame()