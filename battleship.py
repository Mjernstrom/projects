import random
from random import randint
import copy
from os import system, name

# Author: Matthew Jernstrom
# Written in January of 2020

# This is clearly a way over-written file, but my working knowledge was pretty limited at the time this was made.

# Function directory (shows general order of function calls):

# main: handles game loop
# gameIntro: introduce game instructions
# createBoard: handle player input to place player ships
# placementInit: checks size of player input and prep's input to the placement function
# Placement: converts string input to coordinates and performs placement
# printBoards: I used a big space string to display both boards side by side
# botPlacement: uses random generation and a massive amount of checks to create a valid board. Delete comment on
# the function call in the main loop to check it out in action
# turn: handles both player and bot turn. Checks game counters for game condition
# botIntelligence: keeps track of multiple coordinates and attacks sort of like a human

# Create board arrays

boardP = [["." for i in range(13)] for j in range(13)]
boardP[0][0] = " "
for i in range(0, 13):
    if i > 0:
        boardP[0][i] = i
        if i < 12:
            boardP[i][0] = str(chr(i + 64))
        else:
            for j in range(0, 13):
                boardP[i][j] = " "
                boardP[j][i] = " "
boardPcopy = copy.deepcopy(boardP)

boardBot = [["." for i in range(20)] for j in range(20)]
boardInt = 1
for i in range(0, 20):
    for j in range(0, 20):
        if i == 0:
            if j <= 4 or j > 15:
                boardBot[i][j] = " "
            else:
                boardBot[i][j] = boardInt
                boardInt += 1
        elif i <= 4 or i > 15:
            if j <= 4 or j > 15:
                boardBot[i][j] = " "
            else:
                boardBot[i][j] = "#"
        else:
            if j < 5 or j > 15:
                boardBot[i][j] = "#"

# Create AI choice index's

# If in hit mode, choose to attack in 1 of 4 directions
# Each value in the list represents an attack direction. 1 is up, 2 is down, 3 is left, 4 is right
# If a direction returns a miss, removes the direction from list
# If the spot turns into a '#', it will reset bot back to random selection
# If this list manages to have all it's contents deleted, reset bot back to random selection

directionChoice = [1, 2, 3, 4]
direction = 0

# This list is created to store the original spot of the hit in order to ensure the bot can
# return to it to keep searching for the rest of the ship's pieces
# The second pair of coordinates in the list is there to ensure the bot keeps hitting in the same direction

attackMode = 0
tracking = [0, 0, 0, 0]

# Create a few counters to keep track of how many spots of each ship were hit,
# as well as a counter tracking how many ships were sunk

bShipBot = 0
frigBot = 0
cruBot = 0
gbBot = 0
bShipPl = 0
frigPl = 0
cruPl = 0
gbPl = 0
botSunk = 0
plSunk = 0


# Function to clear window

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

# Create and set the bot display board to have '?' spots

boardBotDisplay = copy.deepcopy(boardP)

for i in range(1, 12):
    for j in range(1, 12):
        boardBotDisplay[i][j] = "?"

# Print player and bot board side by side

def printBoards():
    for i in range(0, 12):
        for j in range(0, 12):
            if j == 0:
                print("\n")
            if i == 0 and j == 10:
                print(boardP[i][j], end="   ")
            elif j < 11:
                print(boardP[i][j], end="    ")
            else:
                print(boardP[i][j], end="                   ")
                for x in range(0, 12):
                    if i == 0 and x == 10:
                        print(boardP[i][x], end="   ")
                    else:
                        print(boardBotDisplay[i][x], end="     ")

# Prints Bot hidden board for testing purposes

def printBotHidden():
    for i in range(5, 16):
        for j in range(5, 16):
            if j == 0:
                print("\n")
            print(boardBot[i][j], end="     ")


# Intro to game and instructions

def gameIntro():
    print("\n\n        Welcome to my Battleship game!\n        Each ship space is marked with it's corresponding",
          "beginning letter\n\n        If you hit the opponents space, the '?' will turn into a '#'",
          "\n\n        If you hit the opponents space, the '?' will turn into a '!'",
          "\n        If you destroy an opponents ship, the '#' marks each turn into a '*'",
          "\n        Below your 4 ships are listed: a Battleship, a Cruiser, a Frigate, and a GunBoat -->",
          "\n\n     B  C  F  G\n     B  C  F  G\n     B  C  F\n     B  C\n     B",
          "\n\n     Enter each space for your ships by typing in the corresponding spot exactly like so: 'A1d'",
          "\n       Where A1 is the initial spot placement and d means down. Use r for right, l for left, and u for up",
          "\n\n     Your board is displayed on the left, the bot's board is displayed to the right:")


