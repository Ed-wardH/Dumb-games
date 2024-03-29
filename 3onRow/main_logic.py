# Basic function ideas needed
# 1- Draw Initial game screen
# 2- Update game screen
# 3- Play turn 
# 4- Check win
#
# Full idea evolution at the bottom
#---------------------------------------
matrix = [["0","0","0"],["0","1","0"],["0","2","0"]]
options = {"0":"X","1":"O","2":" "}
stillPlaying = True

# Show actual state of game
def showGame():
    print("")
    line="|"
    for i in range(0,3):
        for j in range(0,3):
            line += options.get(matrix[i][j],"NF")
            line += "|"
        print(line)
        line="|"

# Generate/reset game
def resetGame():   
    for i in range(0,3):
        for j in range(0,3):
            matrix[i][j]="2" 

# Set the player move by position
def playerMove(player):
    pos=input("Player "+str(player)+" move: ")
    x=int(pos[0])
    y=int(pos[1])
    matrix[x][y] = str(player)



#---------------------------------------
print("Game START")
#showGame()  
#generateGame()
#showGame()
showGame()





#---------------------------------------
# - Variables needed
# Matrix(3x3) -> Use as base for the game 
# X and O -> for players
# Array(3) -> Options for the matrix values (0,1,2)
#
# - Functions evolution
# 1 Initiate game -> use 'generateGame()' to reset all the values of matrix, then print the matrix with 'showGame()'
# 2 Update game -> use 'showGame()' after each player takes a turn
# 3 Play turn -> use 'playerMove(player)' player depends by round number using (0,1) as players values. Player gives an input of 2 numbers as 00-22
# 4 Check win -> use 'checkWin()' to verify all posible wins; look at columns, rows and diagonal
#
#
