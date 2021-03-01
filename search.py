import state
from state import *
from heapq import *

def BFS(initialState):
    searchQueue = [initialState]

    closed = {}

    while len(searchQueue) > 0:
        currentNode = searchQueue.pop(0)
        if currentNode.isGoal():
            return currentNode
        elif hash(currentNode) not in closed:
            closed[hash(currentNode)] = 1
            successorStates = currentNode.successors()

            for node in successorStates:
                if node not in closed:
                    searchQueue.append(node)
    return None

def DFS(initialState):
    searchQueue = [initialState]

    closed = {}

    while len(searchQueue) > 0:
        currentNode = searchQueue.pop()
        if currentNode.isGoal():
            return currentNode
        elif hash(currentNode) not in closed:
            closed[hash(currentNode)] = 1
            successorStates = currentNode.successors()
            for node in successorStates:
                if node not in closed:
                    searchQueue.append(node)
    return None

def DLDFS(initialState, limit):
    closed = {}

    def overload(initialState, limit):
        closed[hash(initialState)] = True


        if initialState.isGoal():
            return initialState

        if limit <= 0:
            return None
        
        for state in initialState.successors():
            if hash(state) not in closed:
                closed[hash(state)] = True
                result = overload(state, limit - 1)

                if result:
                    return result
        return None

    return overload(initialState, limit)

def IDDFS(initialState):
    limit = 1

    while True:
        node = DLDFS(initialState, limit)
        if node:
            return node
        limit = limit + 1

        # Detect overflow
        if limit <= 0:
            return None

def ASTAR(initialState):
    priorityQueue = [[0, initialState]]

    closed = {}

    while len(priorityQueue) > 0:
        currentNode = heappop(priorityQueue)[1]
        if currentNode.isGoal():
            return currentNode
        elif hash(currentNode) not in closed:
            closed[hash(currentNode)] = 1
            successorStates = currentNode.successors()

            for node in successorStates:
                if node not in closed:
                    heappush(priorityQueue, [node.h(), node])
    return None


def flipPlayer(player) :
    if player == 'x' :
        return 'o'
    else :
        return 'x'


def minimax(initialState, player):
    if initialState.isGoal():
        initialState.scoreSelf(player)
        return initialState, initialState.score
    elif player == 'x':
        maxVal = -10e9
        bestMove = None
        for move in initialState.successors('x'):
            choice, score = minimax(move, 'o')
            if score > maxVal:
                maxVal = score
                bestMove = move
        return bestMove, maxVal
    elif player == 'o':
        minVal = 10e9
        bestMove = None
        for move in initialState.successors('o'):
            choice, score = minimax(move, 'x')
            if score < minVal:
                minVal = score
                bestMove = move
        return bestMove, minVal

def getXMove(board):
    boardCopy = copy.deepcopy(board)
    try:
        y = int(input("Enter the row index of your choice (0-2): "))
        x = int(input("Enter the column index of your choice (0-2): "))
    except Exception:
        print("You can't break me...")
        return getXMove(board)
        

    if 0 <= x <= 2 and 0 <= y <= 2:
        if boardCopy[y][x] != ' ':
            print("Nice try sucker.")
            return getXMove(board)
        else:
            boardCopy[y][x] = 'x'
            return boardCopy
    else:
        print("Not a valid move bucko... Try again.")
        return getXMove(board)

def getOMove(board):
    boardCopy = copy.deepcopy(board)
    try:
        y = int(input("Enter the row index of your choice (0-2): "))
        x = int(input("Enter the column index of your choice (0-2): "))
    except Exception:
        print("You can't break me...")
        return getOMove(board)
        

    if 0 <= x <= 2 and 0 <= y <= 2:
        if boardCopy[y][x] != ' ':
            print("Nice try sucker.")
            return getOMove(board)
        else:
            boardCopy[y][x] = 'o'
            return boardCopy
    else:
        print("Not a valid move bucko... Try again.")
        return getOMove(board)
    pass

def main():
    c = input("Pick 'x' or 'o' (You won't win either way): ")

    if c == 'x':
        game = TicTacToeState()

        while not game.isGoal():
            for x in game.board: print(x)
            board = getXMove(game.board)

            game = TicTacToeState(board)
            newBoard, score = minimax(game, 'o')
            game = TicTacToeState(board=newBoard.board)
        for x in game.board: print(x)
        
        
    else:
        game = TicTacToeState()
        board = None

        while not game.isGoal():            
            if board:
                game = TicTacToeState(board)
            board, score = minimax(game, 'x')
            for x in board.board: print(x)
            if not game.isGoal():
                newBoard = getOMove(board.board)
            game = TicTacToeState(newBoard)
            board = newBoard
            
        for x in game.board: print(x)

  
    
main()