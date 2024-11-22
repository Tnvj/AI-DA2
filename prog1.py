import numpy as np
from copy import deepcopy

# Define the goal state
GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Manhattan Distance Heuristic
def manhattan_distance(state):
    distance = 0
    for r in range(3):
        for c in range(3):
            value = state[r][c]
            if value != 0:
                target_r, target_c = divmod(value - 1, 3)
                distance += abs(r - target_r) + abs(c - target_c)
    return distance

# Misplaced Tiles Heuristic
def misplaced_tiles(state):
    return sum(
        1 for r in range(3) for c in range(3) 
        if state[r][c] != 0 and state[r][c] != GOAL_STATE[r][c]
    )

# Find the empty tile's position
def find_empty_tile(state):
    for r in range(3):
        for c in range(3):
            if state[r][c] == 0:
                return r, c

# Generate possible moves
def generate_neighbors(state):
    r, c = find_empty_tile(state)
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_state = deepcopy(state)
            new_state[r][c], new_state[nr][nc] = new_state[nr][nc], new_state[r][c]
            neighbors.append(new_state)
    return neighbors

# Hill Climbing Algorithm
def hill_climbing(initial_state, heuristic="manhattan"):
    current = deepcopy(initial_state)
    path = [current]
    heuristic_func = manhattan_distance if heuristic == "manhattan" else misplaced_tiles

    print("Initial State:")
    display_board(current)

    step = 0
    while True:
        step += 1
        print(f"Step {step}:")
        neighbors = generate_neighbors(current)

        # Sort neighbors by the heuristic function
        neighbors.sort(key=heuristic_func)
        best_neighbor = neighbors[0]

        print("Neighbors evaluated:")
        for neighbor in neighbors:
            display_board(neighbor)
            print(f"Heuristic Cost: {heuristic_func(neighbor)}\n")

        # If the best neighbor isn't better, stop
        if heuristic_func(best_neighbor) >= heuristic_func(current):
            print("No improvement possible. Reached local maximum or plateau.\n")
            break

        print("Moving to the best neighbor:")
        display_board(best_neighbor)
        print(f"Best Heuristic Cost: {heuristic_func(best_neighbor)}\n")
        
        current = best_neighbor
        path.append(current)

    return current, heuristic_func(current), path

# Display the board state
def display_board(board):
    for row in board:
        print(" ".join(str(x) if x != 0 else " " for x in row))
    print()

# Test Cases
test_cases = [
    {
        "initial": [[1, 2, 3], [4, 0, 6], [7, 5, 8]],
        "description": "Almost solved, minor moves needed (easy success case)"
    },
    {
        "initial": [[1, 2, 3], [4, 5, 6], [0, 7, 8]],
        "description": "Stuck due to local maxima (classic failure case)"
    },
    {
        "initial": [[1, 2, 3], [4, 5, 6], [8, 7, 0]],
        "description": "Requires large steps to solve, highlighting plateau"
    }
]

for i, test in enumerate(test_cases, start=1):
    print(f"Test Case {i}: {test['description']}")
    print("Initial Board:")
    display_board(test["initial"])

    for heuristic in ["manhattan", "misplaced"]:
        print(f"Using {heuristic.title()} Heuristic:")
        result, cost, path = hill_climbing(test["initial"], heuristic)
        print("Final Board:")
        display_board(result)
        print(f"Heuristic Cost: {cost}")
        print(f"Steps Taken: {len(path)}")
        status = "Solved successfully!" if cost == 0 else "Failed to solve."
        print(f"Status: {status}\n")

    print("=" * 50)
