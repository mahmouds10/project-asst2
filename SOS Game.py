"""
Name :Mahmoud Sayed
ID: 20210370
"""
Body = [["   ", "   ", "   ", "   ", "   ",],
                ["   ", "   ", "   ", "   ", "   ",],
                ["   ", "   ", "   ", "   ", "   ",],
                ["   ", "   ", "   ", "   ", "   ",],
                ["   ", "   ", "   ", "   ", "   ",]]
score1 = 0
score2 = 0
gameCounter = 1
Player_indx = 1
row = 0
column = 0


def DrawPattern():
    print ("\n Player 1 pts : " + str(score1) + "     " + "player 2 pts : " + str(score2) + "\n")
    if (Player_indx % 2):
        print ("(Player 1 turn)\n")
    else:
        print ("(Player 2 turn)\n")

    for row in Body:
        print("|", end = "")
        for element in row:
            print (element, end = "|")
        print("\n" + "---------------------")

def InputIndx():
    global row, column
    row = int(input("Enter Row's Index : "))
    column = int(input("Enter Column's Index : "))

    global gameCounter

    if gameCounter % 2:
        Body[row - 1][column - 1] = " S "
    else:
        Body[row - 1][column - 1] = " O "

    gameCounter += 1

def Pts_calculating():
    global Player_indx, score1, score2
    win = False
    # Fix error of out of index
    if Body[row - 1][column - 1] == " S ":
        if (Body[row - 1][column - 2] == " O " and Body[row - 1][column - 3] == " S "):
            if (Player_indx % 2):
                score1 += 1
                win = True
            else:
                score2 += 1
                win = True

        if (Body[row - 1][column] == " O " and Body[row - 1][column + 1] == " S "):
            if (Player_indx % 2):
                score1 += 1
                win = True
            else:
                score2 += 1
                win = True

        if (Body[row - 2][column - 1] == " O " and Body[row - 3][column - 1] == " S "):
            if (Player_indx % 2):
                score1 += 1
                win = True
            else:
                score2 += 1
                win = True

        if (Body[row][column - 1] == " O " and Body[row + 1][column - 1] == " S "):
            if (Player_indx % 2):
                score1 += 1
                win = True
            else:
                score2 += 1
                win = True

        if (Body[row][column - 2] == " O " and Body[row + 1][column - 3] == " S "):
            if (Player_indx % 2):
                score1 += 1
                win = True
            else:
                score2 += 1
                win = True

        if (Body[row - 2][column] == " O " and Body[row - 3][column + 1] == " S "):
            if (Player_indx % 2):
                score1 += 1
                win = True
            else:
                score2 += 1
                win = True

        if (Body[row][column] == " O " and Body[row + 1][column + 1] == " S "):
            if (Player_indx % 2):
                score1 += 1
                win = True
            else:
                score2 += 1
                win = True

        if (Body[row - 2][column - 2] == " O " and Body[row - 3][column - 3] == " S "):
            if (Player_indx % 2):
                score1 += 1
                win = True
            else:
                score2 += 1
                win = True

    elif  Body[row - 1][column - 1] == " O ":
        if (Body[row - 1][column] == " S " and Body[row - 1][column - 2] == " S "):
            if (Player_indx % 2):
                score1 += 1
                win = True
            else:
                score2 += 1
                win = True

        if (Body[row][column - 1] == " S " and Body[row - 2][column - 1] == " S "):
            if (Player_indx % 2):
                score1 += 1
                win = True
            else:
                score2 += 1
                win = True

        if (Body[row - 2][column] == " S " and Body[row][column - 2] == " S "):
            if (Player_indx % 2):
                score1 += 1
                win = True
            else:
                score2 += 1
                win = True

        if (Body[row - 2][column - 2] == " S " and Body[row][column] == " S "):
            if (Player_indx % 2):
                score1 += 1
                win = True
            else:
                score2 += 1
                win = True
    if not win:
        Player_indx += 1


def Replay ():
    DrawPattern()
    InputIndx()
    Pts_calculating()

while(gameCounter <= 26):
    Replay()

# GameEnds()