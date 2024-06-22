import curses
import random

def create_obstacles(height, width):
    obstacles = []
    obstacle_count = (height * width) // 20
    for _ in range(obstacle_count):
        if random.choice([True, False]):
            start_x = random.randint(0, width - 5)
            start_y = random.randint(0, height - 1)
            for i in range(5):
                if start_x + i < width:
                    obstacles.append([start_y, start_x + i])
        else:
            start_x = random.randint(0, width - 1)
            start_y = random.randint(0, height - 5)
            for i in range(5):
                if start_y + i < height:
                    obstacles.append([start_y + i, start_x])
    return obstacles

def generate_food(height, width, snake, obstacles):
    food = None
    while food is None:
        nf = [random.randint(1, height - 2), random.randint(1, width - 2)]
        if nf not in snake and nf not in obstacles:
            food = nf
    return food

def main(stdscr):
    curses.curs_set(0)
    height, width = stdscr.getmaxyx()
    win = curses.newwin(height, width, 0, 0)
    win.keypad(1)
    win.timeout(100)

    snake_x = width // 4
    snake_y = height // 2
    snake = [
        [snake_y, snake_x],
        [snake_y, snake_x - 1],
        [snake_y, snake_x - 2]
    ]
    obstacles = create_obstacles(height, width)
    normal_food = generate_food(height, width, snake, obstacles)
    special_food = generate_food(height, width, snake, obstacles)

    win.addch(normal_food[0], normal_food[1], 'π')
    win.addch(special_food[0], special_food[1], 'X')
    for ob in obstacles:
        win.addch(ob[0], ob[1], curses.ACS_CKBOARD | curses.A_REVERSE)

    key = curses.KEY_RIGHT
    score = {'normal': 0, 'special': 0}
    paused = False

    while True:
        next_key = win.getch()
        if next_key == 32:  # space bar for pause/resume
            paused = not paused
            if paused:
                win.addstr(height // 2, width // 2 - 6, "Paused")
                win.refresh()
            continue
        
        if paused:
            continue

        key = key if next_key == -1 else next_key

        if key not in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
            key = prev_key

        if key == curses.KEY_DOWN:
            new_head = [snake[0][0] + 1, snake[0][1]]
        elif key == curses.KEY_UP:
            new_head = [snake[0][0] - 1, snake[0][1]]
        elif key == curses.KEY_LEFT:
            new_head = [snake[0][0], snake[0][1] - 1]
        elif key == curses.KEY_RIGHT:
            new_head = [snake[0][0], snake[0][1] + 1]

        new_head[0] = new_head[0] % height
        new_head[1] = new_head[1] % width

        if new_head in snake or new_head in obstacles:
            break

        snake.insert(0, new_head)

        if snake[0] == normal_food:
            score['normal'] += 1
            normal_food = generate_food(height, width, snake, obstacles)
            win.addch(normal_food[0], normal_food[1], 'π')
        elif snake[0] == special_food:
            score['special'] += 1
            if len(snake) > 1:
                snake.pop()
            special_food = generate_food(height, width, snake, obstacles)
            win.addch(special_food[0], special_food[1], 'X')
        else:
            snake.pop()

        win.clear()
        win.addch(normal_food[0], normal_food[1], 'π')
        win.addch(special_food[0], special_food[1], 'X')
        for ob in obstacles:
            win.addch(ob[0], ob[1], curses.ACS_CKBOARD | curses.A_REVERSE)
        for segment in snake:
            win.addch(segment[0], segment[1], '■')

    curses.endwin()
    print(f"Game Over! Normal food eaten: {score['normal']}, Special food eaten: {score['special']}")

if __name__ == "__main__":
    curses.wrapper(main)
