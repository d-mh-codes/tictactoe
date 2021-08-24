# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 17:53:04 2021

@author: mh_codes
"""

# | |  0
#----- 1
# | |  2
#----- 3
# | |  4
#01234


def field(current) :
    for row in range(5) : #0,1,2,3,4
        if row%2 == 0:
            prow = int(row / 2)
            for column in range(5) :#0,1,2,3,4
                if column%2 == 0 :
                    pcolumn = int(column / 2)
                    if column != 4 :
                        print(current[pcolumn][prow], end = "")
                    else:
                        print(current[pcolumn][prow])
                else:
                    print("|", end = "")
        else:
            print("-----")

player = 1
currentField = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
field(currentField)

while(True) : #True == True
    print("Players turn: ", player)
    rowMove = int(input("Please enter the row: "))
    columnMove = int(input("Please enter the column: "))
    if player == 1:
        #make move for player 1
        rowMove +=-1
        columnMove +=-1
        if currentField[columnMove][rowMove] == " ":
            currentField[columnMove][rowMove] = "X"
            player = 2
    else:
        #make move for player 2
        rowMove +=-1
        columnMove +=-1
        if currentField[columnMove][rowMove] == " ":
            currentField[columnMove][rowMove] = "O"
            player = 1
    field(currentField)