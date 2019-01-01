
# Initial Imports
import numpy as np


# Creating the Sudoku Class
class Sudoku():
    Store = []

    def __init__(self):
        self.grid = input("Input Sudoku numbers (3x3 box, from left to right), please use 0 when empty : ")
        self.grid = [int(i) for i in self.grid]

    # Creating a 9x9 grid from the 3x3 boxes which the user input
    def reshape():
        if len(Sudoku.Store) > 8:
            count = 0
            g = []
            k = []
            l = []
            for i in Sudoku.Store:

                if count == 0:
                    g = i
                elif count == 3:
                    k = i
                elif count == 6:
                    l = i
                count += 1
                if 1 < count <= 3:
                    g = np.concatenate((g, i), axis=1)
                elif 4 < count <= 6:
                    k = np.concatenate((k, i), axis=1)
                elif count > 7:
                    l = np.concatenate((l, i), axis=1)

            Sudoku.Store = np.concatenate((g, k, l), axis=0)
        else:
            print("Sudoku not complete")

    # Function to Display the Board
    def displayBoard():
        print(Sudoku.Store)

# Creating a class for each 3x3 Box within the Sudoku. This is  a subclass
class Box(Sudoku):

    def __init__(self, name):
        Sudoku.__init__(self)
        self.name = name
        self.options = {}
        for i in range(9):
            self.options[i] = list([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.grid = np.reshape(self.grid, (3, 3))
        Sudoku.Store.append(self.grid)


# Initialising Boxes
boxes = [i for i in range(9)]
for i in range(9):
    boxes[i] = Box(str(i))
    #print(boxes[i].grid)

# Reshape Sudoku store and print
Sudoku.reshape()
# Sudoku.displayBoard()


# Method to remove options within a 3x3 box
def BoxCheck(boxes):
    print("Performing 3x3 check.")

    # Check for correct number of boxes
    # (insert check here)

    # for each box perform check
    for box in boxes:

        # get list of numbers that have been filled in current box
        numbers = np.reshape(box.grid, (1, 9))
        numbers = list(numbers[0])
        # print(numbers)

        # each filled number needs to be removed from every possibility within that box
        for i in numbers:

            for j in range(9):
                try:
                    # Remove option
                    box.options[j].remove(i)
                except:
                    # Do nothing
                    pass


def ColumnCheck(boxes):
    print("Performing column check.")

    # Generating list of numbers in each column
    xopt = [[] for k in range(9)]

    for i in range(0, 9):
        for j in range(0, 9):
            try:
                xopt[j].append(Sudoku.Store[i][j])
            except(ValueError, KeyError):
                pass
    # print(xopt)
    # print(" ")


    for i in range(9): # loop for columns, xopt
        j = int(i / 3) # loop for boxes
        for k in xopt[i]: # loops through the numbers in the column
            for l in range(0,9,3): # loops through the squares in each box
                try:
                    boxes[j].options[l + (i % 3)].remove(k)
                    #print(boxes[j].options[l + (i % 3)])
                except:
                    #print(boxes[j].options[l + (i % 3)])
                    pass
                try:
                    boxes[j + 3].options[l + (i % 3)].remove(k)
                    #print(boxes[j + 3].options[l + (i % 3)])
                except:
                    #print(boxes[j + 3].options[l + (i % 3)])
                    pass
                try:
                    boxes[j + 6].options[l + (i % 3)].remove(k)
                    #print(boxes[j + 6].options[l + (i % 3)])
                except:
                    #print(boxes[j + 6].options[l + (i % 3)])
                    pass


def RowCheck(boxes):
    print("Performing row check.")

    # Generating list of numbers in each row
    yopt = [[] for k in range(9)]

    for i in range(0, 9):
        for j in range(0, 9):
            try:
                yopt[i].append(Sudoku.Store[i][j])
            except(ValueError, KeyError):
                pass
    # print(yopt)
    # print(" ")


    for i in range(9): # loop for rows, yopt
        j = (int(i / 3)) * 3 # loop for boxes
        for k in yopt[i]: # loops through the numbers in the row
            for l in range(3): # loops through the squares in each box
                try:
                    boxes[j].options[l + ((i % 3) * 3)].remove(k)
                    #print(boxes[j].options[l + (i % 3)])
                except:
    #                #print(boxes[j].options[l + (i % 3)])
                    pass
                try:
                    boxes[j + 1].options[l + ((i % 3) * 3)].remove(k)
    #                #print(boxes[j + 3].options[l + (i % 3)])
                except:
    #                #print(boxes[j + 3].options[l + (i % 3)])
                    pass
                try:
                    boxes[j + 2].options[l + ((i % 3) * 3)].remove(k)
    #                #print(boxes[j + 6].options[l + (i % 3)])
                except:
                    #print(boxes[j + 6].options[l + (i % 3)])
                    pass


def ClearFilledOptions(boxes):
    print("Removing options for filled in boxes.")
    for box in boxes:

        # get list of numbers that have been filled in current box
        numbers = np.reshape(box.grid, (1, 9))
        numbers = list(numbers[0])

        # if the square contains a number empty its options
        for i in range(9):
            if numbers[i] != 0:
                box.options[i] = []



def PrintOptions(boxes):
    count = 0
    for box in boxes:
        print("Box " + str(count))
        print(box.options)
        count += 1


# First run of all checks to create options for unfilled squares
ColumnCheck(boxes)
RowCheck(boxes)
BoxCheck(boxes)
ClearFilledOptions(boxes)
PrintOptions(boxes)
Sudoku.displayBoard()