class EightPuzzle:
    def __init__(self, _start, _goal, _strategy):
        self.state = _start
        self.goal = _goal
        self.strategy = _strategy
        self.state = Node(self.start, null, 1, 0)

    def successor(self, parrent):
        # Create list of branch states to be returned
        successorStates = list()
        # Get current position of the free space in the puzzle
        i = parrent.state.index(0)
        if i > 2:
            # Create new child state
            child_up = Node(parrent.state, parrent, parrent.depth + 1, 0)
            # Swap selected pieces
            child_up.state[i] = parrent.state[i - 3]
            child_up.state[i - 3] = parrent.state[i]
            # Add to list of new branch states
            successorStates.append(child_up)
        if i < 6:
            child_down = Node(parrent.state, parrent, parrent.depth + 1, 0)
            child_down.state[i] = parrent.state[i + 3]
            child_down.state[i + 3] = parrent.state[i]
            successorStates.append(child_down)
        if i not in (0, 3, 6):
            child_left = Node(parrent.state, parrent, parrent.depth + 1, 0)
            child_left.state[i] = parrent.state[i - 1]
            child_left.state[i - 1] = parrent.state[i]
            successorStates.append(child_left)
        if i not in (2, 5, 8):
            child_right = Node(parrent.state, parrent, parrent.depth + 1, 0)
            child_right.state[i] = parrent.state[i + 1]
            child_right.state[i + 1] = parrent.state[i]
            successorStates.append(child_right)
        return successorStates

    def printResults(self):
        current = self.state
        while current:
            current.printState()
            current = current.parent

    def A1(self):
        pass

    def breadthFirst(self):
        pass

    def depthFirst(self):
        pass

    def iterativeDeepening(self):
        pass

    def uniformCost(self):
        pass

    def bestFirst(self):
        pass

    def A2(self):
        pass

    def A3(self):
        pass


class Node:
    def __init__(self, _state, _parent, _depth, _cost):
        self.state = _state
        self.parent = _parent
        self.child = null
        self.depth = _depth
        self.cost = _cost
        self.expanded = 'no'

    def printState(self):
        cState = self.state
        print("|-----------|")
        print("| {} | {} | {} |".format(cState[0], cState[1], cState[2]))
        print("|-----------|")
        print("| {} | {} | {} |".format(cState[3], cState[4], cState[5]))
        print("|-----------|")
        print("| {} | {} | {} |".format(cState[6], cState[7], cState[8]))
        print("|-----------|")
        print(" ")
