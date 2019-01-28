from collections import deque
from sortedcontainers import SortedDict
from copy import deepcopy
import time


class EightPuzzle:
    def __init__(self):
        # Algorithm specific inputs
        self.start = None
        self.goal = None
        self.strategy = None
        self.difficulty = None
        # Global reporting variables
        self.time = None
        self.space = None
        self.depth = None
        self.cost = None

    '''
    This setter is used to configure the 8 puzzle to the appropriate start, finish, search strategy, and difficulty of
    that strategy. This last setting is merely for reporting purposes as the true difficulty is set by the start start.
    '''
    def setGame(self, start, goal, strategy, difficulty):
        self.start = Node(start, None, 1, 0)
        self.goal = goal
        self.strategy = strategy
        self.difficulty = difficulty

    '''
    The successor function takes a node as input and produces up to four potential children nodes as output.
    The number is determined by the position of the blank square on the current node state. Based on this, the
    Left/Right/Up/Down moves can be represented by creating new state spaces that represent this positional shit 
    of the blank square. The choices are limited by the current index of the blank square.
    
    Additionally, the new child nodes are supplied new depth and cost values. Depth is incremented 1 from the parent
    node depth, and the cost is incremented by the value of the swapped non-blank piece. This is how we account for
    the MODIFIED cost in our search strategies.'''
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
        # Right
        if i not in (2, 5, 8):
            child_right = Node(deepcopy(parent.state), parent, parent.depth + 1, parent.cost + parent.state[i+1])
            child_right.state[i] = parent.state[i + 1]
            child_right.state[i + 1] = parent.state[i]
            successorStates.append(child_right)
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
        return successorStates

    '''
    This method is used by the EightPuzzle object to initialize the search strategy that will be explored.
    The selection is based on the global 'strategy' variable. Upon completion, the printSummary method is called
    to display the results.'''
    def search(self):
        strategy = self.strategy
        if strategy == "Breadth First":
            result = self.breadthFirst()
        elif strategy == "Depth First":
            result = self.depthFirst()
        elif strategy == "Iterative Deepening":
            result = self.iterativeDeepening()
        elif strategy == "Uniform Cost":
            result = self.aStar(self.hUniform)
        elif strategy == "Best First":
            result = self.aStar(self.hBest)
        elif strategy == "A*":
            result = self.aStar(self.fMisplaced)
        elif strategy == "A* 2":
            result = self.aStar(self.fManhattan)
        elif strategy == "A* 3":
            result = self.aStar(self.fMyChoice)
        else:
            print("Unknown search strategy has been selected!")
        self.printSummary(result)
        return

    '''
    This method is used to display the search results in the command line terminal.
    Example:
    ------------------------------------------------------
    Strategy: A* 3
    Difficulty: Easy
    Start = [1, 3, 4, 8, 6, 2, 7, 0, 5]
    Goal = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    Depth: 6
    Cost: 17
    Time: 81
    Space: 152
        '''
    def printSummary(self, result):
        print("\n------------------------------------------------------")
        print("Strategy: {}\nDifficulty: {}".format(self.strategy, self.difficulty))
        print("Start = {}\nGoal = {}".format(self.start.state, self.goal))
        if result:
            print("Depth: {}\nCost: {}".format(self.depth, self.cost))
            print("Time: {}".format(self.time))
            print("Space: {}".format(self.space))
        else:
            print("Error: Timed out before solution was discovered")
        return

    '''
    This is an optional method that may be employed to print out a visual trace of the solution to the 
    8 puzzle problem for each of its states.
    Example:
    Depth: 10,  Cost: 31
    |-----------|
    | 1 | 2 | 3 |
    |-----------|
    | 8 | 0 | 4 |
    |-----------|
    | 7 | 6 | 5 |
    |-----------|
    '''
    def printPath(self, head):
        if head:
            self.printPath(head.parent)
            head.printState()
        return

    def breadthFirst(self):
        # Create queue
        queue = deque()
        queue.append(self.start)

        # Create list of visited nodes
        visited = {}

        # Initialize space/time tracking
        self.space = 1
        self.time = 0

        while 0 < len(queue):
            # Pop item off the queue
            parent = queue.popleft()
            visited[(''.join(map(str, parent.state)))] = parent
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
        return False

    def depthFirst(self):
        # Create queue, and list of visited states
        stack = deque()
        stack.append(self.start)

        # Maintain set of all visited nodes
        visited = {}

        # Initialize space/time tracking
        self.space = 1
        self.time = 0

        while 0 < len(stack):
            # Pop item off the queue & visit its leaves
            parent = stack.pop()
            visited[(''.join(map(str, parent.state)))] = parent
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
                    if ''.join(map(str, child.state)) not in visited:
                        stack.append(child)

            # Check if space in the queue has grown
            if self.space < len(stack):
                self.space = len(stack)
        return False

    '''
    This implementation of the iterative deepening algorithm relies on a helper method that implements a version
    of Depth First Search whose node traversal is capped by a maximum depth. The loop runs until the helper returns
    with verification that the solution was discovered. Each iteration consists of a new call to the subroutine with
    an incremented depth level.'''
    def iterativeDeepening(self):
        # Initialize space/time tracking
        self.space = 1
        self.time = 0
        solutionFound = False
        currentDepth = 1
        while solutionFound == False:
            solutionFound = self.ID_Helper(currentDepth)
            currentDepth += 1
        return solutionFound

    def ID_Helper(self, limit):
        # Create queue
        stack = deque()
        stack.append(self.start)

        # Maintain set of all elements visited
        visited = set(''.join(map(str, self.start.state)))

        while 0 < len(stack):
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
                    # Now check that child node depth meets the current limit before adding to the stack!
                    childKey = ''.join(map(str, child.state))
                    if childKey not in visited and child.depth <= limit:
                        visited.add(childKey)
                        stack.append(child)

            # Check if space in the queue has grown
            if self.space < len(stack):
                self.space = len(stack)
        return False


    '''
    This aStar function implements searches for the Uniform-Cost, Best-First, A*, A*1, and A*2 algorithms. 
    It does this by swapping in the correct heuristic function as an argument. Unlike the previous algorithms, 
    the unexpanded nodes are maintained on a priority queue, with expanded nodes stored in a hash table for reference.
    Items on the queue are sorted according to the f(n) value returned from the heuristic function.
    '''
    def aStar(self, f):
        # Create sorted priority queue
        # This time we replace the cost with the number of misplaced tiles as the heuristic
        h = f(self.start)
        pQueue = [(h, self.start)]

        # Create list of visited state/cost pairs
        visited = set([])

        # Initialize space/time tracking
        self.space = 1
        self.time = 0

        while 0 < len(pQueue) < 40000:
            # Sort the queued items based on path cost
            pQueue = sorted(pQueue, key=lambda x: x[0])

            # Pop item off the queue & visit its leaves
            parent = pQueue.pop(0)[1]
            parentKey = ''.join(map(str, parent.state))

            # Add to visited tracking
            visited.add((parent.cost, parentKey))
            self.time += 1

            # Get next possible moves
            children = self.successor(parent)
            for child in children:
                if child.state == self.goal:
                    self.depth = child.depth
                    self.cost = child.cost
                    return True

                else:
                    # If no solution is found, add leaf to stack and continue
                    childCost = f(child)
                    childKey = ''.join(map(str, child.state))
                    # Check for duplicates on the queue
                    if (childCost, childKey) not in visited:
                        # Add key value (cost, node) onto the sorted queue
                        pQueue.append((childCost, child))
                        visited.add((childCost, childKey))

            # Check if space in the queue has grown
            if self.space < len(pQueue):
                self.space = len(pQueue)
        return False


    '''
    The heuristic function for Uniform-Cost merely returns the cost stored on the node object.
    '''
    def hUniform(self, node):
        return node.cost

    '''
    The heuristic function for best first is similar to the misplaced tile heuristic, however g(n) is not
    added to h(n) before returned. 
    '''
    def hBest(self, node):
        state = node.state
        num = 0
        for i in range(len(self.goal)):
            if state[i] != self.goal[i]:
                num += 1
        return num

    '''
    This is the misplaced tiles heuristic, which calculates the number of tiles in the incorrect position. This is
    the heuristic used for A*2.
    '''
    def fMisplaced(self, node):
        num = 0
        state = node.state
        for i in range(len(self.goal)):
            if state[i] != self.goal[i]:
                num += 1
        return node.cost + num

    '''
    The manhattan heuristic calculates the number of squares each till needs to move along the both the x and y axis 
    to get to their correct position.
    '''
    def fManhattan(self, node):
        sum = 0
        state = node.state
        for i in range(1, 9):
            a = state.index(i)
            b = self.goal.index(i)
            ax, ay = a % 3, a // 3
            bx, by = b % 3, b // 3
            sum += (abs(ax - bx) + abs(ay - by))
        return node.cost + sum

    '''
    My heuristic is an iteration of the manhattan heuristic. However, I sum it against the node depth as opposed to
    the path cost. This is an intuitive solution in the sense that one would expect an increased depth a strong
    indicator of increased search space, an therefore decreased performance. Further, this mitigates the modified cost
    value of the individual pieces.
    '''
    def fMyChoice(self, node):
        sum = 0
        state = node.state
        for i in range(1, 9):
            a = state.index(i)
            b = self.goal.index(i)
            ax, ay = a % 3, a // 3
            bx, by = b % 3, b // 3
            sum += (abs(ax - bx) + abs(ay - by))
        return node.depth + sum

    def fmyChoice2(self, node):
        pass

'''
This is node class that is stored on queue. Each maintains the puzzle state it represents, the parent state, 
the current depth relative to its parent, and the total cost relative to its parent.'''
class Node:
    def __init__(self, _state, _parent, _depth, _cost):
        self.state = _state
        self.parent = _parent
        self.depth = _depth
        self.cost = _cost

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
