from random import randint
# List declarations
boardP = [[' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'],
          ['A', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
          ['B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
          ['C', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
          ['D', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
          ['E', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
          ['F', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
          ['G', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
          ['H', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
          ['I', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
          ['J', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
          ['K', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]

boardBot = boardBotDisplay = boardP.copy()
arrayBattleship = [[None for y in range(2)] for x in range(5)]
arrayCruiser = [[None for i in range(2)] for j in range(4)]
arrayFrigate = [[None for a in range(2)] for b in range(3)]
arrayGunboat = [[None for c in range(2)] for d in range(2)]

# Set the bot display board to have '?' spots
for i in range(1, 12):
    for j in range(1, 12):
        boardBotDisplay[i][j] = "?"

# Prints Player board
def printPBoard():
    for i in range(0, 12):
        for j in range(0, 12):
            if j == 0:
                print("\n")
            if i == 0 and j == 10:
                print(boardP[i][j], end="   ")
            else:
                print(boardP[i][j], end="    ")


# Prints Bot board
def printBotBoard():
    for i in range(0, 12):
        for j in range(0, 12):
            if j == 0:
                print("\n")
            if i == 0 and j == 10:
                print(boardBotDisplay[i][j], end="   ")
            else:
                print(boardBotDisplay[i][j], end="    ")

# Prints Bot hidden board for testing purposes
def printBotHidden():
    for i in range(0, 12):
        for j in range(0, 12):
            if j == 0:
                print("\n")
            if i == 0 and j == 10:
                print(boardBot[i][j], end="   ")
            else:
                print(boardBot[i][j], end="    ")

# Intro to game and instructions
def gameIntro():
    print("\n\nWelcome to my Battleship game!\nEach ship space is marked with an '+'")
    print("\n\n If you hit the opponents space, the '?' will turn into a '!'")
    print("\n If you destroy an opponents ship, the '!' marks each turn into a '*'")
    print("\n Below your 4 ships are listed: a Battleship, a Cruiser, a Frigate, and a GunBoat -->")
    print("\n\n+  +  +  +\n+  +  +  +\n+  +  +\n+  +\n+")
    print("\n\nEnter each space for your ships by typing in the corresponding spot such as 'A5'")


# Handles placement of Player ships
def placement(userinput):
    stringIn = userinput[0]
    numberIn = int(userinput[1])
    if stringIn == "A" or "a":
        if boardP[1][numberIn] == ".":
            boardP[1][numberIn] = "+"
        else:
            return False
    elif stringIn == "B" or "b":
        if boardP[2][numberIn] == ".":
            boardP[2][numberIn] = "+"
        else:
            return False
    elif stringIn == "C" or "c":
        if boardP[3][numberIn] == ".":
            boardP[3][numberIn] = "+"
        else:
            return False
    elif stringIn == "D" or "d":
        if boardP[4][numberIn] == ".":
            boardP[4][numberIn] = "+"
        else:
            return False
    elif stringIn == "E" or "e":
        if boardP[5][numberIn] == ".":
            boardP[5][numberIn] = "+"
        else:
            return False
    elif stringIn == "F" or "f":
        if boardP[6][numberIn] == ".":
            boardP[6][numberIn] = "+"
        else:
            return False
    elif stringIn == "G" or "g":
        if boardP[7][numberIn] == ".":
            boardP[7][numberIn] = "+"
        else:
            return False
    elif stringIn == "H" or "h":
        if boardP[8][numberIn] == ".":
            boardP[8][numberIn] = "+"
        else:
            return False
    elif stringIn == "I" or "i":
        if boardP[9][numberIn] == ".":
            boardP[9][numberIn] = "+"
        else:
            return False
    elif stringIn == "J" or "j":
        if boardP[10][numberIn] == ".":
            boardP[10][numberIn] = "+"
        else:
            return False
    elif stringIn == "K" or "k":
        if boardP[11][numberIn] == ".":
            boardP[11][numberIn] = "+"
        else:
            return False
    return True

# Handles placement of AI ship spots

def botBoard(shiptype):
    # Designate ship type
    if shiptype == 1:
        #C heck if initial placement is valid
        initialCheck = True
        directionCheck = True
        while initialCheck:
            randomRow = randint(1, 12)
            randomCol = randint(1, 12)
            if boardBot[randomRow][randomCol] == ".":
                boardBot[randomRow][randomCol] = "+"
                # Set hidden board and the ship's array the new spot
                # Ship array: dump the coordinate row and col in ship's array
                arrayBattleship[0][0] = randomRow
                arrayBattleship[0][1] = randomCol
            else:
                initialCheck = False
            if initialCheck:
                while directionCheck:
                    randomDirection = randint(1, 5)
                    #Use for loop to check
                    if randomDirection == 1:
                        if boardBot[randomRow + 1][randomCol] == ".":
                            if boardBot[randomRow + 2][randomCol] == ".":
                                if boardBot[randomRow + 3][randomCol] == ".":
                                    if boardBot[randomRow + 4][randomCol] == ".":
                                        for i in range(1, 5):
                                            boardBot[randomRow + i][randomCol] = "+"
                                            arrayBattleship[i][0] = randomRow + i
                                            arrayBattleship[i][1] = randomCol
                        else:
                            directionCheck = False

                    if randomDirection == 2:
                        if boardBot[randomRow - 1][randomCol] == ".":
                            if boardBot[randomRow - 2][randomCol] == ".":
                                if boardBot[randomRow - 3][randomCol] == ".":
                                    if boardBot[randomRow - 4][randomCol] == ".":
                                        for i in range(1, 5):
                                            boardBot[randomRow - i][randomCol] = "+"
                                            arrayBattleship[i][0] = randomRow - i
                                            arrayBattleship[i][1] = randomCol
                        else:
                            directionCheck = False

                    if randomDirection == 3:
                        if boardBot[randomRow][randomCol + 1] == ".":
                            if boardBot[randomRow][randomCol + 1] == ".":
                                if boardBot[randomRow][randomCol + 1] == ".":
                                    if boardBot[randomRow][randomCol + 1] == ".":
                                        for i in range(1, 5):
                                            boardBot[randomRow][randomCol + i] = "+"
                                            arrayBattleship[i][0] = randomRow
                                            arrayBattleship[i][1] = randomCol + i
                        else:
                            directionCheck = False

                    if randomDirection == 4:
                        if boardBot[randomRow][randomCol - 1] == ".":
                            if boardBot[randomRow][randomCol - 1] == ".":
                                if boardBot[randomRow][randomCol - 1] == ".":
                                    if boardBot[randomRow][randomCol - 1] == ".":
                                        for i in range(1, 5):
                                            boardBot[randomRow][randomCol - i] = "+"
                                            arrayBattleship[i][0] = randomRow
                                            arrayBattleship[i][1] = randomCol - i
                        else:
                            directionCheck = False

# Input and check validity of chosen spot
def createBoard():
    j = 1
    while j < 6:
        printPBoard()
        inputString = input("\n\nEnter spot " + str(j) + " for your Battleship -->")
        print(inputString)
        checkSpot = placement(inputString)
        if not checkSpot:
            print(inputString, " is not a valid spot! Choose again -->")
        else:
            j += 1
    j = 1
    while j < 5:
        printPBoard()
        inputString = input("\n\nEnter spot " + str(j) + " for your Cruiser -->")
        print(inputString)
        placement(inputString)
        checkSpot = placement(inputString)
        if not checkSpot:
            print(inputString, " is not a valid spot! Choose again -->")
        else:
            j += 1
    j = 1
    while j < 4:
        printPBoard()
        inputString = input("\n\nEnter spot " + str(j) + " for your Frigate -->")
        print(inputString)
        placement(inputString)
        checkSpot = placement(inputString)
        if not checkSpot:
            print(inputString, " is not a valid spot! Choose again -->")
        else:
            j += 1
    j = 1
    while j < 3:
        printPBoard()
        inputString = input("\n\nEnter spot " + str(j) + " for your GunBoat -->")
        print(inputString)
        placement(inputString)
        checkSpot = placement(inputString)
        if not checkSpot:
            print(inputString, " is not a valid spot! Choose again -->")
        else:
            j += 1


# Master function
def playGame():
    # gameIntro()
    # createBoard()
    for i in range(1, 2):
        botBoard(i)
    printBotHidden()


playGame()