# Handles placement of AI ship spots

def botPlacement():
    x = 1
    # Extend bot board

    # Generate random initial spot for ship placement

    while x < 5:
        randRowInit = randint(5, 16)
        randColInit = randint(5, 16)

        # Place Battleship spots

        if x == 1:
            boardBot[randRowInit][randColInit] = "B"

            # Give bot a random direction (up, down, left, right) to continue spot placement

            continueCheck = True
            while continueCheck:
                randDirection = randint(1, 5)
                finalLoop = 1
                finalCheck = True

                # Check and place next 4 spots down

                if randDirection == 1:
                    while finalLoop < 5:
                        if boardBot[randRowInit + finalLoop][randColInit] != ".":
                            finalCheck = False
                            finalLoop = 5
                        else:
                            finalLoop += 1
                    if finalCheck:
                        for i in range(1, 5):
                            boardBot[randRowInit + i][randColInit] = "B"
                        continueCheck = False
                        x += 1

                # Check and place next 4 spots up

                elif randDirection == 2:
                    while finalLoop < 5:
                        if boardBot[randRowInit - finalLoop][randColInit] != ".":
                            finalCheck = False
                            finalLoop = 5
                        else:
                            finalLoop += 1
                    if finalCheck:
                        for i in range(1, 5):
                            boardBot[randRowInit - i][randColInit] = "B"
                        continueCheck = False
                        x += 1

                # Check and place next 4 spots left

                elif randDirection == 3:
                    while finalLoop < 5:
                        if boardBot[randRowInit][randColInit - finalLoop] != ".":
                            finalCheck = False
                            finalLoop = 5
                        else:
                            finalLoop += 1
                    if finalCheck:
                        for i in range(1, 5):
                            boardBot[randRowInit][randColInit - i] = "B"
                        continueCheck = False
                        x += 1

                # Check and place next 4 spots right

                elif randDirection == 4:
                    while finalLoop < 5:
                        if boardBot[randRowInit][randColInit + finalLoop] != ".":
                            finalCheck = False
                            finalLoop = 5
                        else:
                            finalLoop += 1
                    if finalCheck:
                        for i in range(1, 5):
                            boardBot[randRowInit][randColInit + i] = "B"
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
                            if boardBot[randRowInit + finalLoop][randColInit] != ".":
                                finalCheck = False
                                finalLoop = 4
                            else:
                                finalLoop += 1
                        if finalCheck:
                            for i in range(1, 4):
                                boardBot[randRowInit + i][randColInit] = "C"
                                continueCheck = False
                                x = 3

                    # Check and place next 3 spots up

                    elif randDirection == 2:
                        while finalLoop < 4:
                            if boardBot[randRowInit - finalLoop][randColInit] != ".":
                                finalCheck = False
                                finalLoop = 4
                            else:
                                finalLoop += 1
                        if finalCheck:
                            for i in range(1, 4):
                                boardBot[randRowInit - i][randColInit] = "C"
                                continueCheck = False
                                x = 3

                    # Check and place next 3 spots left

                    elif randDirection == 3:
                        while finalLoop < 4:
                            if boardBot[randRowInit][randColInit - finalLoop] != ".":
                                finalCheck = False
                                finalLoop = 4
                            else:
                                finalLoop += 1
                        if finalCheck:
                            for i in range(1, 4):
                                boardBot[randRowInit][randColInit - i] = "C"
                                continueCheck = False
                                x = 3

                    # Check and place next 3 spots right

                    elif randDirection == 4:
                        while finalLoop < 4:
                            if boardBot[randRowInit][randColInit + finalLoop] != ".":
                                finalCheck = False
                                finalLoop = 4
                            else:
                                finalLoop += 1
                        if finalCheck:
                            for i in range(1, 4):
                                boardBot[randRowInit][randColInit + i] = "C"
                                continueCheck = False
                                x = 3

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
                            if boardBot[randRowInit + finalLoop][randColInit] != ".":
                                finalCheck = False
                                finalLoop = 3
                            else:
                                finalLoop += 1
                        if finalCheck:
                            for i in range(1, 3):
                                boardBot[randRowInit + i][randColInit] = "F"
                                continueCheck = False
                                x = 4

                    # Check and place next 2 spots up

                    elif randDirection == 2:
                        while finalLoop < 3:
                            if boardBot[randRowInit - finalLoop][randColInit] != ".":
                                finalCheck = False
                                finalLoop = 3
                            else:
                                finalLoop += 1
                        if finalCheck:
                            for i in range(1, 3):
                                boardBot[randRowInit - i][randColInit] = "F"
                                continueCheck = False
                                x = 4

                    # Check and place next 2 spots left

                    elif randDirection == 3:
                        while finalLoop < 3:
                            if boardBot[randRowInit][randColInit - finalLoop] != ".":
                                finalCheck = False
                                finalLoop = 3
                            else:
                                finalLoop += 1
                        if finalCheck:
                            for i in range(1, 3):
                                boardBot[randRowInit][randColInit - i] = "F"
                                continueCheck = False
                                x = 4

                    # Check and place next 2 spots right

                    elif randDirection == 4:
                        while finalLoop < 3:
                            if boardBot[randRowInit][randColInit + finalLoop] != ".":
                                finalCheck = False
                                finalLoop = 3
                            else:
                                finalLoop += 1
                        if finalCheck:
                            for i in range(1, 3):
                                boardBot[randRowInit][randColInit + i] = "F"
                                continueCheck = False
                                x = 4

        # Place Gunboat spots

        elif x == 4:
            randRowInit = randint(5, 16)
            randColInit = randint(5, 16)
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
                            if boardBot[randRowInit + finalLoop][randColInit] != ".":
                                finalCheck = False
                                finalLoop = 2
                            else:
                                finalLoop += 1
                        if finalCheck:
                            for i in range(1, 2):
                                boardBot[randRowInit + i][randColInit] = "G"
                                continueCheck = False
                                x += 1

                    # Check and place next spot up

                    elif randDirection == 2:
                        while finalLoop < 2:
                            if boardBot[randRowInit - finalLoop][randColInit] != ".":
                                finalCheck = False
                                finalLoop = 2
                            else:
                                finalLoop += 1
                        if finalCheck:
                            for i in range(1, 2):
                                boardBot[randRowInit - i][randColInit] = "G"
                                continueCheck = False
                                x += 1

                    # Check and place next spot left

                    elif randDirection == 3:
                        while finalLoop < 2:
                            if boardBot[randRowInit][randColInit - finalLoop] != ".":
                                finalCheck = False
                                finalLoop = 2
                            else:
                                finalLoop += 1
                        if finalCheck:
                            for i in range(1, 2):
                                boardBot[randRowInit][randColInit - i] = "G"
                                continueCheck = False
                                x += 1

                    # Check and place next spot right

                    elif randDirection == 4:
                        while finalLoop < 2:
                            if boardBot[randRowInit][randColInit + finalLoop] != ".":
                                finalCheck = False
                                finalLoop = 2
                            else:
                                finalLoop += 1
                        if finalCheck:
                            for i in range(1, 2):
                                boardBot[randRowInit][randColInit + i] = "G"
                                continueCheck = False
                                x += 1

