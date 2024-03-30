# Basic function ideas needed
# 1- Draw Initial game screen
# 2- Update game screen
# 3- Play turn 
# 4- Check win
#
# Full idea evolution at the bottom + posible UPGRADES
#---------------------------------------
mx = [["0","1","0"],["0","0","0"],["0","2","0"]]
options = {"0":"X","1":"O","2":" "}
ableMoves = ["00","01","02","10","11","12","20","21","22"]
global stillPlaying 
global turn

# Execution of game
def executeGame():
    resetGame()
    showGame()
    turn=0
    stillPlaying=True
    while(stillPlaying):
        player=turn%2
        playerMove(player)
        showGame()
        if(checkWin(player)):
            break
        turn+=1
        
    # keep playing?
    keepPlaying=input("KEEP PLAYING?(Y,n)")
    if(keepPlaying=="Y"):
        executeGame()
    

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
def playerMove(player):
    pos=input("Player "+options.get(str(player),"NF")+" move: ")
    if(checkAbleMove(pos)): 
        x=int(pos[0])
        y=int(pos[1])
        if(checkEmptySpace(x,y)):
            mx[x][y] = str(player)
        else:
            print("Unable move")
            playerMove(player)
    else:
        print("Unable move")
        playerMove(player)

# -CHECK WIN-
def checkWin(player):
    if(checkRow(player) or checkColumn(player) or checkDiagonal(player)):
        print("Player "+str(player)+" WINS")
        stillPlaying = False
        return True

#Check rows for a win
def checkRow(player):
    for i in range(0,3):
        if(mx[i][0]==str(player) and mx[i][0]==mx[i][1] and mx[i][0]==mx[i][2]):
            print("row"+str(i))
            return True
    return False

#Check columns for a win
def checkColumn(player):
    for i in range(0,3):
        if(mx[0][i]==str(player) and mx[0][i]==mx[1][i] and mx[0][i]==mx[2][i]):
            print("column"+str(i))
            return True
    return False

#Check diagonals for a win
def checkDiagonal(player):
    #from TopLeft to BottomRight
    if(mx[0][0]==str(player) and mx[0][0]==mx[1][1] and mx[0][0]==mx[2][2]):
        print("TL")
        return True
    #form TopRight to BottomLeft  
    if(mx[0][2]==str(player) and mx[0][2]==mx[1][1] and mx[0][2]==mx[2][0]):
        print("TR")
        return True
    return False

#---------------------------------------
# Upgrade
# Check move is inside matrix
def checkAbleMove(move):
    if(move in ableMoves):
        return True
    if(move=="c"):  
        exit("Game END")
    return False

# Check move is empty on matrix
def checkEmptySpace(x,y):
    if(mx[x][y]=="2"):
        return True
    return False

#---------------------------------------
print("Game START")
#showGame()  
#resetGame()
#playerMove(0)
#checkRow(0)
#checkColumn(0)
#checkDiagonal(0)
executeGame()





#---------------------------------------
# - Variables needed
# matrix(3x3) -> Use as base for the game 
# X and O -> for players
# Array(3) -> Options for the matrix values (0,1,2)
#
# - Functions evolution
# 1 Initiate game -> use 'generateGame()' to reset all the values of matrix, then print the matrix with 'showGame()'
# 2 Update game -> use 'showGame()' after each player takes a turn
# 3 Play turn -> use 'playerMove(player)' player depends by round number using (0,1) as players values. Player gives an input of 2 numbers as 00-22
# 4 Check win -> use 'checkWin()' to verify all posible wins; look at columns, rows and diagonal
#
#---------------------------------------
# Posible UPGRADES
# +check player input to be correct -> use exist on array
# +check player move is empty -> check if the matrix is empty("2")
