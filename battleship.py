// A very inefficient yet functional Battleship game, all thats left is smart bot spot placement
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


boardBot = [[" ", " ", " ", " ", " ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", " ", " ", " "],
            ["#", "#", "#", "#", "#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", "#", "#", "#"],
            [" ", " ", " ", " ", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", " ", " ", " "]]

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

# Create and set the bot display board to have '?' spots

boardBotDisplay = copy.deepcopy(boardP)
for i in range(1, 12):
    for j in range(1, 12):
        boardBotDisplay[i][j] = "?"


# Prints Player board

def printPBoard():
    for x in range(0, 12):
        for y in range(0, 12):
            if y == 0:
                print("\n")
            if x == 0 and y == 10:
                print(boardP[x][y], end="   ")
            else:
                print(boardP[x][y], end="    ")


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
    x = 5
    while x < 16:
        print("\n")
        y = 5
        while y < 16:
            print(boardBot[x][y], end="     ")
            y += 1
        x += 1


# Intro to game and instructions

def gameIntro():
    print("\n\n        Welcome to my Battleship game!\n        Each ship space is marked with it's corresponding",
          "beginning letter\n\n        If you hit the opponents space, the '?' will turn into a '#'",
          "\n\n        If you hit the opponents space, the '?' will turn into a '!'",
          "\n        If you destroy an opponents ship, the '#' marks each turn into a '*'",
          "\n        Below your 4 ships are listed: a Battleship, a Cruiser, a Frigate, and a GunBoat -->",
          "\n\n     B  C  F  G\n     B  C  F  G\n     B  C  F\n     B  C\n     B",
          "\n\n     Enter each space for your ships by typing in the corresponding spot such as 'A5'",
          "\n\n     DO NOT DIAGONALLY PLACE SHIP PIECES! If you do so, restart program!:")

# Initialize placement of Player ships

def placementInit(inputstring, shippiece):
    stringIn = inputstring
    length = len(inputstring)

    # If player inputs column 10 or 11, we want access to 3 string elements:

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

    # If spot is in column 1-9:

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

    # Convert string to character, and then use corresponding ord() value to compare
    charToInt = ord(stringinput[0])

    # For capital letters:

    if charToInt < 97:
        if boardP[charToInt - 64][numberIn] == ".":
            boardP[charToInt - 64][numberIn] = shippiece
        else:
            return False

    # For lowercase letters:

    else:
        if boardP[charToInt - 96][numberIn] == ".":
            boardP[charToInt - 96][numberIn] = shippiece
        else:
            return False

    return True

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

# Handle's turns
# Returns 0 if player or bot choice is invalid
# Returns 1 if player wins
# Returns 2 if bot wins
# Return True if game continues

def turn(spot, user):

    # Allow function to modify game counters

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
                if boardP[row][10] == "#" or boardP[row][10] == "*":
                    return 0
                if boardP[row][10] != ".":
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
                else:
                    print("\nBot MISSED!")

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
                if boardP[row][11] == "#" or boardP[row][11] == "*":
                    return 0
                if boardP[row][11] != ".":
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
                else:
                    print("\nBot MISSED!")

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
            if boardP[row][numberIn] == "#" or boardP[row][numberIn] == "*":
                return 0
            if boardP[row][numberIn] != ".":
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
            else:
                print("\nBot MISSED!")
    else:
        print("\nInvalid input, choose again:")
        return 0

   # Check if ship is sunk and increment final game counter accordingly

    if bShipBot == 5:
        convertToSunk(4, 1)
        botSunk += 1
        bShipBot = 0
    if cruBot == 4:
        convertToSunk(3, 1)
        botSunk += 1
        cruBot = 0
    if frigBot == 3:
        convertToSunk(2, 1)
        botSunk += 1
        frigBot = 0
    if gbBot == 2:
        convertToSunk(1, 1)
        botSunk += 1
        gbBot = 0
    if bShipPl == 5:
        convertToSunk(4, 2)
        plSunk += 1
        bShipPl = 0
    if cruPl == 4:
        convertToSunk(3, 2)
        plSunk += 1
        cruPl = 0
    if frigPl == 3:
        convertToSunk(2, 2)
        plSunk += 1
        frigPl = 0
    if gbPl == 2:
        convertToSunk(1, 2)
        plSunk += 1
        gbPl = 0

    # Check win/loss condition

    if botSunk == 4:
        return 1
    if plSunk == 4:
        return 2

# Scans board bot's display board for #'s and compares location to hidden board's letter in the scanned positions
# If it detects a certain amount of #'s, it will convert each display board spot from # to *
# Only shows sunk bot's sunk ships

def convertToSunk(ship, user):

    displayCheck = True

    # Scan bot's board for a sunk ship:

    if user == 1:
        if ship == 4:

            # Scan for ! horizontally:

            for i in range(1, 12):
                for j in range(1, 7):
                    for scan in range(0, 5):
                        if boardBotDisplay[i][j + scan] != "#":
                            displayCheck = False

                    # If the code makes it here, set board peices for the ship to '*'
                    # Has to check hidden board to ensure all the '!'s are of the same ship type

                    if displayCheck:
                        for convert in range(0, 5):
                            if botBoard[i + 4][j + 4 + convert] != "B":
                                displayCheck = False
                        if displayCheck:
                            for convert in range(0, 5):
                                boardBotDisplay[i][j + convert] = "*"
                            print("\nEnemy Battleship sunk!")
                            return True

            # Scan for ! vertically:

            displayCheck = True
            for i in range(1, 12):
                for j in range(1, 7):
                    for scan in range(0, 5):
                        if boardBotDisplay[j + scan][i] != "#":
                            displayCheck = False
                    if displayCheck:
                        for convert in range(0, 5):
                            if botBoard[i + 4 + convert][j + 4] != "B":
                                displayCheck = False
                        if displayCheck:
                            for convert in range(0, 5):
                                boardBotDisplay[i + convert][j] = "*"
                            print("\nEnemy Battleship sunk!")
                            return True

        elif ship == 3:

            # Scan for ! horizontally:

            for i in range(1, 12):
                for j in range(1, 7):
                    for scan in range(0, 4):
                        if boardBotDisplay[i][j + scan] != "#":
                            displayCheck = False

                    # If the code makes it here, set board peices for the ship to '*'
                    # Has to check hidden board to ensure all the '!'s are of the same ship type

                    if displayCheck:
                        for convert in range(0, 4):
                            if botBoard[i + 4][j + 4 + convert] != "C":
                                displayCheck = False
                        if displayCheck:
                            for convert in range(0, 4):
                                boardBotDisplay[i][j + convert] = "*"
                            print("\nEnemy Cruiser sunk!")
                            return True

            # Scan for ! vertically:

            displayCheck = True
            for i in range(1, 12):
                for j in range(1, 7):
                    for scan in range(0, 4):
                        if boardBotDisplay[j + scan][i] != "#":
                            displayCheck = False
                    if displayCheck:
                        for convert in range(0, 4):
                            if botBoard[i + 4 + convert][j + 4] != "C":
                                displayCheck = False
                        if displayCheck:
                            for convert in range(0, 4):
                                boardBotDisplay[i + convert][j] = "*"
                            print("\nEnemy Cruiser sunk!")
                            return True

        elif ship == 2:

            # Scan for ! horizontally:

            for i in range(1, 12):
                for j in range(1, 7):
                    for scan in range(0, 3):
                        if boardBotDisplay[i][j + scan] != "#":
                            displayCheck = False

                    # If the code makes it here, set board peices for the ship to '*'
                    # Has to check hidden board to ensure all the '!'s are of the same ship type

                    if displayCheck:
                        for convert in range(0, 3):
                            if botBoard[i + 4][j + 4 + convert] != "F":
                                displayCheck = False
                        if displayCheck:
                            for convert in range(0, 3):
                                boardBotDisplay[i][j + convert] = "*"
                            print("\nEnemy Frigate sunk!")
                            return True

            # Scan for ! vertically:

            displayCheck = True
            for i in range(1, 12):
                for j in range(1, 7):
                    for scan in range(0, 3):
                        if boardBotDisplay[j + scan][i] != "#":
                            displayCheck = False
                    if displayCheck:
                        for convert in range(0, 3):
                            if botBoard[i + 4 + convert][j + 4] != "F":
                                displayCheck = False
                        if displayCheck:
                            for convert in range(0, 3):
                                boardBotDisplay[i + convert][j] = "*"
                            print("\nEnemy Frigate sunk!")
                            return True

        elif ship == 1:

            # Scan for ! horizontally:

            for i in range(1, 12):
                for j in range(1, 7):
                    for scan in range(0, 2):
                        if boardBotDisplay[i][j + scan] != "#":
                            displayCheck = False

                    # If the code makes it here, set board peices for the ship to '*'
                    # Has to check hidden board to ensure all the '!'s are of the same ship type

                    if displayCheck:
                        for convert in range(0, 2):
                            if botBoard[i + 4][j + 4 + convert] != "G":
                                displayCheck = False
                        if displayCheck:
                            for convert in range(0, 2):
                                boardBotDisplay[i][j + convert] = "*"
                            print("\nEnemy Gunboat sunk!")
                            return True

            # Scan for ! vertically:

            displayCheck = True
            for i in range(1, 12):
                for j in range(1, 7):
                    for scan in range(0, 2):
                        if boardBotDisplay[j + scan][i] != "#":
                            displayCheck = False
                    if displayCheck:
                        for convert in range(0, 2):
                            if botBoard[i + 4 + convert][j + 4] != "G":
                                displayCheck = False
                        if displayCheck:
                            for convert in range(0, 2):
                                boardBotDisplay[i + convert][j] = "*"
                            print("\nEnemy Gunboat sunk!")
                            return True
    elif user == 2:
        if ship == 4:

            # Scan for ! horizontally:

            for i in range(1, 12):
                for j in range(1, 7):
                    for scan in range(0, 5):
                        if boardP[i][j + scan] != "#":
                            displayCheck = False

                    # If the code makes it here, set board peices for the ship to '*'
                    # Has to check hidden board to ensure all the '!'s are of the same ship type

                    if displayCheck:
                        for convert in range(0, 5):
                            if boardPCopy[i][j + convert] != "B":
                                displayCheck = False
                        if displayCheck:
                            for convert in range(0, 5):
                                boardP[i][j + convert] = "*"
                            print("\nYour Battleship has been sunk!")
                            return True

            # Scan for ! vertically:

            displayCheck = True
            for i in range(1, 12):
                for j in range(1, 7):
                    for scan in range(0, 5):
                        if boardP[j + scan][i] != "#":
                            displayCheck = False
                    if displayCheck:
                        for convert in range(0, 5):
                            if boardPCopy[i + convert][j] != "B":
                                displayCheck = False
                        if displayCheck:
                            for convert in range(0, 5):
                                boardP[i + convert][j] = "*"
                            print("\nYour Battleship has been sunk!")
                            return True

        elif ship == 3:

            # Scan for ! horizontally:

            for i in range(1, 12):
                for j in range(1, 7):
                    for scan in range(0, 4):
                        if boardP[i][j + scan] != "#":
                            displayCheck = False

                    # If the code makes it here, set board peices for the ship to '*'
                    # Has to check hidden board to ensure all the '!'s are of the same ship type

                    if displayCheck:
                        for convert in range(0, 4):
                            if boardPCopy[i][j + convert] != "C":
                                displayCheck = False
                        if displayCheck:
                            for convert in range(0, 4):
                                boardP[i][j + convert] = "*"
                            print("\nYour Cruiser has been sunk!")
                            return True

            # Scan for ! vertically:

            displayCheck = True
            for i in range(1, 12):
                for j in range(1, 7):
                    for scan in range(0, 4):
                        if boardP[j + scan][i] != "#":
                            displayCheck = False
                    if displayCheck:
                        for convert in range(0, 4):
                            if boardPCopy[i + convert][j] != "C":
                                displayCheck = False
                        if displayCheck:
                            for convert in range(0, 4):
                                boardP[i + convert][j] = "*"
                            print("\nYour Cruiser has been sunk!")
                            return True

        elif ship == 2:

            # Scan for ! horizontally:

            for i in range(1, 12):
                for j in range(1, 7):
                    for scan in range(0, 3):
                        if boardP[i][j + scan] != "#":
                            displayCheck = False

                    # If the code makes it here, set board peices for the ship to '*'
                    # Has to check hidden board to ensure all the '!'s are of the same ship type

                    if displayCheck:
                        for convert in range(0, 3):
                            if boardPCopy[i][j + convert] != "F":
                                displayCheck = False
                        if displayCheck:
                            for convert in range(0, 3):
                                boardP[i][j + convert] = "*"
                            print("\nYour Frigate has been sunk!")
                            return True

            # Scan for ! vertically:

            displayCheck = True
            for i in range(1, 12):
                for j in range(1, 7):
                    for scan in range(0, 3):
                        if boardP[j + scan][i] != "#":
                            displayCheck = False
                    if displayCheck:
                        for convert in range(0, 3):
                            if boardPCopy[i + convert][j] != "F":
                                displayCheck = False
                        if displayCheck:
                            for convert in range(0, 3):
                                boardP[i + convert][j] = "*"
                            print("\nYour Frigate has been sunk!")
                            return True

        elif ship == 1:

            # Scan for ! horizontally:

            for i in range(1, 12):
                for j in range(1, 7):
                    for scan in range(0, 2):
                        if boardP[i][j + scan] != "#":
                            displayCheck = False

                    # If the code makes it here, set board peices for the ship to '*'
                    # Has to check hidden board to ensure all the '!'s are of the same ship type

                    if displayCheck:
                        for convert in range(0, 2):
                            if boardPCopy[i][j + convert] != "G":
                                displayCheck = False
                        if displayCheck:
                            for convert in range(0, 2):
                                boardP[i][j + convert] = "*"
                            print("\nYour Gunboat has been sunk!")
                            return True

            # Scan for ! vertically:

            displayCheck = True
            for i in range(1, 12):
                for j in range(1, 7):
                    for scan in range(0, 2):
                        if boardP[j + scan][i] != "#":
                            displayCheck = False
                    if displayCheck:
                        for convert in range(0, 2):
                            if boardPCopy[i + convert][j] != "G":
                                displayCheck = False
                        if displayCheck:
                            for convert in range(0, 2):
                                boardP[i + convert][j] = "*"
                            print("\nYour Gunboat has been sunk!")
                            return True


# Handle each bot turn, threw some AI in here

def botIntelligence():

    # Generate random attack

    random = True
    if random:
        spotList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
        randRow = spotList[randint(0, 10)]
        randCol = str(randint(1, 12))
        randomAttack = randRow + randCol
        turn(randomAttack, 2)


# Master function

def main():
    gameIntro()
    createBoard()
    # A copy of the player board is made to scan for sunk player ships
    boardPCopy = copy.deepcopy(boardP)
    printPBoard()
    botPlacement()
    # printBotHidden()

   # Game loop
    gameLoop = True
    while gameLoop:

        # Handle player turn

        validPlayer = True
        while validPlayer:
            printBotBoard()
            playerSpot = input("\nEnter spot to attack:")
            turn(playerSpot, 1)
            if turn == 1:
                print("You have won!")
                printBotHidden()
                gameLoop = False
                break
            elif turn == 2:
                print("You have lost!")
                printPBoard()
                gameLoop = False
                break
            elif turn == 0:
                validPlayer = True
            elif turn:
                validPlayer = False

        # Handle bot turn

        validBot = True
        while validBot:
            print("\nBot is attacking. . . ")
            printPBoard()
            # Implement bot spot selection
            botIntelligence()
            if turn == 1:
                print("You have won!")
                printBotHidden()
                gameLoop = False
                break
            elif turn == 2:
                print("You have lost!")
                printPBoard()
                gameLoop = False
                break
            elif turn == 0:
                validBot = True
            elif turn:
                validBot = False


main()
