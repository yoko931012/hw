import random

def generate_maze(N, M):
    maze = [[' ' for _ in range(M)] for _ in range(N)]
    return maze

def print_maze(maze):
    for row in maze:
        print('+---' * len(row) + '+')
        print('|' + '|'.join('{:^3}'.format(cell) for cell in row) + '|')
    print('+---' * len(maze[0]) + '+')

def generate_path(N, M):
    path = [(0, 0)]  # Start from the top-left corner
    current_cell = (0, 0)

    while current_cell != (N - 1, M - 1):  # Continue until reaching the bottom-right corner
        next_moves = []
        if current_cell[0] < N - 1:
            next_moves.append((current_cell[0] + 1, current_cell[1]))  # Move down
        if current_cell[1] < M - 1:
            next_moves.append((current_cell[0], current_cell[1] + 1))  # Move right

        next_cell = random.choice(next_moves)
        path.append(next_cell)
        current_cell = next_cell

    return path

def add_obstacles(maze, num_obstacles):
    N, M = len(maze), len(maze[0])
    obstacles_added = 0
    while obstacles_added < num_obstacles:
        row = random.randint(0, N-1)
        col = random.randint(0, M-1)
        if maze[row][col] == ' ':
            maze[row][col] = 'X'  # Place obstacle in the empty cell
            obstacles_added += 1
    return maze
if __name__ == "__main__":
    N = int(input("Enter the number of rows (N): "))
    M = int(input("Enter the number of columns (M): "))
    num_obstacles = int(input("Enter the number of obstacles (0-{}): ".format((N-1) * (M-1))))

    while num_obstacles < 0 or num_obstacles > (N-1) * (M-1):
        num_obstacles = int(input("Re-enter again (0-{}): ".format((N-1) * (M-1))))

    maze = generate_maze(N, M)
    path = generate_path(N, M)
    add_obstacles(maze, num_obstacles)

    # Mark the path in the maze
    for row, col in path:
        maze[row][col] = ' '

    # Print the maze
    print("Generated Maze:")
    print_maze(maze)

