# Design and develop a program that replicates a simple version of the game Battleship.
# Program will demonstrate an understanding of how to apply file I/O, list and looping concepts,
# in a Battleship program that will work as follows:
# Program will read contents from grid text file into a 2d list.
# Ship grid will be invisible to user, but map of current game will be displayed each turn.
# User will be given 30 turns to sink all five ships and will be prompted to enter a new map coordinate each turn.
# Program will evaluate whether the chosen coordinate is valid, and if invalid, will re-prompt user for input
# Game will end if either user sinks all ships on map, or user runs out of missiles
# and will display a win or lose message.
# BONUS: Program will notify user when a particular ship has been sunk

import csv


# prints the board every time it gets updated
def print_board(grid):
    counter = 1
    print("   A B C D E F G H I J")
    for row in grid:
        if counter < 10:
            print(str(counter) + "  " + " ".join(row))
            counter += 1
        elif counter == 10:
            print(str(counter) + " " + " ".join(row))


# changes user input string into list index for column coordinate
def get_column(column):
    if column.upper() == "A":
        return 0
    elif column.upper() == "B":
        return 1
    elif column.upper() == "C":
        return 2
    elif column.upper() == "D":
        return 3
    elif column.upper() == "E":
        return 4
    elif column.upper() == "F":
        return 5
    elif column.upper() == "G":
        return 6
    elif column.upper() == "H":
        return 7
    elif column.upper() == "I":
        return 8
    elif column.upper() == "J":
        return 9


# return proper index for row coordinate
def get_row(user_input):
    row_hit = int(user_input) - 1
    return row_hit


# counters for how many hits each ship can take
a_counter = 5
b_counter = 4
s_counter = 3
c_counter = 3
d_counter = 2

# counters for how many turns you get
missile_counter = 30
hit_counter = 0
target = 00

# variables that will function as list indices
missile_y = ""
missile_x = 0

# creates lists for the board
ship_grid = []
play_grid = []
blank_grid = [['1 '], ['2 '], ['3 '], ['4 '], ['5 '], ['6 '], ['7 '], ['8 '], ['9 '], ['10 ']]

# creates a blank board to modify for the game
for potential_targets in range(10):
    play_grid.append([" "] * 10)

# creates a 2d list from the csv file with ship positions to compare with game board
with open("battleship_grid.csv", "r") as ship_csv:
    csv_data = csv.reader(ship_csv)
    for row in csv_data:
        ship_grid.append(row)

print("Let's play Battleship!")
print("You have 30 missiles to fire to sink all five ships.")
print()

# prints a blank grid
print("   A B C D E F G H I J")
for row in blank_grid:
    print(row[0])

print()

# loop runs as many times as there are set missiles
for turn in range(missile_counter):

        # loop runs until user input is valid
        while missile_y.upper() not in ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J") and missile_x not in range(1, 11):
            while True:
                try:
                    target = input("Choose your target (Ex. A1): ")

                    # splits user input into 2 separate coordinates based on their position in the string
                    missile_y = target[0]
                    missile_x = int(target[1:])

                    # once user input is valid, loop is broken
                    if missile_x in range(1, 11) and missile_y.upper() in ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J"):
                        break
                    else:
                        print("That's not in the ocean!")

                except ValueError:
                    print("That's not in the ocean!")

        # runs through both functions to return proper coordinates
        missile_y = get_column(missile_y)
        missile_x = get_row(missile_x)

        # checks to see if ship is it
        if ship_grid[missile_x][missile_y] in ('A', 'B', 'S', 'C', 'D'):

            # checks to make sure target hasn't been hit before
            if play_grid[missile_x][missile_y] != "X":
                what_ship = ship_grid[missile_x][missile_y]  # determines what ship has been hit
                play_grid[missile_x][missile_y] = "X"  # updates position status on map
                print("HIT!!!!!")
                hit_counter += 1  # adds 1 every time a hit is sustained

                # counters to take away a point every time a certain ship has been hit
                if what_ship == "A":
                    a_counter -= 1
                elif what_ship == "B":
                    b_counter -= 1
                elif what_ship == "S":
                    s_counter -= 1
                elif what_ship == "C":
                    c_counter -= 1
                elif what_ship == "D":
                    d_counter -= 1
            else:  # prints when a target has already been hit
                print("You already tried that! Way to waste a missile!")
                print("Those things aren't cheap you know!")

        # prints a miss whenever a ship was not hit and updates position status on map
        elif ship_grid[missile_x][missile_y] not in ('A', 'B', 'S', 'C', 'D'):
            if play_grid[missile_x][missile_y] != "O":
                play_grid[missile_x][missile_y] = "O"
                print("Miss")
            else:  # prints when a target has already been hit
                print("You already tried that! Way to waste a missile!")
                print("Those things aren't cheap you know!")

        # prints message whenever a particular ship has been sunk
        if a_counter == 0:
            print("YOU SANK MY AIRCRAFT CARRIER!")
            a_counter = 99   # counter lazily set to magical unachievable number so "sank ship" message will never reprint
        if b_counter == 0:
            print("YOU SANK MY BATTLESHIP!")
            b_counter = 99
        if s_counter == 0:
            print("YOU SANK MY SUBMARINE!")
            s_counter = 99
        if c_counter == 0:
            print("YOU SANK MY CRUISER!")
            c_counter = 99
        if d_counter == 0:
            print("YOU SANK MY DESTROYER!")
            d_counter = 99

        # counts down to 0 missiles and displays missile status to user
        missile_counter -= 1
        print("You have " + str(missile_counter) + " missiles remaining")

        # displays current board to user
        print_board(play_grid)
        print()

        # resets list indices
        missile_y = ""
        missile_x = 0

        # determines status of game
        # prints winning message if user sank all ships
        if hit_counter == 17:
            print("YOU SANK MY ENTIRE FLEET!")
            print("You had 17 of 17 hits, which sank all the ships!")
            print("You won, congratulations!")
            break

        # prints losing message if user runs out of missiles
        elif missile_counter == 0:
            print("GAME OVER.")
            print("You had {} of 17 hits, but didn't sink all the ships.".format(hit_counter))
            print("Better luck next time.")