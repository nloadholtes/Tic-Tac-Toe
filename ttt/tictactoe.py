"""Play a game of tic-tac-toe

Nick Loadholtes <nick@ironboundsoftware.com
"""

import sys

from ai import randomPlayer, winningPlayer


WIN_MESSAGES = {"X": "Once again, I am victorious.", "O": "Whoops, it looks like you won."}


def _showValue(v, pos):
    """Displays a pretty board so the user knows where to place their marker.
    Please note that this is where the board numbers come from and they are off
    by one (because people don't like 0-based counting)."""
    return v[pos] if v[pos] is not None else pos+1


def showBoard(board):
    b = board
    for x in xrange(0, 9, 3):
        print("\t\t%s-%s-%s" % (_showValue(b, x), _showValue(b, x+1), _showValue(b, x+2)))


def getUserInput(board):
    output = None
    while(output is None):
        print("Where would you like place your O?   (q to quit)")
        output = raw_input()
        if output not in '123456789q':
            output = None
        try:
            if output is not 'q' and board[int(output) - 1] is not None:
                output = None
        except Exception:
            output = None
    return output


def checkForWin(board):
    #check rows
    for x in xrange(0, 9, 3):
        if board[x] == board[x+1] == board[x+2] and board[x] is not None:
            showBoard(board)
            print("Winner (row %s): %s\n%s" % (x+1, board[x], WIN_MESSAGES[board[x]]))
            return True
    #check cols
    for x in xrange(0, 3):
        if board[x] == board[x+3] == board[x+6] and board[x] is not None:
            showBoard(board)
            print("Winner (column %s): %s\n%s" % (x+1, board[x], WIN_MESSAGES[board[x]]))
            return True
    #check diags
    if board[0] == board[4] == board[8] and board[0] is not None:
        showBoard(board)
        print("Winner (diagonal 1): %s\n%s" % (board[0], WIN_MESSAGES[board[0]]))
        return True
    if board[2] == board[4] == board[6] and board[2] is not None:
        showBoard(board)
        print("Winner (diagonal 2): %s\n%s" % (board[0], WIN_MESSAGES[board[x]]))
        return True
    #Check for empty spots
    if None not in board:
        showBoard(board)
        print("We have tied!")
        return True
    return False


def playGame(computer_player):
    #Setup board
    board = [None for x in range(9)]
    #Display start text/rules/etc
    print("""\n\nWelcome to this little tic-tac-toe game. I (the computer) will play as X. \
You can play as O. Just enter the number of the cell where you want to place your marker. \
(Enter q if you want to give up and quit.)\n\n""")
    while(True):
        #make move
        computer_player(board)
        #check for win
        if(checkForWin(board)):
            break
        #display board
        print("\n")
        showBoard(board)
        #get input
        pos = getUserInput(board)
        if pos == 'q':
            print("Quitting!")
            break
        board[int(pos)-1] = 'O'
        #check for win
        if(checkForWin(board)):
            break

if __name__ == '__main__':
    args = sys.argv
    if len(args) == 2:
        ai = randomPlayer
    else:
        ai = winningPlayer
    playGame(ai)
