class EightPuzzle:
    def __init__(self):
        self.state = null
        self.goal = null
        self.strategy = null

    def setGame(self, start, goal, strategy):
        self.state = start
        self.goal = goal
        self.strategy = strategy

    def successor(self, parent):
        # Create list of branch states to be returned
        successorStates = list()
        # Get current position of the free space in the puzzle
        i = parent.state.index(0)
        if i > 2:
            # Create new child state
            child_up = Node(parent.state, parent, parent.depth + 1, 0)
            # Swap selected pieces
            child_up.state[i] = parent.state[i - 3]
            child_up.state[i - 3] = parent.state[i]
            # Add to list of new branch states
            successorStates.append(child_up)
        if i < 6:
            child_down = Node(parent.state, parent, parent.depth + 1, 0)
            child_down.state[i] = parent.state[i + 3]
            child_down.state[i + 3] = parent.state[i]
            successorStates.append(child_down)
        if i not in (0, 3, 6):
            child_left = Node(parent.state, parent, parent.depth + 1, 0)
            child_left.state[i] = parent.state[i - 1]
            child_left.state[i - 1] = parent.state[i]
            successorStates.append(child_left)
        if i not in (2, 5, 8):
            child_right = Node(parent.state, parent, parent.depth + 1, 0)
            child_right.state[i] = parent.state[i + 1]
            child_right.state[i + 1] = parent.state[i]
            successorStates.append(child_right)
        return successorStates

    def search(self):
        strategy = self.strategy
        if strategy == "Breadth First":
            breadthFirst()
        elif strategy == "Depth First":
            depthFirst()
        elif strategy == "Iterative Deepening":
            iterativeDeepening()
        elif strategy == "Uniform Cost":
            uniformCost()
        elif strategy == "Best First":
            bestFirst()
        elif strategy == "A*":
            A1()
        elif strategy == "A* 2":
            A2()
        elif strategy == "A* 3":
            A3()
        else:
            print("Unknown search strategy has been selected!")
        return

    def A1(self):
        openList = []
        closedList = []
        openList.append(start)

        while openList:
            current, index = best_fvalue(openList)
            if current.goal():
                return current
            openList.pop(index)
            closedList.append(current)

            X = move_function(current)
            for move in X:
                ok = False  # checking in closedList
                for i, item in enumerate(closedList):
                    if item == move:
                        ok = True
                        break
                if not ok:  # not in closed list
                    newG = current.g + 1
                    present = False

                    # openList includes move
                    for j, item in enumerate(openList):
                        if item == move:
                            present = True
                            if newG < openList[j].g:
                                openList[j].g = newG
                                openList[j].f = openList[j].g + openList[j].h
                                openList[j].parent = current
                    if not present:
                        move.g = newG
                        move.h = move.manhattan()
                        move.f = move.g + move.h
                        move.parent = current
                        openList.append(move)

        def printResults(self):
            current = self.state
            while current:
                current.printState()
                current = current.parent

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
