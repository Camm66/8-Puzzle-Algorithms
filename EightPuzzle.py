from collections import deque
from sortedcontainers import SortedDict
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
            self.aStar(self.hMisplaced)
        elif strategy == "A* 2":
            self.aStar(self.hManhattan)
        elif strategy == "A* 3":
            self.aStar(self.hMyChoice)
        else:
            print("Unknown search strategy has been selected!")
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
            self.printPath(head.parent)
            head.printState()
        return

    def breadthFirst(self):
        # Create queue
        queue = deque()
        queue.append(self.start)

        # Create list of visited states
        visited = set()

        # Initialize space/time tracking
        self.space = 1
        self.time = 0

        while len(queue) > 0:
            # Pop item off the queue & visit its leaves
            parent = queue.popleft()
            visited.add(''.join(map(str, parent.state)))
            self.time += 1
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
        visited = set()

        # Initialize space/time tracking
        self.space = 1
        self.time = 0

        while len(stack) > 0:
            # Pop item off the queue & visit its leaves
            parent = stack.pop()
            visited.add(''.join(map(str, parent.state)))
            self.time += 1
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
        # Create queue
        stack = deque()
        stack.append(self.start)

        # Maintain set of all elements visited
        visited = set(''.join(map(str, self.start.state)))

        # Initialize space/time tracking
        self.space = 1
        self.time = 0

        while len(stack) > 0:
            # Pop item off the queue & visit its leaves
            parent = stack.pop()
            self.time += 1
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
        # Create sorted priority queue
        pQueue = [(self.start.cost, self.start)]
        # Create list of visited state/cost pairs
        visited = {}

        # Initialize space/time tracking
        self.space = 1
        self.time = 0

        while pQueue:
            # Sort the queued items based on cost
            pQueue = sorted(pQueue, key=lambda x: x[0])
            # Pop item off the queue & add to list of visited nodes
            parent = pQueue.pop(0)[1]
            parentKey = ''.join(map(str, parent.state))
            visited[parentKey] = parent.cost
            self.time += 1

            # Get next possible moves
            children = self.successor(parent)
            # Check leaves for solution
            for child in children:
                if child.state == self.goal:
                    self.depth = child.depth
                    self.cost = child.cost
                    # self.printPath()
                    return True
                else:
                    # If no solution is found, add leaf to stack and continue
                    childKey = ''.join(map(str, child.state))
                    if visited.get(childKey):
                        if visited.get(childKey) > child.cost:
                            # Update the cost of the visited state
                            visited[childKey] = child.cost
                            # Add key value (cost, node) onto the sorted queue
                            pQueue.append((child.cost, child))
                    # If state has not been visited
                    else:
                        visited[childKey] = child.cost
                        pQueue.append((child.cost, child))

            # Check if space in the queue has grown
            if self.space < len(pQueue):
                self.space = len(pQueue)

    def bestFirst(self):
        # Create sorted priority queue
        # This time we replace the cost with the number of misplaced tiles as the heuristic
        pQueue = [(self.hMisplaced(self.start.state), self.start)]
        # Create list of visited state/cost pairs
        visited = set([])

        # Initialize space/time tracking
        self.space = 1
        self.time = 0

        while pQueue:
            # Sort the queued items based on cost
            pQueue = sorted(pQueue, key=lambda x: x[0])
            # Pop item off the queue & visit its leaves
            parent = pQueue.pop(0)
            visited.add((parent[0], parent[1]))
            self.time += 1

            # Get next possible moves
            children = self.successor(parent[1])
            # Check leaves for solution
            for child in children:
                if child.state == self.goal:
                    self.depth = child.depth
                    self.cost = child.cost
                    # self.printPath()
                    return True
                else:
                    # If no solution is found, add leaf to stack and continue
                    childCost = (self.hMisplaced(self.start.state))
                    if (childCost, child) not in visited:
                        # Add key value (cost, node) onto the sorted queue
                        pQueue.append((childCost, child))
                        visited.add((childCost, child))
            # Check if space in the queue has grown
            if self.space < len(pQueue):
                self.space = len(pQueue)

    def aStar(self, h):
        # Create sorted priority queue
        # This time we replace the cost with the number of misplaced tiles as the heuristic
        pQueue = [(self.start.cost + h(self.start.state), self.start)]
        # Create list of visited state/cost pairs
        visited = set([])

        # Initialize space/time tracking
        self.space = 1
        self.time = 0

        while len(pQueue) > 0:
            # Sort the queued items based on path cost
            pQueue = sorted(pQueue, key=lambda x: x[0])
            # Pop item off the queue & visit its leaves
            parent = pQueue.pop(0)[1]

            # Check for goal
            if parent.state == self.goal:
                self.depth = parent.depth
                self.cost = parent.cost
                print("Found")
                return True
            visited.add((parent.cost, ''.join(map(str, parent.state))))
            self.time += 1

            # Get next possible moves
            children = self.successor(parent)
            for child in children:
                if child.state == self.goal:
                    self.depth = child.depth
                    self.cost = child.cost
                    print("Found")
                    return True
                else:
                    # If no solution is found, add leaf to stack and continue
                    childCost = child.cost + h(self.start.state)
                    if (childCost, ''.join(map(str, child.state))) not in visited:
                        # Add key value (cost, node) onto the sorted queue
                        pQueue.append((childCost, child))
                        visited.add((childCost, child))
            # Check if space in the queue has grown
            if self.space < len(pQueue):
                self.space = len(pQueue)

    def hMisplaced(self, state):
        num = 0
        for i in range(len(self.goal)):
            if state[i] != self.goal[i]:
                num += 1
        return num

    def hManhattan(self, state):
        def xyDiff(a, b):
            ax, ay = a % 3, a // 3
            bx, by = b % 3, b // 3
            return abs(ax - bx) + abs(ay - by)

        return sum([xyDiff(state.index(i), self.goal.index(i))
                    for i in range(1, 9)])


    def hMyChoice(self):
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
