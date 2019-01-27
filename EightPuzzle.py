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
        self.depth = None
        self.cost = None

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
        # Up
        if i > 2:
            # Create new child state
            child_up = Node(deepcopy(parent.state), parent, parent.depth + 1, parent.cost + parent.state[i-3])
            # Swap selected pieces
            child_up.state[i] = parent.state[i - 3]
            child_up.state[i - 3] = parent.state[i]
            # Add to list of new branch states
            successorStates.append(child_up)
        # Down
        if i < 6:
            child_down = Node(deepcopy(parent.state), parent, parent.depth + 1, parent.cost + parent.state[i+3])
            child_down.state[i] = parent.state[i + 3]
            child_down.state[i + 3] = parent.state[i]
            successorStates.append(child_down)
        # Left
        if i not in (0, 3, 6):
            child_left = Node(deepcopy(parent.state), parent, parent.depth + 1, parent.cost + parent.state[i-1])
            child_left.state[i] = parent.state[i - 1]
            child_left.state[i - 1] = parent.state[i]
            successorStates.append(child_left)
        # Right
        if i not in (2, 5, 8):
            child_right = Node(deepcopy(parent.state), parent, parent.depth + 1, parent.cost + parent.state[i+1])
            child_right.state[i] = parent.state[i + 1]
            child_right.state[i + 1] = parent.state[i]
            successorStates.append(child_right)
        return successorStates

    def search(self):
        # Start timer for the selected algorithm
        self.time = time.time()
        strategy = self.strategy
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
        # Determine runtime by subtracting the start-time from the end-time
        self.time = time.time() - self.time
        self.printSummary()
        return

    def printSummary(self):
        print("\n------------------------------------------------------")
        print("Strategy: {}\nDifficulty: {}".format(self.strategy, self.difficulty))
        print("Start = {}\nGoal = {}".format(self.start.state, self.goal))
        print("Depth: {}\nCost: {}".format(self.depth, self.cost))
        print("Time: {}".format(self.time))
        print("Space: {}".format(self.space))
        return

    def printPath(self, head):
        if head:
            self.printResults(head.parent)
            head.printState()
        return


    def A1(self):
        # Create queue
        queue = deque()
        queue.append(self.start)
        visited = {}

        while len(queue) > 0:
            pass
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

        # def best_fvalue(openList):
        #     f = openList[0].f
        #     index = 0
        #     for i, item in enumerate(openList):
        #         if i == 0:
        #             continue
        #         if (item.f < f):
        #             f = item.f
        #             index = i
        #
        #     return openList[index], index
        pass

    def breadthFirst(self):
        # Create queue
        queue = deque()
        queue.append(self.start)

        # Create list of visited states
        visited = set()

        # Initialize space complexity tracking
        self.space = 1;

        while len(queue) > 0:
            # Pop item off the queue & visit its leaves
            parent = queue.popleft()
            visited.add(''.join(map(str, parent.state)))
            # Get next possible moves
            children = self.successor(parent)
            # Check leaves for solution
            for child in children:
                if child.state == self.goal:
                    self.depth = child.depth
                    self.cost = child.cost
                    return True
                # If no solution is found, add leaf to queue and continue
                elif ''.join(map(str, child.state)) not in visited:
                    queue.append(child)

            # Check if space in the queue has grown
            if self.space < len(queue):
                self.space = len(queue)

    def depthFirst(self):
        # Create queue, and list of visited states
        stack = deque()
        stack.append(self.start)

        # Maintain set of all elements, visited AND on stack
        visited = set(''.join(map(str, self.start.state)))

        # Initialize space complexity tracking
        self.space = 1;

        while len(stack) > 0:
            # Pop item off the queue & visit its leaves
            parent = stack.pop()
            # Get next possible moves
            children = self.successor(parent)
            # Check leaves for solution
            for child in children:
                if child.state == self.goal:
                    self.depth = child.depth
                    self.cost = child.cost
                    return True
                else:
                    # If no solution is found, add leaf to stack and continue
                    childKey = ''.join(map(str, child.state))
                    if childKey not in visited:
                        visited.add(childKey)
                        stack.append(child)

            # Check if space in the queue has grown
            if self.space < len(stack):
                self.space = len(stack)

    def iterativeDeepening(self):
        solutionFound = False
        currentDepth = 1
        while solutionFound == False:
            solutionFound = self.ID_Helper(currentDepth)
            currentDepth += 1

    def ID_Helper(self, limit):
        # Create queue, and list of visited states
        stack = deque()
        stack.append(self.start)

        # Maintain set of all elements, visited AND on stack
        visited = set(''.join(map(str, self.start.state)))

        # Initialize space complexity tracking
        self.space = 1;

        while len(stack) > 0:
            # Pop item off the queue & visit its leaves
            parent = stack.pop()
            # Get next possible moves
            children = self.successor(parent)
            # Check leaves for solution
            for child in children:
                if child.state == self.goal:
                    self.depth = child.depth
                    self.cost = child.cost
                    return True
                else:
                    childKey = ''.join(map(str, child.state))
                    # Now check that child node depth meets the current limit before adding to the stack!
                    if childKey not in visited and child.depth <= limit:
                        visited.add(childKey)
                        stack.append(child)

            # Check if space in the queue has grown
            if self.space < len(stack):
                self.space = len(stack)
        return False

    def uniformCost(self):
        stack = deque()
        stack.append(self.start)

        # Create list of visited states
        visited = set()

        # Initialize space complexity tracking
        self.space = 1;
        
        while len(stack) > 0:
            # Pop item off the queue & visit its leaves
            parent = stack.pop()
            # Get next possible moves
            children = self.successor(parent)
            # Check leaves for solution
            for child in children:
                if child.state == self.goal:
                    self.depth = child.depth
                    self.cost = child.cost
                    return True
                else:
                    # If no solution is found, add leaf to stack and continue
                    childKey = ''.join(map(str, child.state))
                    if childKey not in visited:
                        visited.add(childKey)
                        stack.append(child)

            # Check if space in the queue has grown
            if self.space < len(stack):
                self.space = len(stack)

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
