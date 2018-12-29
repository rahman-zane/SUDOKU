
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

# Creating a class for each 3x3 Box within the Sudoku. This is  a subclass
class Box(Sudoku):

    def __init__(self, name):
        Sudoku.__init__(self)
        self.name = name
        self.options = {}
        self.grid = np.reshape(self.grid, (3, 3))
        Sudoku.Store.append(self.grid)




# Initialising Boxes
boxes = [i for i in range(9)]
for i in range(9):
    boxes[i] = Box(str(i))
    #print(boxes[i].grid)

# Reshape Sudoku store and print
Sudoku.reshape()
# print(Sudoku.Store)

# Initialise default options for every box in each box dictionary
count = 0;
for box in boxes:
    for i in range(9):
        box.options[i] = list([1,2,3,4,5,6,7,8,9])
    # print the options for each square in each box
    print("Box " + str(count))
    print(box.options)
    count += 1

# Method to remove options within a 3x3 box
def BoxCheck(boxes):
    print("Performing 3x3 check. New options are:")

    # Check for correct number of boxes
    # (insert check here)

    # for each box perform check
    count = 0;
    for box in boxes:

        # get list of numbers that have been filled in current box
        numbers = np.reshape(box.grid, (1, 9))
        numbers = list(numbers[0])
        # print(numbers)

        # each filled number in needs to be removed from every possibility within that box
        for i in numbers:

            for j in range(9):
                try:
                    # Remove option
                    box.options[j].remove(i)
                except:
                    # Do nothing
                    pass

        print("Box " + str(count))
        print(box.options)
        count += 1

    return

BoxCheck(boxes)