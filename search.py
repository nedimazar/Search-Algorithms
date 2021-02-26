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

##  player will be x or o.
def minimax(initialState, player) :
    if initialState.isGoal() :
        initialState.scoreSelf(player)
        print(initialState)
        return initialState.getScore()
    else :
        if player == 'x':
            maxVal = -10e9
            for state in initialState.successors(player):
                value = minimax(state, flipPlayer(player))
                maxVal = max(maxVal, value)
            return maxVal
        else:
            minVal = 10e9
            for state in initialState.successors(player):
                value = minimax(state, flipPlayer(player))
                minVal = min(minVal, value)
            return minVal



def main():
    board = TicTacToeState()
    print(minimax(board, 'x'))
  
    
main()