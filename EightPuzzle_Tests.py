from EightPuzzle import *

# inital states
easy = [1, 3, 4, 8, 6, 2, 7, 0, 5]
medium = [2, 8, 1, 0, 4, 3, 7, 6, 5]
hard = [5, 6, 7, 4, 0, 8, 3, 2, 1]

# goal state
goal = [1, 2, 3, 8, 0, 4, 7, 6, 5]

eightPuzzle = EightPuzzle()
strategy = ["Breadth First", "Depth First", "Iterative Deepening",
            "Uniform Cost", "Best First", "A*", "A* 2", "A* 3"]


# Breadth First Tests
#Easy
eightPuzzle.setGame(easy, goal, strategy[1])
eightPuzzle.search()
#Medium
eightPuzzle.setGame(medium, goal, strategy[1])
eightPuzzle.search()
#Hard
eightPuzzle.setGame(hard, goal, strategy[1])
eightPuzzle.search()

'''
# Depth First Tests
#Easy
eightPuzzle.setGame(easy, goal, strategy[2])
eightPuzzle.search()
#Medium
eightPuzzle.setGame(medium, goal, strategy[2])
eightPuzzle.search()
#Hard
eightPuzzle.setGame(hard, goal, strategy[2])
eightPuzzle.search()

# Iterative Deepening Tests
#Easy
eightPuzzle.setGame(easy, goal, strategy[3])
eightPuzzle.search()
#Medium
eightPuzzle.setGame(medium, goal, strategy[3])
eightPuzzle.search()
#Hard
eightPuzzle.setGame(hard, goal, strategy[3])
eightPuzzle.search()

# Uniform Cost Tests
#Easy
eightPuzzle.setGame(easy, goal, strategy[4])
eightPuzzle.search()
#Medium
eightPuzzle.setGame(medium, goal, strategy[4])
eightPuzzle.search()
#Hard
eightPuzzle.setGame(hard, goal, strategy[4])
eightPuzzle.search()

# Best First Tests
#Easy
eightPuzzle.setGame(easy, goal, strategy[5])
eightPuzzle.search()
#Medium
eightPuzzle.setGame(medium, goal, strategy[5])
eightPuzzle.search()
#Hard
eightPuzzle.setGame(hard, goal, strategy[5])
eightPuzzle.search()

# A* Tests
#Easy
eightPuzzle.setGame(easy, goal, strategy[6])
eightPuzzle.search()
#Medium
eightPuzzle.setGame(medium, goal, strategy[6])
eightPuzzle.search()
#Hard
eightPuzzle.setGame(hard, goal, strategy[6])
eightPuzzle.search()

# A* 2 Tests
#Easy
eightPuzzle.setGame(easy, goal, strategy[7])
eightPuzzle.search()
#Medium
eightPuzzle.setGame(medium, goal, strategy[7])
eightPuzzle.search()
#Hard
eightPuzzle.setGame(hard, goal, strategy[7])
eightPuzzle.search()

# A* 3 Tests
#Easy
eightPuzzle.setGame(easy, goal, strategy[8])
eightPuzzle.search()
#Medium
eightPuzzle.setGame(medium, goal, strategy[8])
eightPuzzle.search()
#Hard
eightPuzzle.setGame(hard, goal, strategy[8])
eightPuzzle.search()

'''
