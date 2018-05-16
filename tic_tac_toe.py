"""
This is my implementation of a game of Tic Tac Toe against an opponent
"""
x = set()
o = set()
    

# Place the specified symbol in the specified box
def place( board, team, i ):
    p = box(i)
    if (board[p[0]][p[1]] != "X" and board[p[0]][p[1]] != "O"):
        board[p[0]][p[1]] = team

# Print the board
def print_b( board ):
    for i in range(3):
        print("{}|{}|{}".format(board[i][0],board[i][1],board[i][2]))

# Maps a number to the ordered pair that designates a possition on the board
def box( i ):
    return {
            1 : (0,0), 2 : (0,1), 3 : (0,2),
            4 : (1,0), 5 : (1,1), 6 : (1,2),
            7 : (2,0), 8 : (2,1), 9 : (2,2)
            }[i]

# Maps ordered pairs to 1-9 
def p( p ):
    return {
            (0,0) : 1, (0,1) : 2, (0,2) : 3,
            (1,0) : 4, (1,1) : 5, (1,2) : 6,
            (2,0) : 7, (2,1) : 8, (2,2) : 9
            }[p]

# Prompt the player
def promt( board, team ):
    print_b(board)
    inp = int(input("Make your move: "))
    place(board,team,inp) 

    
# Game driver
def play( board ):
    while(playable(board)):
        promt(board,"X")


# Has a player won?
# Returns true if a player has won
def win( x ):
    if ( 1 in x ):
        if ( 2 in x and 3 in x ):
            return True
        if ( 5 in x and 9 in x ):
            return True
        if ( 4 in x and 7 in x ):
            return True
    if ( 3 in x ):
        if ( 6 in x and 9 in x ):
            return True
        if ( 5 in x and 7 in x ):
            return True
    if ( 2 in x and 5 in x and 8 in x ):
        return True
    if ( 4 in x and 5 in x and 6 in x):
        return True
    if ( 7 in x and 8 in x and 9 in x ):
        return True
    return False


# Is the board playable?
# Returns true if no one has won yet
def playable( board ):
   for i in range(3):
        for j in range(3):
            if (board[i][j] == "X"):
                x.add(p((i,j)))
            if (board[i][j] == "O"):
                o.add(p((i,j)))
            if (win(x) or win(o)):
                print_b(board)
                return False
    return True


# Returns true if the board is full
def full( board ):
    for i in range(3):
        for j in range(3):
            if (board[i][j] != "X" and board[i][j] != "O"):
                return False
    return True




if __name__ == "__main__":
    board = [[str((x+1)+3*y) for x in range(3)] for y in range(3)]
    play(board)

