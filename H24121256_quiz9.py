import random

def generate_path(maze, N, M):
    i, j = 0, 0
    maze[(i, j)] = 2  # Start point
    while i < N - 1 or j < M - 1:
        if i == N - 1:
            j += 1
        elif j == M - 1:
            i += 1
        else:
            if random.choice([True, False]):
                j += 1
            else:
                i += 1
        maze[(i, j)] = 2  # Path point
    maze[(N-1, M-1)] = 2  # End point

def add_obstacles(maze, min_obstacles, N, M):
    obstacles_added = 0
    while obstacles_added < min_obstacles:
        x, y = random.randint(0, N-1), random.randint(0, M-1)
        if maze.get((x, y), 0) == 0:
            maze[(x, y)] = 1
            obstacles_added += 1

def set_obstacle(maze, N, M):
    try:
        x, y = map(int, input("Enter the coordinates to set an obstacle (x y): ").split())
        if not (0 <= x < N and 0 <= y < M):
            raise KeyError("Coordinates out of bounds.")
        if maze.get((x, y)) == 2:
            raise ValueError("Cannot place an obstacle on the path.")
        maze[(x, y)] = 1
    except ValueError as ve:
        print(f"Error: {ve}")
    except KeyError as ke:
        print(f"Error: {ke}")

def remove_obstacle(maze, N, M):
    try:
        x, y = map(int, input("Enter the coordinates to remove an obstacle (x y): ").split())
        if not (0 <= x < N and 0 <= y < M):
            raise KeyError("Coordinates out of bounds.")
        if maze.get((x, y)) == 2:
            raise ValueError("Cannot remove a path cell.")
        if maze.get((x, y)) != 1:
            raise ValueError("No obstacle at the specified coordinates.")
        maze[(x, y)] = 0
    except ValueError as ve:
        print(f"Error: {ve}")
    except KeyError as ke:
        print(f"Error: {ke}")

def print_maze(maze, N, M):
    for i in range(N):
        for j in range(M):
            if maze.get((i, j)) == 1:
                print(" X ", end="")
            elif maze.get((i, j)) == 2:
                print(" O ", end="")
            else:
                print("   ", end="")
        print()

def read_maze_file(file_name):
    try:
        with open(file_name) as file:
            maze_blueprint = [line.strip().split() for line in file]
            N = len(maze_blueprint)
            M = len(maze_blueprint[0])
            maze = {(i, j): int(maze_blueprint[i][j]) for i in range(N) for j in range(M)}
        return maze, N, M
    except IOError:
        print("IOError occurred in main function. File not found. Please enter a valid file name.")
        return None, None, None
    except ValueError:
        print("Error: File format is incorrect.")
        return None, None, None

def main():
    while True:
        file_name = input("Enter file name: ")
        maze, N, M = read_maze_file(file_name)
        if maze is not None:
            break

    while True:
        try:
            min_obstacles = int(input("Enter the minimum number of obstacles to add: "))
            if min_obstacles < 0:
                raise ValueError("Number of obstacles cannot be negative.")
            break
        except ValueError as ve:
            print(f"Error: {ve}")

    generate_path(maze, N, M)
    add_obstacles(maze, min_obstacles, N, M)

    while True:
        print_maze(maze, N, M)
        print("Options:")
        print("1. Set an obstacle")
        print("2. Remove an obstacle")
        print("3. Exit")
        option = input("Enter your option: ")
        if option == "1":
            set_obstacle(maze, N, M)
        elif option == "2":
            remove_obstacle(maze, N, M)
        elif option == "3":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
