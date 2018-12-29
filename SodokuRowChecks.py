# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 15:35:36 2018

@author: aeo17
"""

import numpy as np

class Sudoku ():

    Store =[]
    boxes =[]
    rows = []

    def __init__(self):
        self.grid = input("input sudoku numbers, please use 0 when empty : ")
        self.grid = [int(i) for i in self.grid]

    def reshape():
        if len(Sudoku.Store) >8:
            count = 0
            g=[]
            k=[]
            l=[]
            for  i in Sudoku.Store:

                if count == 0:
                    g = i
                elif count == 3:
                    k = i
                elif count == 6:
                    l = i
                count+=1    
                if 1<count <= 3:
                    g=np.concatenate((g,i), axis=1)
                elif 4 < count <= 6:
                    k  = np.concatenate((k,i), axis=1)
                elif count > 7:
                    l =np.concatenate((l,i), axis=1)

            Sudoku.Store = np.concatenate((g,k,l), axis=0)
        else:
            print("Sudoku not complete")

    def displayBoard():
        print(Sudoku.Store)



class Box(Sudoku):  
    def __init__ (self,name):
        Sudoku.__init__(self)
        self.name= name
        self.options = {}
        self.grid = np.reshape(self.grid,(3,3))
        Sudoku.Store.append(self.grid)
        Sudoku.boxes.append(name)

boxes =[i for i in range(9)]    

for i in range(9):
    boxes[i] = Box(str(i))


Sudoku.reshape()
Sudoku.displayBoard()
#creates the list of options
Options = [[1,2,3,4,5,6,7,8,9] for i in range(0,9)]
print(Options[0])

#removes numbers present in row from list of options
for j in range(1,10):
    if j in Sudoku.Store[0]:
        Options[0].remove(j)
for i in range(1,10):
    if i in Sudoku.Store[1]:
        Options[1].remove(i)
for i in range(1,10):
    if i in Sudoku.Store[2]:
        Options[2].remove(i)
for i in range(1,10):
    if i in Sudoku.Store[3]:
        Options[3].remove(i)
for i in range(1,10):
    if i in Sudoku.Store[4]:
        Options[4].remove(i)
for i in range(1,10):
    if i in Sudoku.Store[5]:
        Options[5].remove(i)
for i in range(1,10):
    if i in Sudoku.Store[6]:
        Options[6].remove(i)
for i in range(1,10):
    if i in Sudoku.Store[7]:
        Options[7].remove(i)
for i in range(1,10):
    if i in Sudoku.Store[8]:
        Options[8].remove(i)
#prints list of options for each row        
print(Options) 

#kindainefficient #lowkey decent attempt #dontjudge2019