# Initialize placement of Player ships

def placementInit(inputstring, shippiece):
    stringIn = inputstring
    length = len(inputstring)

    # If player inputs column 10 or 11, we want access to 3 string elements:

    if length == 4:
        numberIn = int(inputstring[2])
        directionInput = inputstring[3].upper()
        if numberIn == 0:
            check = placement(stringIn, 10, shippiece, directionInput)
            if check:
                return True
            else:
                return False
        elif numberIn == 1:
            check = placement(stringIn, 11, shippiece, directionInput)
            if check:
                return True
            else:
                return False

    # If spot is in column 1-9:

    elif length == 3:
        directionInput = inputstring[2].upper()
        numberIn = int(inputstring[1])
        check = placement(stringIn, numberIn, shippiece, directionInput)
        if check:
            return True
        else:
            return False
    else:
        print('Invalid input length provided!')
        return False


# Handle placement of Player ships

def placement(stringinput, numberinput, shippiece, directioninput):
    # Convert string to row:
    charToInt = ord(stringinput[0])
    placeCount = 0

    # Set range for spot checks
    if shippiece == "B":
        placeCount = 5
    elif shippiece == "C":
        placeCount = 4
    elif shippiece == "F":
        placeCount = 3
    elif shippiece == "G":
        placeCount = 2

    if directioninput == "D":
        for x in range(0, placeCount):
            if boardP[charToInt - 64 + x][numberinput] != ".":
                return False
        for x in range(0, placeCount):
            boardP[charToInt - 64 + x][numberinput] = shippiece
        return True
    elif directioninput == "U":
        for x in range(0, placeCount):
            if boardP[charToInt - 64 - x][numberinput] != ".":
                return False
        for x in range(0, placeCount):
            boardP[charToInt - 64 - x][numberinput] = shippiece
        return True
    elif directioninput == "L":
        for x in range(0, placeCount):
            if boardP[charToInt - 64][numberinput - x] != ".":
                return False
        for x in range(0, placeCount):
            boardP[charToInt - 64][numberinput - x] = shippiece
        return True
    elif directioninput == "R":
        for x in range(0, placeCount):
            if boardP[charToInt - 64][numberinput + x] != ".":
                return False
        for x in range(0, placeCount):
            boardP[charToInt - 64][numberinput + x] = shippiece
        return True
    else:
        return False


