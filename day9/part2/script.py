from collections import deque


def calculate_area(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    x = abs(x2 - x1) + 1
    y = abs(y2 - y1) + 1
    return x * y


def mark_outside(grid):
    # Flood fill from all borders
    h, w = len(grid), len(grid[0])
    stack = deque()

    for x in range(w):
        stack.append((x, 0))
        stack.append((x, h - 1))
    for y in range(h):
        stack.append((0, y))
        stack.append((w - 1, y))

    while stack:
        x, y = stack.pop()
        if not (0 <= x < w and 0 <= y < h):
            continue
        if grid[y][x] in (1, 2):
            continue

        grid[y][x] = 2
        stack.extend([(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)])


def print_grid(grid, numbers=False):
    for row in grid:
        line = ""
        for cell in row:
            if numbers:
                line += f"{cell}\t"
            elif cell == 1:
                line += "#"
            elif cell == 2:
                line += "x"
            else:
                line += "."
        print(line)
    print("\n")


with open("input.txt", "r") as file:
    content = file.read()
    lines = content.splitlines()

    points = []
    for line in lines:
        x, y = map(int, line.split(","))
        points.append((x, y))

    print("Setting up Boundaries...")
    edges = []
    for i in range(len(points)):
        edges.append((points[i], points[(i + 1) % len(points)]))

    # Coordinate compression (ONLY vertices + padding)
    print("Compressing Coordinates...")
    xs, ys = set(), set()
    for x, y in points:
        xs.add(x)
        xs.add(x - 1)
        xs.add(x + 1)
        ys.add(y)
        ys.add(y - 1)
        ys.add(y + 1)

    xs = sorted(xs)
    ys = sorted(ys)

    x_index = {x: i for i, x in enumerate(xs)}
    y_index = {y: i for i, y in enumerate(ys)}

    width = len(xs)
    height = len(ys)

    print("Setting up the Grid...")
    grid = [[0 for _ in range(width)] for _ in range(height)]

    # Rasterize walls AFTER compression
    for (x1, y1), (x2, y2) in edges:
        gx1, gy1 = x_index[x1], y_index[y1]
        gx2, gy2 = x_index[x2], y_index[y2]

        if gx1 == gx2:
            for y in range(min(gy1, gy2), max(gy1, gy2) + 1):
                grid[y][gx1] = 1
        else:
            for x in range(min(gx1, gx2), max(gx1, gx2) + 1):
                grid[gy1][x] = 1

    print("Marking the outside points...")
    mark_outside(grid)
    # print_grid(grid)

    print("Calculate the number of outside values starting at (0, 0)...")
    outside_counts = [[0 for _ in range(width)] for _ in range(height)]
    for i in range(height):
        for j in range(width):
            total = 0
            if i - 1 >= 0:
                total += outside_counts[i - 1][j]
            if j - 1 >= 0:
                total += outside_counts[i][j - 1]
            if i - 1 >= 0 and j - 1 >= 0:
                total -= outside_counts[i - 1][j - 1]

            if grid[i][j] == 2:
                total += 1
            outside_counts[i][j] = total

    print("Recalibrating points...")
    new_points = []
    for x, y in points:
        new_points.append((x_index[x], y_index[y]))

    print("Final Calculation...")
    max_area = 0
    for i in range(len(new_points)):
        for j in range(i + 1, len(new_points)):
            # Compressed (for validity)
            x1, y1 = new_points[i]
            x2, y2 = new_points[j]

            # Original (for area)
            ox1, oy1 = points[i]
            ox2, oy2 = points[j]

            area = calculate_area((ox1, oy1), (ox2, oy2))
            if area <= max_area:
                continue

            x3 = min(x1, x2) + 1
            x4 = max(x1, x2) - 1
            y3 = min(y1, y2) + 1
            y4 = max(y1, y2) - 1

            # Empty interior is always valid
            if x3 > x4 or y3 > y4:
                max_area = area
                continue

            A = outside_counts[y4][x4]
            B = outside_counts[y3 - 1][x4] if y3 > 0 else 0
            C = outside_counts[y4][x3 - 1] if x3 > 0 else 0
            D = outside_counts[y3 - 1][x3 - 1] if x3 > 0 and y3 > 0 else 0

            if A - B - C + D == 0:
                max_area = area

    print(f"Largest Area: {max_area}")


def recursive_mark_outside(grid, x, y):
    # Boundary
    value = grid[y][x]

    # Boundary
    if value == 1:
        return
    # Already marked outside
    if value == 2:
        return

    # Mark as outside
    grid[y][x] = 2

    height = len(grid)
    width = len(grid[0])

    # Right
    if x + 1 < width:
        recursive_mark_outside(grid, x + 1, y)
    # Left
    if x - 1 >= 0:
        recursive_mark_outside(grid, x - 1, y)
    # Up
    if y + 1 < height:
        recursive_mark_outside(grid, x, y + 1)
    # Down
    if y - 1 >= 0:
        recursive_mark_outside(grid, x, y - 1)
