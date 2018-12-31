# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 15:35:36 2018

@author: aeo17
"""

import numpy as np

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
        self.grid = np.reshape(self.grid, (3, 3))
        Sudoku.Store.append(self.grid)
boxes =[i for i in range(9)]    

for i in range(9):
    boxes[i] = Box(str(i))


Sudoku.reshape()
Sudoku.displayBoard()

#creates the list of options
Options = [[1,2,3,4,5,6,7,8,9] for i in range(9)]
yopt=[[0]*9 for i in range(9)]
#removes numbers present in row from list of options
def rowCheck():
    for k in range(9):
        for j in range(1,10):
            if j in Sudoku.Store[k]:
                Options[k].remove(j)     
#prints list of options for each row        
    print(Options) 
#all numbers in same row will have same options
 
    for h in range(9): #loops through rows
        for a in range(9): #loops through numbers in rows
            if Sudoku.Store[h][a] ==0:
              yopt[h][a]=Options[h]  #stores options for the rows in zero positions
            else:
                yopt[h][a]= Sudoku.Store[h][a]
                
           # print(str(h) + str(a))
            #print(yopt[h][a])
     

rowCheck()
# =============================================================================
# 380690004
# 090000070
# 070005069
# 020430510
# 800601004
# 041058090
# 840100050
# 000900060
# 900084013
# =============================================================================
#firsttry #notsstoring anything correctly #but i tried #lol