# Handles input for player ship spots

def createBoard():
    global boardPcopy
    j = 0
    battleshipPiece = "B"
    cruiserPiece = "C"
    frigatePiece = "F"
    gunboatPiece = "G"
    while j == 0:
        printBoards()
        inputstring = input("\n\nEnter initial spot followed by direction for your Battleship -->")
        print(inputstring)
        checkSpot = placementInit(inputstring.upper(), battleshipPiece)
        if checkSpot:
            j += 1
        else:
            print(inputstring, " is not a valid spot! Choose again -->")
    j = 0
    while j == 0:
        printBoards()
        inputstring = input("\n\nEnter spot initial spot followed by direction for your Cruiser -->")
        print(inputstring)
        checkSpot = placementInit(inputstring.upper(), cruiserPiece)
        if checkSpot:
            j += 1
        else:
            print(inputstring, " is not a valid spot! Choose again -->")
    j = 0
    while j == 0:
        printBoards()
        inputstring = input("\n\nEnter spot initial spot followed by direction for your Frigate -->")
        print(inputstring)
        checkSpot = placementInit(inputstring.upper(), frigatePiece)
        if checkSpot:
            j += 1
        else:
            print(inputstring, " is not a valid spot! Choose again -->")
    j = 0
    while j == 0:
        printBoards()
        inputstring = input("\n\nEnter spot initial spot followed by direction for your GunBoat -->")
        print(inputstring)
        checkSpot = placementInit(inputstring.upper(), gunboatPiece)
        if checkSpot:
            j += 1
        else:
            print(inputstring, " is not a valid spot! Choose again -->")
    boardPcopy = copy.deepcopy(boardP)


# Handle's turns
# Returns 0 if player choice is invalid or bot misses
# Returns 1 if player wins
# Returns 2 if bot wins
# Return True if game continues

