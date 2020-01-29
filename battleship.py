# This is a stupidly inefficient but nevertheless funtional attempt at Battleship with fully functioning AI, no special libraries.
from random import randint
import copy
# List declarations
boardP = [["   ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"],
          ["A: ", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
          ["B: ", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
          ["C: ", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
          ["D: ", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
          ["E: ", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
          ["F: ", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
          ["G: ", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
          ["H: ", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
          ["I: ", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
          ["J: ", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
          ["K: ", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]

boardBot = copy.deepcopy(boardP)
boardBotDisplay = copy.deepcopy(boardP)
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
    print("\n\n        Welcome to my Battleship game!\n        Each ship space is marked with it's corresponding starting letter")
    print("\n\n        If you hit the opponents space, the '?' will turn into a '!'")
    print("\n        If you destroy an opponents ship, the '!' marks each turn into a '*'")
    print("\n        Below your 4 ships are listed: a Battleship, a Cruiser, a Frigate, and a GunBoat -->")
    print("\n\n     B  C  F  G\n     B  C  F  G\n     B  C  F\n     B  C\n     B")
    print("\n\n     Enter each space for your ships by typing in the corresponding spot such as 'A5':")


# Initialize placement of Player ships
def placementInit(inputstring, shippiece):
    stringIn = inputstring[0]
    length = len(inputstring)
    if length == 3:
        numberIn = int(inputstring[2])
        if numberIn == 0:
            check = placement(stringIn, 10, shippiece)
            if check:
                return True
            else:
                return False
        elif numberIn == 1:
            check = placement(stringIn, 11, shippiece)
            if check:
                return True
            else:
                return False
    elif length == 2:
        numberIn = int(inputstring[1])
        check = placement(stringIn, numberIn, shippiece)
        if check:
            return True
        else:
            return False
    else:
        print('Invalid input length provided!')
        return False

# Handle placement of Player ships
def placement(stringinput, numberinput, shippiece):
    numberIn = numberinput
    if stringinput == "A" or stringinput == "a":
        if boardP[1][numberIn] == ".":
            boardP[1][numberIn] = shippiece
        else:
            return False
    elif stringinput == "B" or stringinput == "b":
        if boardP[2][numberIn] == ".":
            boardP[2][numberIn] = shippiece
        else:
            return False
    elif stringinput == "C" or stringinput == "c":
        if boardP[3][numberIn] == ".":
            boardP[3][numberIn] = shippiece
        else:
            return False
    elif stringinput == "D" or stringinput == "d":
        if boardP[4][numberIn] == ".":
            boardP[4][numberIn] = shippiece
        else:
            return False
    elif stringinput == "E" or stringinput == "e":
        if boardP[5][numberIn] == ".":
            boardP[5][numberIn] = shippiece
        else:
            return False
    elif stringinput == "F" or stringinput == "f":
        if boardP[6][numberIn] == ".":
            boardP[6][numberIn] = shippiece
        else:
            return False
    elif stringinput == "G" or stringinput == "g":
        if boardP[7][numberIn] == ".":
            boardP[7][numberIn] = shippiece
        else:
            return False
    elif stringinput == "H" or stringinput == "h":
        if boardP[8][numberIn] == ".":
            boardP[8][numberIn] = shippiece
        else:
            return False
    elif stringinput == "I" or stringinput == "i":
        if boardP[9][numberIn] == ".":
            boardP[9][numberIn] = shippiece
        else:
            return False
    elif stringinput == "J" or stringinput == "j":
        if boardP[10][numberIn] == ".":
            boardP[10][numberIn] = shippiece
        else:
            return False
    elif stringinput == "K" or stringinput == "k":
        if boardP[11][numberIn] == ".":
            boardP[11][numberIn] = shippiece
        else:
            return False
    return True

# Handles placement of AI ship spots
# Extends list to allow bot to check out of bounds
def botPlacement():
    # Extend first 12 rows 5 spaces to the left
    for i in range(0, 12):
        for j in range(-6, 0):
            boardBot[j][i] = ""
    # Extend last 12 rows 5 spaces to the right
    for i in range(0, 12):
        for j in range(12, 18):
            boardBot[i][j] = ""
    # Extend top of list up 5 spaces
    for i in range(0, 12):
        for j in range(-6, 0):
            boardBot[i][j] = ""
    # Extend bottom of list down 5 spaces
    for i in range(0, 12):
        for j in range(12, 18):
            boardBot[j][i] = ""

    # Generate random initial spot for ship placement
    x = 1
    while x < 5:
        randRowInit = randint(1, 12)
        randColInit = randint(1, 12)
        
        # Place Battleship spots
        
        if x == 1:
            initCheck = True
            if boardBot[randRowInit][randColInit] == ".":
                boardBot[randRowInit][randColInit] = "B"
            else:
                initCheck = False
                
            # Give bot a random direction (up, down, left, right) to continue spot placement
            
            if initCheck:
                continueCheck = True
                while continueCheck:
                    randDirection = randint(1, 5)
                    
                    # Check and place next 4 spots down
                    
                    finalLoop = 1
                    finalCheck = True
                    if randDirection == 1:
                        while finalLoop < 5:
                           if boardBot[randColInit + finalLoop][randColInit] != ".":
                               finalCheck = False
                               finalLoop = 5
                           else:
                               finalLoop += 1
                        if finalCheck:
                            for i in range(1, 5):
                                boardBot[randColInit + i][randColInit] = "B"
                                continueCheck = False
                               
                    # Check and place next 4 spots up
                    
                    elif randDirection == 2:
                        while finalLoop < 5:
                            if boardBot[randColInit - finalLoop][randColInit] != ".":
                                finalCheck = False
                                finalLoop = 5
                            else:
                                finalLoop += 1
                        if finalCheck:
                            for i in range(1, 5):
                                boardBot[randColInit - i][randColInit] = "B"
                                continueCheck = False
                                
                    # Check and place next 4 spots left
                    
                    elif randDirection == 3:
                        while finalLoop < 5:
                            if boardBot[randColInit][randColInit - finalLoop] != ".":
                                finalCheck = False
                                finalLoop = 5
                            else:
                                finalLoop += 1
                        if finalCheck:
                            for i in range(1, 5):
                                boardBot[randColInit][randColInit - i] = "B"
                                continueCheck = False

                    # Check and place next 4 spots right
                    
                    elif randDirection == 4:
                        while finalLoop < 5:
                            if boardBot[randColInit][randColInit + finalLoop] != ".":
                                finalCheck = False
                                finalLoop = 5
                            else:
                                finalLoop += 1
                        if finalCheck:
                            for i in range(1, 5):
                                boardBot[randColInit][randColInit + i] = "B"
                                continueCheck = False
                    x += 1

        # Place Cruiser spots

        elif x == 2:
            initCheck = True
            if boardBot[randRowInit][randColInit] == ".":
                boardBot[randRowInit][randColInit] = "C"
            else:
                initCheck = False

            # Give bot a random direction (up, down, left, right) to continue spot placement

            if initCheck:
                continueCheck = True
                while continueCheck:
                    randDirection = randint(1, 5)

                    # Check and place next 3 spots down

                    finalLoop = 1
                    finalCheck = True
                    if randDirection == 1:
                        while finalLoop < 4:
                            if boardBot[randColInit + finalLoop][randColInit] != ".":
                                finalCheck = False
                                finalLoop = 4
                            else:
                                finalLoop += 1
                        if finalCheck:
                            for i in range(1, 4):
                                boardBot[randColInit + i][randColInit] = "C"
                                continueCheck = False

                    # Check and place next 3 spots up

                    elif randDirection == 2:
                        while finalLoop < 4:
                            if boardBot[randColInit - finalLoop][randColInit] != ".":
                                finalCheck = False
                                finalLoop = 4
                            else:
                                finalLoop += 1
                        if finalCheck:
                            for i in range(1, 4):
                                boardBot[randColInit - i][randColInit] = "C"
                                continueCheck = False

                    # Check and place next 3 spots left

                    elif randDirection == 3:
                        while finalLoop < 4:
                            if boardBot[randColInit][randColInit - finalLoop] != ".":
                                finalCheck = False
                                finalLoop = 4
                            else:
                                finalLoop += 1
                        if finalCheck:
                            for i in range(1, 4):
                                boardBot[randColInit][randColInit - i] = "C"
                                continueCheck = False

                    # Check and place next 3 spots right

                    elif randDirection == 4:
                        while finalLoop < 4:
                            if boardBot[randColInit][randColInit + finalLoop] != ".":
                                finalCheck = False
                                finalLoop = 4
                            else:
                                finalLoop += 1
                        if finalCheck:
                            for i in range(1, 4):
                                boardBot[randColInit][randColInit + i] = "C"
                                continueCheck = False
                    x += 1
                    
        # Place Frigate spots
                    
        elif x == 3:
            initCheck = True
            if boardBot[randRowInit][randColInit] == ".":
                boardBot[randRowInit][randColInit] = "F"
            else:
                initCheck = False

            # Give bot a random direction (up, down, left, right) to continue spot placement

            if initCheck:
                continueCheck = True
                while continueCheck:
                    randDirection = randint(1, 5)

                    # Check and place next 2 spots down

                    finalLoop = 1
                    finalCheck = True
                    if randDirection == 1:
                        while finalLoop < 3:
                            if boardBot[randColInit + finalLoop][randColInit] != ".":
                                finalCheck = False
                                finalLoop = 3
                            else:
                                finalLoop += 1
                        if finalCheck:
                            for i in range(1, 3):
                                boardBot[randColInit + i][randColInit] = "F"
                                continueCheck = False

                    # Check and place next 2 spots up

                    elif randDirection == 2:
                        while finalLoop < 3:
                            if boardBot[randColInit - finalLoop][randColInit] != ".":
                                finalCheck = False
                                finalLoop = 3
                            else:
                                finalLoop += 1
                        if finalCheck:
                            for i in range(1, 3):
                                boardBot[randColInit - i][randColInit] = "F"
                                continueCheck = False

                    # Check and place next 2 spots left

                    elif randDirection == 3:
                        while finalLoop < 3:
                            if boardBot[randColInit][randColInit - finalLoop] != ".":
                                finalCheck = False
                                finalLoop = 3
                            else:
                                finalLoop += 1
                        if finalCheck:
                            for i in range(1, 3):
                                boardBot[randColInit][randColInit - i] = "F"
                                continueCheck = False

                    # Check and place next 2 spots right

                    elif randDirection == 4:
                        while finalLoop < 3:
                            if boardBot[randColInit][randColInit + finalLoop] != ".":
                                finalCheck = False
                                finalLoop = 3
                            else:
                                finalLoop += 1
                        if finalCheck:
                            for i in range(1, 3):
                                boardBot[randColInit][randColInit + i] = "F"
                                continueCheck = False
                    x += 1

        # Place Gunboat spots

        elif x == 4:
            initCheck = True
            if boardBot[randRowInit][randColInit] == ".":
                boardBot[randRowInit][randColInit] = "G"
            else:
                initCheck = False

            # Give bot a random direction (up, down, left, right) to continue spot placement

            if initCheck:
                continueCheck = True
                while continueCheck:
                    randDirection = randint(1, 5)

                    # Check and place next spot down

                    finalLoop = 1
                    finalCheck = True
                    if randDirection == 1:
                        while finalLoop < 2:
                            if boardBot[randColInit + finalLoop][randColInit] != ".":
                                finalCheck = False
                                finalLoop = 2
                            else:
                                finalLoop += 1
                        if finalCheck:
                            for i in range(1, 2):
                                boardBot[randColInit + i][randColInit] = "G"
                                continueCheck = False

                    # Check and place next spot up

                    elif randDirection == 2:
                        while finalLoop < 2:
                            if boardBot[randColInit - finalLoop][randColInit] != ".":
                                finalCheck = False
                                finalLoop = 2
                            else:
                                finalLoop += 1
                        if finalCheck:
                            for i in range(1, 2):
                                boardBot[randColInit - i][randColInit] = "G"
                                continueCheck = False

                    # Check and place next spot left

                    elif randDirection == 3:
                        while finalLoop < 2:
                            if boardBot[randColInit][randColInit - finalLoop] != ".":
                                finalCheck = False
                                finalLoop = 2
                            else:
                                finalLoop += 1
                        if finalCheck:
                            for i in range(1, 2):
                                boardBot[randColInit][randColInit - i] = "G"
                                continueCheck = False

                    # Check and place next spot right

                    elif randDirection == 4:
                        while finalLoop < 2:
                            if boardBot[randColInit][randColInit + finalLoop] != ".":
                                finalCheck = False
                                finalLoop = 2
                            else:
                                finalLoop += 1
                        if finalCheck:
                            for i in range(1, 2):
                                boardBot[randColInit][randColInit + i] = "G"
                                continueCheck = False
                    x += 1
            

# Checks if ship is destroyed
def checkShips():



# Handles input for player ship spots
def createBoard():
    j = 1
    battleshipPiece = "B"
    cruiserPiece = "C"
    frigatePiece = "F"
    gunboatPiece = "G"
    while j < 6:
        printPBoard()
        inputstring = input("\n\nEnter spot " + str(j) + " for your Battleship -->")
        print(inputstring)
        checkSpot = placementInit(inputstring, battleshipPiece)
        if checkSpot:
            j += 1
        else:
            print(inputstring, " is not a valid spot! Choose again -->")
    j = 1
    while j < 5:
        printPBoard()
        inputstring = input("\n\nEnter spot " + str(j) + " for your Cruiser -->")
        print(inputstring)
        checkSpot = placementInit(inputstring, cruiserPiece)
        if checkSpot:
            j += 1
        else:
            print(inputstring, " is not a valid spot! Choose again -->")
    j = 1
    while j < 4:
        printPBoard()
        inputstring = input("\n\nEnter spot " + str(j) + " for your Frigate -->")
        print(inputstring)
        checkSpot = placementInit(inputstring, frigatePiece)
        if checkSpot:
            j += 1
        else:
            print(inputstring, " is not a valid spot! Choose again -->")
    j = 1
    while j < 3:
        printPBoard()
        inputstring = input("\n\nEnter spot " + str(j) + " for your GunBoat -->")
        print(inputstring)
        checkSpot = placementInit(inputstring, gunboatPiece)
        if checkSpot:
            j += 1
        else:
            print(inputstring, " is not a valid spot! Choose again -->")

# Master function

def main():
    gameIntro()
    createBoard()
    printPBoard()


main()

