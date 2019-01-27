from collections import deque
from copy import deepcopy
import time


class EightPuzzle:
    def __init__(self):
        self.start = None
        self.goal = None
        self.strategy = None
        self.difficulty = None
        self.time = None
        self.space = None

    def setGame(self, start, goal, strategy, difficulty):
        self.start = Node(start, None, 1, 0)
        self.goal = goal
        self.strategy = strategy
        self.difficulty = difficulty

    def successor(self, parent):
        # Create list of branch states to be returned
        successorStates = list()
        # Get current position of the free space in the puzzle
        i = parent.state.index(0)
        # Left
        if i not in (0, 3, 6):
            # Create new child state
            child_left = Node(deepcopy(parent.state), parent, parent.depth + 1, parent.cost + parent.state[i-1])
            # Swap selected pieces
            child_left.state[i] = parent.state[i - 1]
            child_left.state[i - 1] = parent.state[i]
            # Add to list of new branch states
            successorStates.append(child_left)
        # Up
        if i > 2:
            child_up = Node(deepcopy(parent.state), parent, parent.depth + 1, parent.cost + parent.state[i-3])
            child_up.state[i] = parent.state[i - 3]
            child_up.state[i - 3] = parent.state[i]
            successorStates.append(child_up)
        # Down
        if i < 6:
            child_down = Node(deepcopy(parent.state), parent, parent.depth + 1, parent.cost + parent.state[i+3])
            child_down.state[i] = parent.state[i + 3]
            child_down.state[i + 3] = parent.state[i]
            successorStates.append(child_down)
        # Right
        if i not in (2, 5, 8):
            child_right = Node(deepcopy(parent.state), parent, parent.depth + 1, parent.cost + parent.state[i+1])
            child_right.state[i] = parent.state[i + 1]
            child_right.state[i + 1] = parent.state[i]
            successorStates.append(child_right)
        return successorStates

    def search(self):
        strategy = self.strategy
        print("\n------------------------------------------------------")
        print("Strategy: {}\nDifficulty: {}".format(self.strategy, self.difficulty))
        print("Start = {}\nGoal = {}".format(self.start.state, self.goal))
        print("\n")
        self.time = time.time()
        if strategy == "Breadth First":
            self.breadthFirst()
        elif strategy == "Depth First":
            self.depthFirst()
        elif strategy == "Iterative Deepening":
            self.iterativeDeepening()
        elif strategy == "Uniform Cost":
            self.uniformCost()
        elif strategy == "Best First":
            self.bestFirst()
        elif strategy == "A*":
            self.A1()
        elif strategy == "A* 2":
            self.A2()
        elif strategy == "A* 3":
            self.A3()
        else:
            print("Unknown search strategy has been selected!")
        endTime = time.time()
        print("Time: {}".format(endTime - self.time))
        print("Space: {}".format(self.space))

        return

    def printResults(self, current):
        if current:
            self.printResults(current.parent)
            current.printState()
        return

    def A1(self):
        # openList = []
        # closedList = []
        # openList.append(start)
        #
        # while openList:
        #     current, index = best_fvalue(openList)
        #     if current.goal():
        #         return current
        #     openList.pop(index)
        #     closedList.append(current)
        #
        #     X = move_function(current)
        #     for move in X:
        #         ok = False  # checking in closedList
        #         for i, item in enumerate(closedList):
        #             if item == move:
        #                 ok = True
        #                 break
        #         if not ok:  # not in closed list
        #             newG = current.g + 1
        #             present = False
        #
        #             # openList includes move
        #             for j, item in enumerate(openList):
        #                 if item == move:
        #                     present = True
        #                     if newG < openList[j].g:
        #                         openList[j].g = newG
        #                         openList[j].f = openList[j].g + openList[j].h
        #                         openList[j].parent = current
        #             if not present:
        #                 move.g = newG
        #                 move.h = move.manhattan()
        #                 move.f = move.g + move.h
        #                 move.parent = current
        #                 openList.append(move)
        pass

    def breadthFirst(self):
        # Create queue, and list of visited states
        queue = deque()
        visited = {}
        # Add root onto the queue
        queue.append(self.start)
        self.space = 1;

        while len(queue) > 0:
            # Pop item off the queue & visit its leaves
            parent = queue.popleft()
            visited[''.join(map(str, parent.state))] = parent
            children = self.successor(parent)
            # Check leaves for solution
            for child in children:
                if child.state == self.goal:
                    self.printResults(child)
                    return
                else:
                    # If no solution is found, add leaf to queue and continue
                    if ''.join(map(str, child.state)) not in visited:
                        queue.append(child)

            if self.space < len(queue):
                self.space = len(queue)

    def depthFirst(self):
        # Create queue, and list of visited states
        stack = deque()
        visited = set()

        # Maintain set of elements on the queue
        onStack = set(''.join(map(str, self.start.state)))


        # Add root onto the queue
        stack.append(self.start)
        self.space = 1;

        while len(stack) > 0:
            # Pop item off the queue & visit its leaves
            parent = stack.pop()

            parentKey = ''.join(map(str, parent.state))
            visited.add(parentKey)

            children = self.successor(parent)
            # Check leaves for solution
            for child in children:
                if child.state == self.goal:
                    print("Depth: {}\nCost: {}".format(child.depth, child.cost))
                    #self.printResults(child)
                    return
                else:
                    # If no solution is found, add leaf to queue and continue
                    childKey = ''.join(map(str, child.state))
                    if childKey not in visited:
                        if childKey not in onStack:
                            stack.append(child)
                            onStack.add(childKey)
            # Remove parent key from onQueue
            if parentKey in onStack:
                onStack.remove(parentKey)

            if self.space < len(stack):
                self.space = len(stack)

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
        self.child = None
        self.depth = _depth
        self.cost = _cost
        self.expanded = 'no'

    def printState(self):
        cState = self.state
        print("Depth: {},  Cost: {}".format(self.depth, self.cost))
        print("|-----------|")
        print("| {} | {} | {} |".format(cState[0], cState[1], cState[2]))
        print("|-----------|")
        print("| {} | {} | {} |".format(cState[3], cState[4], cState[5]))
        print("|-----------|")
        print("| {} | {} | {} |".format(cState[6], cState[7], cState[8]))
        print("|-----------|")
        print(" ")
