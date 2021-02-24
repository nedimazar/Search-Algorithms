import state


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

def DLS(initialState, limit):
    searchQueue = [initialState]
    closed = {}

    depth = 0
    while len(searchQueue) > 0:
        if depth <= limit:
            currentNode = searchQueue.pop()
            if currentNode.isGoal():
                return currentNode
            elif hash(currentNode) not in closed:
                closed[hash(currentNode)] = 1
                successorStates = currentNode.successors()

                for node in successorStates:
                    if node not in closed:
                        searchQueue.append(node)
                depth = depth + 1
        else:
            return None

def flipPlayer(player) :
    if player == 'x' :
        return 'o'
    else :
        return 'x'

##  player will be x or o.
'''
def minimax(initialState, player) :
    if initialState.isGoal() :
        initialState.scoreSelf(player)
        return initialState
    else :
        ### you do this part
'''

def main():
    board = [[6, None, 2], [1, 4, 3], [7, 5, 8]]

    e = state.eightPuzzleState(board)

    n = DLS(e, 500000)

    print(n)
    
main()