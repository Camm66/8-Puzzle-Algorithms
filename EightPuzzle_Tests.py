from EightPuzzle import *

# initial states
easy = [1, 3, 4, 8, 6, 2, 7, 0, 5]
medium = [2, 8, 1, 0, 4, 3, 7, 6, 5]
hard = [5, 6, 7, 4, 0, 8, 3, 2, 1]

# goal state
goal = [1, 2, 3, 8, 0, 4, 7, 6, 5]

eightPuzzle = EightPuzzle()
strategy = ["Breadth First", "Depth First", "Iterative Deepening",
            "Uniform Cost", "Best First", "A*", "A* 2", "A* 3"]

testing = True
while testing:
    print("Available Tests:")
    print("1 : Breadth First\n"
          + "2 : Depth First\n"
          + "3 : Iterative Deepening\n"
          + "4 : Uniform Cost\n"
          + "5 : Best First\n"
          + "6 : A*\n"
          + "7 : A* 2\n"
          + "8 : A* 3\n"
          + "666: Run All\n"
          + "Type 0 to exit\n")
    action = int(raw_input("Please enter the number of the test would like to run: "))
    if action == 0:
        print("Goodbye...")
        testing = False
        break
    if action != 666:
        print("1 == Easy\n2 == Medium\n3 == Hard")
        difficulty = int(raw_input("Please Enter the difficulty: "))
    if action == 1:
    # Breadth First Tests
        if difficulty == 1:
            eightPuzzle.setGame(easy, goal, strategy[0], "Easy")
            eightPuzzle.search()
        elif difficulty == 2:
            eightPuzzle.setGame(medium, goal, strategy[0], "Medium")
            eightPuzzle.search()
        elif difficulty == 3:
            eightPuzzle.setGame(hard, goal, strategy[0], "Hard")
            eightPuzzle.search()

    elif action == 2:
    # Depth First Tests
        if difficulty == 1:
            eightPuzzle.setGame(easy, goal, strategy [1], "Easy")
            eightPuzzle.search()
        elif difficulty == 2:
            eightPuzzle.setGame(medium, goal, strategy[1], "Medium")
            eightPuzzle.search()
        elif difficulty == 3:
            eightPuzzle.setGame(hard, goal, strategy[1], "Hard")
            eightPuzzle.search()

    elif action == 3:
    # Iterative Deepening Tests
        if difficulty == 1:
            eightPuzzle.setGame(easy, goal, strategy[2], "Easy")
            eightPuzzle.search()
        elif difficulty == 2:
            eightPuzzle.setGame(medium, goal, strategy[2], "Medium")
            eightPuzzle.search()
        elif difficulty == 3:
            eightPuzzle.setGame(hard, goal, strategy[2], "Hard")
            eightPuzzle.search()

    elif action == 4:
    # Uniform Cost Tests
        if difficulty == 1:
            eightPuzzle.setGame(easy, goal, strategy[3], "Easy")
            eightPuzzle.search()
        elif difficulty == 2:
            eightPuzzle.setGame(medium, goal, strategy[3], "Medium")
            eightPuzzle.search()
        elif difficulty == 3:
            eightPuzzle.setGame(hard, goal, strategy[3], "Hard")
            eightPuzzle.search()

    elif action == 5:
    # Best First Tests
        if difficulty == 1:
            eightPuzzle.setGame(easy, goal, strategy[4], "Easy")
            eightPuzzle.search()
        elif difficulty == 2:
            eightPuzzle.setGame(medium, goal, strategy[4], "Medium")
            eightPuzzle.search()
        elif difficulty == 3:
            eightPuzzle.setGame(hard, goal, strategy[4], "Hard")
            eightPuzzle.search()

    elif action == 6:
    # A * Tests
        if difficulty == 1:
            eightPuzzle.setGame(easy, goal, strategy[5], "Easy")
            eightPuzzle.search()
        elif difficulty == 2:
            eightPuzzle.setGame(medium, goal, strategy[5], "Medium")
            eightPuzzle.search()
        elif difficulty == 3:
            eightPuzzle.setGame(hard, goal, strategy[5], "Hard")
            eightPuzzle.search()

    elif action == 7:
    # A * 2 Tests
        if difficulty == 1:
            eightPuzzle.setGame(easy, goal, strategy[6], "Easy")
            eightPuzzle.search()
        elif difficulty == 2:
            eightPuzzle.setGame(medium, goal, strategy[6], "Medium")
            eightPuzzle.search()
        elif difficulty == 3:
            eightPuzzle.setGame(hard, goal, strategy[6], "Hard")
            eightPuzzle.search()

    elif action == 8:
    # A * 3 Tests
        if difficulty == 1:
            eightPuzzle.setGame(easy, goal, strategy[7], "Easy")
            eightPuzzle.search()
        elif difficulty == 2:
            eightPuzzle.setGame(medium, goal, strategy[7], "Medium")
            eightPuzzle.search()
        elif difficulty == 3:
            eightPuzzle.setGame(hard, goal, strategy[7], "Hard")
            eightPuzzle.search()

    elif action == 666:
        # Breadth First Tests
        eightPuzzle.setGame(easy, goal, strategy[0], "Easy")
        eightPuzzle.search()
        eightPuzzle.setGame(medium, goal, strategy[0], "Medium")
        eightPuzzle.search()
        eightPuzzle.setGame(hard, goal, strategy[0], "Hard")
        eightPuzzle.search()
        # Depth First Tests
        eightPuzzle.setGame(easy, goal, strategy[1], "Easy")
        eightPuzzle.search()
        eightPuzzle.setGame(medium, goal, strategy[1], "Medium")
        eightPuzzle.search()
        eightPuzzle.setGame(hard, goal, strategy[1], "Hard")
        eightPuzzle.search()
        # Iterative Deepening Tests
        eightPuzzle.setGame(easy, goal, strategy[2], "Easy")
        eightPuzzle.search()
        eightPuzzle.setGame(medium, goal, strategy[2], "Medium")
        eightPuzzle.search()
        eightPuzzle.setGame(hard, goal, strategy[2], "Hard")
        eightPuzzle.search()
        # Uniform Cost Tests
        eightPuzzle.setGame(easy, goal, strategy[3], "Easy")
        eightPuzzle.search()
        eightPuzzle.setGame(medium, goal, strategy[3], "Medium")
        eightPuzzle.search()
        eightPuzzle.setGame(hard, goal, strategy[3], "Hard")
        eightPuzzle.search()
        # Best First Tests
        eightPuzzle.setGame(easy, goal, strategy[4], "Easy")
        eightPuzzle.search()
        eightPuzzle.setGame(medium, goal, strategy[4], "Medium")
        eightPuzzle.search()
        eightPuzzle.setGame(hard, goal, strategy[4], "Hard")
        eightPuzzle.search()
        # A * Tests
        eightPuzzle.setGame(easy, goal, strategy[5], "Easy")
        eightPuzzle.search()
        eightPuzzle.setGame(medium, goal, strategy[5], "Medium")
        eightPuzzle.search()
        eightPuzzle.setGame(hard, goal, strategy[5], "Hard")
        eightPuzzle.search()
        # A * 2 Tests
        eightPuzzle.setGame(easy, goal, strategy[6], "Easy")
        eightPuzzle.search()
        eightPuzzle.setGame(medium, goal, strategy[6], "Medium")
        eightPuzzle.search()

        eightPuzzle.setGame(hard, goal, strategy[6], "Hard")
        eightPuzzle.search()
        # A * 3 Tests
        eightPuzzle.setGame(easy, goal, strategy[7], "Easy")
        eightPuzzle.search()
        eightPuzzle.setGame(medium, goal, strategy[7], "Medium")
        eightPuzzle.search()
        eightPuzzle.setGame(hard, goal, strategy[7], "Hard")
        eightPuzzle.search()
    else:
        print("Invalid Selection")
    print("\n\n")
