"""
This is my implementation of a game of Tic Tac Toe against an opponent
"""
def place( board, team, i ):
    # Place the specified symbol in the specified box
    p = box(i)
    if (board[p[0]][p[1]] != "X" and board[p[0]][p[1]] != "O"):
        board[p[0]][p[1]] = team

def print_b( board ):
    for i in range(3):
        print("{}|{}|{}".format(board[i][0],board[i][1],board[i][2]))

def box( i ):
    return {
            1 : (0,0), 2 : (0,1), 3 : (0,2),
            4 : (1,0), 5 : (1,1), 6 : (1,2),
            7 : (2,0), 8 : (2,1), 9 : (2,2)
            }[i]

def p( p ):
    return {
            (0,0) : 1, (0,1) : 2, (0,2) : 3,
            (1,0) : 4, (1,1) : 5, (1,2) : 6,
            (2,0) : 7, (2,1) : 8, (2,2) : 9
            }[p]

def promt( board, team ):
    print_b(board)
    inp = int(input("Make your move: "))
    place(board,team,inp) 

def play( board ):
    while(playable(board)):
        promt(board,"X")


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


def playable( board ):
    x = set()
    o = set()
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


def full( board ):
    for i in range(3):
        for j in range(3):
            if (board[i][j] != "X" and board[i][j] != "O"):
                return True
    return False




if __name__ == "__main__":
    board = [[str((x+1)+3*y) for x in range(3)] for y in range(3)]
    play(board)