def turn(spot, user, directionchoice):
    # Allow function to modify game counters
    global direction
    global directionChoice
    global tracking
    global attackMode
    global bShipBot
    global frigBot
    global cruBot
    global gbBot
    global bShipPl
    global frigPl
    global cruPl
    global gbPl
    global botSunk
    global plSunk
    length = len(spot)

    if length < 2:
        if user == 1:
            print("\nInvalid input, choose again:")
            return 0
        else:
            return 0

    numberIn = int(spot[1])

    # Convert the first part of the string to it's corresponding row number

    row = ord(spot[0])
    if row <= 75:
        row -= 64
    else:
        row -= 96

    # Check col number and make comparisons

    if length == 3:

        numberIn = int(spot[2])

        if numberIn > 1:
            if user == 1:
                print("\nInvalid input, choose again:")
                return 0
            else:
                return 0

        # Checks if hit or miss for the 10th column on player or bot's turn, increments hit counter if hit

        if numberIn == 0:
            if user == 1:
                if boardBotDisplay[row][10] == "#" or boardBotDisplay[row][10] == "*":
                    print("\nSpot already hit, choose again:")
                    return 0
                elif boardBot[row + 4][14] != ".":
                    if boardBot[row + 4][14] == "B":
                        bShipBot += 1
                    elif boardBot[row + 4][14] == "C":
                        cruBot += 1
                    elif boardBot[row + 4][14] == "F":
                        frigBot += 1
                    elif boardBot[row + 4][14] == "G":
                        gbBot += 1
                    boardBotDisplay[row][10] = "#"
                    print("\nHIT!")
                else:
                    print("\nMISS!")
            elif user == 2:
                if boardP[row][10] == "#" or boardP[row][10] == "*" or boardP[row][10] == ".":
                    if attackMode == 2:
                        for i in range(2, 4):
                            tracking[i] = 0
                            attackMode = 1
                        for deleteDirection in range(0, 4):
                            if direction == directionChoice[deleteDirection]:
                                directionChoice[deleteDirection] = 0
                        print("\nBot MISSED!")
                    elif attackMode == 1:
                        if directionchoice == 1:
                            directionChoice[0] = 0
                        elif directionchoice == 2:
                            directionChoice[1] = 0
                        elif directionchoice == 3:
                            directionChoice[2] = 0
                        elif directionchoice == 4:
                            directionChoice[3] = 0
                        print("\nBot MISSED!")
                    else:
                        print("\nBot MISSED!")
                else:
                    if boardP[row][10] == "B":
                        bShipPl += 1
                    elif boardP[row][10] == "C":
                        cruPl += 1
                    elif boardP[row][10] == "F":
                        frigPl += 1
                    elif boardP[row][10] == "G":
                        gbPl += 1
                    boardP[row][10] = "#"
                    print("\nYou have been hit!")
                    if attackMode == 0:
                        tracking[0] = row
                        tracking[1] = 10
                        attackMode = 1
                    elif attackMode == 1:
                        tracking[2] = row
                        tracking[3] = 10
                        attackMode = 2
                    elif attackMode == 2:
                        tracking[2] = row
                        tracking[3] = 10

        # Checks if hit or miss for the 11th column on player or bot's turn, increments hit counter if hit

        elif numberIn == 1:
            if user == 1:
                if boardBotDisplay[row][11] == "#" or boardBotDisplay[row][11] == "*":
                    print("\nSpot already hit, choose again:")
                    return 0
                elif boardBot[row + 4][15] != ".":
                    if boardBot[row + 4][15] == "B":
                        bShipBot += 1
                    elif boardBot[row + 4][15] == "C":
                        cruBot += 1
                    elif boardBot[row + 4][15] == "F":
                        frigBot += 1
                    elif boardBot[row + 4][15] == "G":
                        gbBot += 1
                    boardBotDisplay[row][11] = "#"
                    print("\nHIT!")
                else:
                    print("\nMISS!")
            elif user == 2:
                if boardP[row][11] == "#" or boardP[row][11] == "*" or boardP[row][11] == ".":
                    if attackMode == 2:
                        for i in range(2, 4):
                            tracking[i] = 0
                            attackMode = 1
                        for deleteDirection in range(0, 4):
                            if direction == directionChoice[deleteDirection]:
                                directionChoice[deleteDirection] = 0
                        print("\nBot MISSED!")
                    elif attackMode == 1:
                        if directionchoice == 1:
                            directionChoice[0] = 0
                        elif directionchoice == 2:
                            directionChoice[1] = 0
                        elif directionchoice == 3:
                            directionChoice[2] = 0
                        elif directionchoice == 4:
                            directionChoice[3] = 0
                        print("\nBot MISSED!")
                    else:
                        print("\nBot MISSED!")
                else:
                    if boardP[row][11] == "B":
                        bShipPl += 1
                    elif boardP[row][11] == "C":
                        cruPl += 1
                    elif boardP[row][11] == "F":
                        frigPl += 1
                    elif boardP[row][11] == "G":
                        gbPl += 1
                    boardP[row][11] = "#"
                    print("\nYou have been hit!")
                    if attackMode == 0:
                        tracking[0] = row
                        tracking[1] = 11
                        attackMode = 1
                    elif attackMode == 1:
                        tracking[2] = row
                        tracking[3] = 11
                        attackMode = 2
                    elif attackMode == 2:
                        tracking[2] = row
                        tracking[3] = 11

    # Checks if hit or miss for any column less than 10 on player or bot's turn, increments hit counter if hit

    elif length == 2:
        if user == 1:
            if boardBotDisplay[row][numberIn] == "#" or boardBotDisplay[row][numberIn] == "*":
                print("\nSpot already hit, choose again:")
                return 0
            elif boardBot[row + 4][numberIn + 4] != ".":
                if boardBot[row + 4][numberIn + 4] == "B":
                    bShipBot += 1
                elif boardBot[row + 4][numberIn + 4] == "C":
                    cruBot += 1
                elif boardBot[row + 4][numberIn + 4] == "F":
                    frigBot += 1
                elif boardBot[row + 4][numberIn + 4] == "G":
                    gbBot += 1
                boardBotDisplay[row][numberIn] = "#"
                print("\nHIT!")
            else:
                print("\nMISS!")
        elif user == 2:
            if boardP[row][numberIn] == "#" or boardP[row][numberIn] == "*" or boardP[row][numberIn] == ".":
                if attackMode == 2:
                    for i in range(2, 4):
                        tracking[i] = 0
                        attackMode = 1
                    print("\nBot MISSED!")
                elif attackMode == 1:
                    if directionchoice == 1:
                        directionChoice[0] = 0
                    elif directionchoice == 2:
                        directionChoice[1] = 0
                    elif directionchoice == 3:
                        directionChoice[2] = 0
                    elif directionchoice == 4:
                        directionChoice[3] = 0
                    print("\nBot MISSED!")
                else:
                    print("\nBot MISSED!")
            else:
                if boardP[row][numberIn] == "B":
                    bShipPl += 1
                elif boardP[row][numberIn] == "C":
                    cruPl += 1
                elif boardP[row][numberIn] == "F":
                    frigPl += 1
                elif boardP[row][numberIn] == "G":
                    gbPl += 1
                boardP[row][numberIn] = "#"
                print("\nYou have been hit!")
                if attackMode == 0:
                    tracking[0] = row
                    tracking[1] = numberIn
                    attackMode = 1
                elif attackMode == 1:
                    tracking[2] = row
                    tracking[3] = numberIn
                    attackMode = 2
                elif attackMode == 2:
                    tracking[2] = row
                    tracking[3] = numberIn
    else:
        if user == 1:
            print("\nInvalid input, choose again:")
            return 0
        else:
            return 0

    # Check if ship is sunk and increment final game counter accordingly
    # Once bot sinks players ship, resets AI parameters

    if bShipBot == 5:
        print("\nEnemy Battleship sunk!")
        botSunk +=1
        bShipBot = 0
    if cruBot == 4:
        print("\nEnemy Cruiser sunk!")
        botSunk += 1
        cruBot = 0
    if frigBot == 3:
        print("\nEnemy Frigate sunk!")
        botSunk += 1
        frigBot = 0
    if gbBot == 2:
        print("\nEnemy Gunboat sunk!")
        botSunk += 1
        gbBot = 0
    if bShipPl == 5:
        print("\nYour Battleship has been sunk!")
        attackMode = 0
        direction = 0
        for reset in range(0, 4):
            tracking[reset] = 0
            directionChoice[reset] = reset + 1
        plSunk += 1
        bShipPl = 0
    if cruPl == 4:
        print("\nYour Cruiser has been sunk!")
        attackMode = 0
        direction = 0
        for reset in range(0, 4):
            tracking[reset] = 0
            directionChoice[reset] = reset + 1
        plSunk += 1
        cruPl = 0
    if frigPl == 3:
        print("\nYour Frigate has been sunk!")
        attackMode = 0
        direction = 0
        for reset in range(0, 4):
            tracking[reset] = 0
            directionChoice[reset] = reset + 1
        plSunk += 1
        frigPl = 0
    if gbPl == 2:
        print("\nYour Gunboat has been sunk!")
        attackMode = 0
        direction = 0
        for reset in range(0, 4):
            tracking[reset] = 0
            directionChoice[reset] = reset + 1
        plSunk += 1
        gbPl = 0

    # Check win/loss condition

    if botSunk == 4:
        return 3
    if plSunk == 4:
        return 4

    return True

