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
ind_height= 5   # total height=6 // max index=5
ind_width = 6   # total width =7 // max index=6

#   - WINs = variables to keep track of wins
win_list=[1,0,0,0]  # H, V, LR, RL
win_bool=True


#=============================================
# METHODS TO MODIFY THE BOARD
#=============================================


def showBoard():
    line=""
    for x in board:
        for y in x:
            if(y==2):
               line=line+"| "
            else:
                if(y==0):
                    p="X"
                else:
                    p="O"
                line=line+"|"+str(p)
        line=line+"|"    
        print(line)
        line=""
    return 0

# =====\ resetWins() \=====
def resetWin():
    global win_bool 
    win_bool= False
    for x in range(len(win_list)):
        win_list[x]=0
    

# =====\ resetBoard() \=====
# 1- 
def resetBoard():
    col_height=[0,0,0,0,0,0,0]
    for x in range(ind_height+1):
        for y in range(ind_width+1):
           board[x][y]=2

# =====\ playTurn(playerCode) \=====
# 1- ask for colum to play until its able
# 2- set the player move on the lowest row of that colum
# 2.1- to set the row we take height value and subtract the checkHight value
def playTurn(player):
    col=input("Select colum: ")
    while(notAbleMove(col)):
       col=input("Select colum: ")
    able_col=int(col)
    #col=3
    #print(able_col)
    row=checkHeight(able_col)
    if(row<0):
        playTurn(player)
    else:
        board[ind_height-row][able_col] = player
        #Check WIN
        checkH(able_col)
        
        return 0

#=============================================
# METHODS TO SIMPLIFY 
#=============================================
# =====\ checkHeight(colum) \=====
# 1- save the able position as solution and return it
# 2- set the next able position
# 3- if position is 6 the colum is full is not able
def checkHeight(col):
    #print(type(col))
    solution=col_height[col] 
    if(solution==6):
        #print(-1)
        return -1
    else:
        col_height[col]+=1
        #print(solution)
        return solution
    
# =====|  checkAbleMove(col)  |=====
def notAbleMove(col):
    # Comprobation of good imput
    if(not col.isdigit()):
        return True
    if(0<=int(col)<6):
        return False
    return True
    
# Do all posible check wins
def checkWin(lastcolumPLay):
    checkH(lastcolumPLay)
    #checkV(lastcolumPLay)
    #checkLR(lastcolumPLay)
    #checkRL(lastcolumPLay)
    return 0

# Do check win vertical
# -- pre-check at least 4 colums with same or more height level
# -- full-check 
def checkH(lastColSelected):
    col=lastColSelected
    # get the actual height of the move for the pre-check
    actualHeight= col_height[col]
    # get the amount of posible values (must be 4 or grater)
    count=0
    
    for x in col_height:
        if x>=actualHeight:
            count+=1
    # check if the count is enought to go into full-check
    if(count>=4):
        
        breakpoint()
        # do full-check
        consecutivePlayer=1
        pWinRow=ind_height-(actualHeight-1)
        actual_player=board[pWinRow][col]
        print('posible victoria de: ' +str(actual_player))
        #go Left
        i=1
        while(col-i>=0):
            if(board[pWinRow][col-i]==actual_player):
                consecutivePlayer+=1
            else:
                i=7
            i+=1  
        #go Right
        i=1
        while(col+i<=6):
            if(board[pWinRow][col+i]==actual_player):
                consecutivePlayer+=1
            else:
                i=7
            i+=1
        if(consecutivePlayer>3):
            global win_bool
            win_bool=True
            win_list[0]=1
            print("WIIIN")
        


# Do check win vertical
#
def checkV():
    return 0

# Do check diagonal left to right
#
def checkLR():
    return 0

# Do check diagonla right to left
#
def checkRL():
    return 0


# EXECUTE PROGRAM
#showBoard()
#checkHeight(0)
#print(checkAbleMove("8"))
#playTurn(8)
#resetWin()
#resetBoard()
#showBoard()

# CUSTOM TEST 
def custom_test1():
    board[5]=[0,0,0,0,2,2,2]
    for x in range(4):
        col_height[x]=1

#=============================================
#       RUN GAME
#=============================================
def runGame(n):
    #   Show game instructions
    print("In this game u select a colum to play betwen 0-6")
    #   Reset game
    resetBoard()
    resetWin()
    #   Play game until win
    rounds=0
    showBoard()
    while((not win_bool) and (rounds<n)):
        playTurn(rounds%2)
        showBoard()
        rounds+=1
    print("WIP")

runGame(10)