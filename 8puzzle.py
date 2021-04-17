# Procedural 1D array solution

import copy

def read_input(input_file):
    """Read a text file into memory and convert it into a 2D array of integers."""
    matrix = [[]]
    with open(input_file, "r") as file:
        while True:
            line = file.readline().split()
            if line:
                matrix[0] += line
            else:
                break
    for index, element in enumerate(matrix[0]):  # Convert strings to integers
        matrix[0][index] = int(matrix[0][index])
    matrix.append(0)  # Append an additional row that represents a depth value
    return matrix


def get_blank_pos(matrix):
    """Get the index value of the blank tile."""
    for index, element in enumerate(matrix[0]):
        if element == 0:
            return index


def find_adjacent(matrix, dijkstra):
    """Find and enqueue adjacent states.
    If dijkstra is true, increment distance based on swapped tiles.
    If dijkstra is false, increment distance by 1."""
    adjacent = []
    pos = get_blank_pos(matrix)  # Find the index of the blank tile.
    row = pos // 3  # 2D row index of the blank tile.
    col = pos % 3  # 2D column index of the blank tile.


    if row != 0:  # Try to move the blank tile up
        swap_up = copy.deepcopy(matrix)
        if dijkstra:  # Increment depth by the swapped tile's value
            swap_up[1] = matrix[1] + matrix[0][pos]
        else:  # Increment depth by 1
            swap_up[1] = matrix[1] + 1
        swap_up[0][pos], swap_up[0][pos-3] = \
        swap_up[0][pos-3], swap_up[0][pos]
        adjacent.append(swap_up)

    if row != 2:  # Try to move the blank tile down
        swap_down = copy.deepcopy(matrix)
        if dijkstra:  # Increment depth by the swapped tile's value
            swap_down[1] = matrix[1] + matrix[0][pos]
        else:  # Increment depth by 1
            swap_down[1] = matrix[1] + 1
        swap_down[0][pos], swap_down[0][pos+3] = \
        swap_down[0][pos+3], swap_down[0][pos]
        adjacent.append(swap_down)

    if col != 0:  # Try to move the blank tile left
        swap_left = copy.deepcopy(matrix)
        if dijkstra:  # Increment depth by the swapped tile's value
            swap_left[1] = matrix[1] + matrix[0][pos]
        else:  # Increment depth by 1
            swap_left[1] = matrix[1] + 1
        swap_left[0][pos], swap_left[0][pos-1] = \
        swap_left[0][pos-1], swap_left[0][pos]
        adjacent.append(swap_left)

    if col != 2:  # Try to move the blank tile right
        swap_right = copy.deepcopy(matrix)
        if dijkstra:  # Increment depth by the swapped tile's value
            swap_right[1] = matrix[1] + matrix[0][pos]
        else:  # Increment depth by 1
            swap_right[1] = matrix[1] + 1
        swap_right[0][pos], swap_right[0][pos+1] = \
        swap_right[0][pos+1], swap_right[0][pos]
        adjacent.append(swap_right)

    return adjacent


def BFS(initial, goal):
    """Breadth-first search.
    Explore the neighbors of all unvisited vertices of a certain depth before
    traversing to deeper vertices."""
    i = 0
    queue, visited = [], []
    queue += find_adjacent(initial, False)
    while True:
        i += 1
        if queue:
            current = queue.pop(0)
            if current[0] in visited:
                print(f"DUPLICATE")
                debug_print(current, i)
                continue
            else:
                visited.append(current[0])
                print(f"APPEND")
                if current[0] == goal:
                    print(f"GOAL")
                    debug_print(current, i)
                    print(f"Solution: The shortest path cost = {current[1]}")
                    break
        queue += find_adjacent(current, False)
        debug_print(current, i)


def DFS(initial, goal):  # Still needs work
    """Iterative depth-first search.
    Queue adjacent vertices and traverse as deep as possible before backtracking."""
    i = 0
    stack, visited = [], []
    stack += find_adjacent(initial, False)
    while True:
        i += 1
        if stack:
            current = stack.pop(-1)
            if current[0] in visited:
                print(f"DUPLICATE")
                debug_print(current, i)
                continue
            else:
                visited.append(current[0])
                print(f"APPEND")
                if current[0] == goal:
                    print(f"GOAL")
                    debug_print(current, i)
                    print(f"Solution: The shortest path cost = {current[1]}")
                    break
        stack += find_adjacent(current, False)
        debug_print(current, i)


def Dijkstra(initial, goal):  # Unfinished
    """
    i = 0
    total_cost = 0
    queue, visited = [], []
    queue += find_adjacent(initial, True)
    while queue:
        current = min(queue, key=lambda x: x[1])  # Select smallest distance vertex
        queue.pop(queue.index(current))
        #visited.append(current)
        if current[0] == goal:
            print("GOAL")
            break
        else:
            queue += find_adjacent(initial, True)
            for vertex in queue:
                if vertex[1] > current[1] + total_cost:
                    vertex[1] = current[1] + total_cost
        i += 1
        debug_print(current, i)
    """


def debug_print(matrix, iter):
    print(f"ITER: {iter}, DEPTH: {matrix[1]}")
    print(f"ROW 1: {matrix[0][0]} {matrix[0][1]} {matrix[0][2]}")
    print(f"ROW 2: {matrix[0][3]} {matrix[0][4]} {matrix[0][5]}")
    print(f"ROW 3: {matrix[0][6]} {matrix[0][7]} {matrix[0][8]}")
    print("------------------------------")


if __name__ == "__main__":
    initial_state = read_input("input.txt")
    goal_state = [1, 2, 3,
                  8, 0, 4,
                  7, 6, 5]
    print("Choose an option:")
    print("1 - BFS")
    print("2 - DFS")
    choice = input()
    if choice == "1":
        BFS(initial_state, goal_state)
    elif choice == "2":
        DFS(initial_state, goal_state)
    else:
        print("Invalid choice")