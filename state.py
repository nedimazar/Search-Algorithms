import copy
import random

### An abstract class that other states will inherit from.
class State:

    def __init__(self):
        pass

    def isGoal(self):
        pass

    def successors(self):
        pass

    def __repr__(self):
        pass



## A state for the 8 puzzle priblem.
class eightPuzzleState(State):

    ## Creates an 8 puzzle board
    def __init__(self, board = [[1, 2, 3], [4, 5, 6], [7, 8, None]], parent = None):

        self.board = board
        
        if None in board[0]:
            self.blankY = 0
            self.blankX = board[0].index(None)
        elif None in board[1]:
            self.blankY = 1
            self.blankX = board[1].index(None)
        elif None in board[2]:
            self.blankY = 2
            self.blankX = board[2].index(None)


        self.parent = parent

    def __repr__(self):
        return(f"{self.board[0]}\n{self.board[1]}\n{self.board[2]}")
        
    # Moves the blank left
    def moveLeft(self):
        b = copy.deepcopy(self.board)
        if self.blankX > 0:
            b[self.blankY][self.blankX] = b[self.blankY][self.blankX - 1]
            b[self.blankY][self.blankX - 1] = None
        return b

    # Moves the blank right
    def moveRight(self):
        b = copy.deepcopy(self.board)
        if self.blankX < 2:
            b[self.blankY][self.blankX] = b[self.blankY][self.blankX + 1]
            b[self.blankY][self.blankX + 1] = None
        return b

    # Moves the blank up
    def moveUp(self):
        b = copy.deepcopy(self.board)
        if self.blankY > 0:
            b[self.blankY][self.blankX] = b[self.blankY - 1][self.blankX]
            b[self.blankY - 1][self.blankX] = None
        return b

    # Moves the blank down
    def moveDown(self):
        b = copy.deepcopy(self.board)
        if self.blankY < 2:
            b[self.blankY][self.blankX] = b[self.blankY + 1][self.blankX]
            b[self.blankY + 1][self.blankX] = None
        return b

    # If the tiles are in this order and ending with the blank
    def isGoal(self):
        return self.board == [[1, 2, 3], [4, 5, 6], [7, 8, None]]

    # There are no possible invalid states here
    def isValidState(self, eightState):
        return True

    def successors(self):
        successorStates = []

        boards = [self.moveUp(), self.moveDown(), self.moveRight(), self.moveLeft()]
        for board in boards:
            if not board == self.board:
                successorStates.append(eightPuzzleState(board, parent = self))

        return successorStates

## helper function to handle changing left to right.
def flip(side):
    if side == 'left':
        return 'right'
    else:
        return 'left'

## A State for the Fox and Chickens problem. We have four instance variables, representing the four objects.
##  (fox, chicken, grain, boat). Values for them are {'left','right'}"""

class FoxAndChickensState(State):
    def __init__(self, f='left', c='left', g='left', b='left', parent=None):
        self.fox = f
        self.chicken = c
        self.grain = g
        self.boat = b
        self.parent = parent

    def isGoal(self):
        return self.fox == 'right' and self.chicken == 'right' and self.grain == 'right' and self.boat == 'right'

    ## check to make sure that we have not left the fox with the chicken, or the chicken with the grain
    def isValidState(self):
        if self.fox == self.chicken and self.fox != self.boat:
            return False
        if self.chicken == self.grain and self.grain != self.boat:
            return False
        return True

    def __repr__(self):
        return "fox: %s chicken: %s grain: %s boat: %s" % (self.fox, self.chicken, self.grain, self.boat)

### generate all valid successor states, and return them in a list.
    def successors(self):
        successorStates = []
        if self.fox == self.boat:
            s = FoxAndChickensState(flip(self.fox), self.chicken, self.grain, flip(self.boat), self)
            if s.isValidState():
                successorStates.append(s)
        if self.chicken == self.boat:
            s = FoxAndChickensState(self.fox, flip(self.chicken), self.grain, flip(self.boat), self)
            if s.isValidState():
                successorStates.append(s)
        if self.grain == self.boat:
            s = FoxAndChickensState(self.fox, self.chicken, flip(self.grain), flip(self.boat), self)
            if s.isValidState():
                successorStates.append(s)
        s = FoxAndChickensState(self.fox, self.chicken, self.grain, flip(self.boat), self)
        if s.isValidState():
            successorStates.append(s)
        return successorStates


#############
## TicTacToeState

### Helper functions to determine whether we are at a leaf node.

def rowWin(board):
    for row in board:
        if len(set(row)) == 1 and row[0] != ' ':
            return row[0]
    return False


def colWin(board):
    for i in range(3):
        col = [item[i] for item in board]
        if len(set(col)) == 1 and col[0] != ' ' :
            return col[0]
    return False


def diagonalWin(board):
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] != ' ':
        return board[1][1]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1] != ' ':
        return board[1][1]
    else:
        return False


def boardFull(board):
    if any(x == ' ' for x in board[0]) or any(x == ' ' for x in board[1]) or any(x == ' ' for x in board[2]):
        return False
    else:
        return True

### State representing a Tic-Tac-Toe board. ' ' is used for unfilled squares.

class TicTacToeState(State):
    def __init__(self, board=None):
        self.score = 0
        if board:
            self.board = board
        else:
            self.board = [[' ', ' ', ' '],
                          [' ', ' ', ' '],
                          [' ', ' ', ' ']]

    def isGoal(self):
        ### we have a win
        if rowWin(self.board) or colWin(self.board) or diagonalWin(self.board):
            return True
        elif boardFull(self.board):
            return True
        else:
            return False

    ## move is either 'x' or 'o'
    def successors(self, move):
        successorStates = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    newBoard = copy.deepcopy(self.board)
                    newBoard[i][j] = move
                    successorStates.append(TicTacToeState(newBoard))

        return successorStates

    ### player is either x or o
    def scoreSelf(self, player):
        winner = rowWin(self.board)
        if not winner:
            winner = colWin(self.board)
        if not winner:
            winner = diagonalWin(self.board)
        if winner:
            if winner == player:
                self.score = 1
            else:
                self.score = -1
        else :
            self.score = 0

    def __repr__(self):
        return " %s\n %s\n %s\n" % (self.board[0], self.board[1], self.board[2])


