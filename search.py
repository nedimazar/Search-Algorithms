import state


def BFS(initialState) :
    searchQueue = [initialState]

    closed = {}

    while len(searchQueue) > 0 :
        currentNode = searchQueue.pop(0)
        if currentNode.isGoal() :
            return currentNode
        elif currentNode not in closed:
            closed[currentNode] = 1
            successorStates = currentNode.successors()
            searchQueue.extend(successorStates)
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

    n = BFS(e)

    print(n)
    
main()