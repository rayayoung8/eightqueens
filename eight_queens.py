
# this function takes in x,y coordinates as parameters
# it is assumed we are talking about an 8x8 chess board
# it is assumed we would call the function with 0,0 (starting at top left)
# the function will print out the 8x8 list with 1's where the queens would go

# 2 dimensional 8x8 list "chess" with 64 zeros
chess = [[0 for n in range(8)] for n in range(8)]

def queens(x,y):

    fail1 = False
    fail2 = False

    # check if there is a queen in that row
    for a in range(0, x):
        if chess[a][y] == 1:
            fail1 = True
            break

    # check if there is a queen on the diagonal (slope of 1 or -1)
    for i in range(0,x):
        for j in range(0, 8):
            if (y-j == x-i or y-j == -x+i) and chess[i][j] == 1:
                fail2 = True
                break

    # if this position is safe, place a queen there
    if fail1 == False and fail2 == False:
        chess[x][y] = 1
        # if we've reached the last column, we are done! print out the board
        if x == 7:
            for num in range(0,8):  
                print(chess[num])
        # otherwise, move on to the next column & do it again
        else:
            queens(x+1, 0)

    # if this position is unsafe, and if we've reached the bottom, backtrack
    elif y == 7:
        fun = x-1
        while fun >= 0:
            # go to the left 1 column
            # if the queen is not at the bottom, go down 1 and do it again
            if chess[fun][7] != 1:
                for h in range(0,8):
                    if chess[fun][h] == 1:
                        index = h
                chess[fun][index] = 0
                queens(fun,index+1)
                fun = -1
            # if the queen is at the bottom, erase that and go to the left again
            else:
                chess[fun][7] = 0
                fun = fun-1

    # if unsafe & not at bottom, go down one and do the function again
    else: 
        queens(x, y+1)           

queens(0,0)