# Handle each bot turn, threw some AI in here
# if 0 is passed in, perform random attack
# If 1, enable hit mode
# if 2, perform track mode

def botIntelligence():
    global attackMode
    attackType = attackMode
    global directionChoice
    global direction
    import random
    spotList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
    returnVal = 0

    # Generate random attack



    # Generate intelligent attack
    # Hit mode enables and can be re-enabled if bot needs to return to original hit position
    # Track mode is when the bot hits multiple spots in a row, so the bot keeps hitting in the specified direction

    if attackType == 1:
        choices = False
        randAttack = 0

        # Check if direction choices list is exhausted:

        for checkChoices in range(0, 4):
            if directionChoice[checkChoices] != 0:
                choices = True
        if choices:
            direction = 0
            randomDir = False
            while not randomDir:
                randAttack = random.choice(directionChoice)
                if randAttack > 0:
                    direction = randAttack
                    randomDir = True
        else:
            tracking[0] = 0
            tracking[1] = 0
            direction = 0
            attackMode = 0
            attackType = 0

        # Attack up 1 row
        if randAttack == 1:
            rowAttackInt = tracking[0] - 1
            rowAttack = spotList[rowAttackInt - 1]
            colAttack = str(tracking[1])
            spot = rowAttack + colAttack
            returnVal = turn(spot, 2, 1)
        # Attack down 1 row
        elif randAttack == 2:
            rowAttackInt = tracking[0] + 1
            rowAttack = spotList[rowAttackInt - 1]
            colAttack = str(tracking[1])
            spot = rowAttack + colAttack
            returnVal = turn(spot, 2, 2)
        # Attack right 1 column
        elif randAttack == 3:
            rowAttackInt = tracking[0]
            colAttackInt = tracking[1] + 1
            rowAttack = spotList[rowAttackInt - 1]
            colAttack = str(colAttackInt)
            spot = rowAttack + colAttack
            returnVal = turn(spot, 2, 3)
        # Attack left 1 column
        elif randAttack == 4:
            rowAttackInt = tracking[0]
            colAttackInt = tracking[1] - 1
            rowAttack = spotList[rowAttackInt - 1]
            colAttack = str(colAttackInt)
            spot = rowAttack + colAttack
            returnVal = turn(spot, 2, 4)

    # Generate random attack

    if attackType == 0:
        randRow = spotList[randint(0, 10)]
        randCol = str(randint(1, 12))
        randomAttack = randRow + randCol
        turn(randomAttack, 2, None)

    # From the tracking list [x, y, x, y] the bot uses the global variable 'direction' to guide it's turns

    elif attackType == 2:
        # Attack up 1 row
        if direction == 1:
            rowAttackInt = tracking[2] - 1
            rowAttack = spotList[rowAttackInt - 1]
            colAttack = str(tracking[3])
            spot = rowAttack + colAttack
            returnVal = turn(spot, 2, 1)
        # Attack down 1 row
        elif direction == 2:
            rowAttackInt = tracking[2] + 1
            rowAttack = spotList[rowAttackInt - 1]
            colAttack = str(tracking[3])
            spot = rowAttack + colAttack
            returnVal = turn(spot, 2, 2)
        # Attack right 1 column
        elif direction == 3:
            rowAttackInt = tracking[2]
            colAttackInt = tracking[3] + 1
            rowAttack = spotList[rowAttackInt - 1]
            colAttack = str(colAttackInt)
            spot = rowAttack + colAttack
            returnVal = turn(spot, 2, 3)
        # Attack left 1 column
        elif direction == 4:
            rowAttackInt = tracking[2]
            colAttackInt = tracking[3] - 1
            rowAttack = spotList[rowAttackInt - 1]
            colAttack = str(colAttackInt)
            spot = rowAttack + colAttack
            returnVal = turn(spot, 2, 4)

    # Return game condition value from turn

    if returnVal == 1:
        return 1
    elif returnVal == 2:
        return 2


# Master function

def main():
    gameIntro()
    createBoard()
    # A copy of the player board is made to scan for sunk player ships
    printBoards()
    botPlacement()
    #printBotHidden()  <-- Un-comment this to see the bot random board generation in action
    # Game loop
    gameLoop = True
    while gameLoop:

        # Handle player turn
        turnPlayer = False
        turnBot = True
        while not turnPlayer:
            printBoards()
            playerSpot = input("\nEnter spot to attack:")
            turnPlayer = turn(playerSpot, 1, None)
            if turnPlayer == 3:
                print("You have won!")
                printBoards()
                gameLoop = False
                turnBot = False
                break
            elif turnPlayer == 4:
                print("You have lost!")
                printBoards()
                gameLoop = False
                turnBot = False
                break
            elif turnPlayer:
                break

        # Handle bot turn
        if turnBot:
            print("\nBot is attacking. . . ")
            returnVal = botIntelligence()
            if returnVal == 3:
                print("You have won!")
                printBoards()
                gameLoop = False
            elif returnVal == 4:
                print("You have lost!")
                printBoards()
                gameLoop = False

main()
