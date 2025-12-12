import math


def euclidean_distance(pointA, pointB):
    x = (pointA[0] - pointB[0]) ** 2
    y = (pointA[1] - pointB[1]) ** 2
    z = (pointA[2] - pointB[2]) ** 2
    return math.sqrt(x + y + z)


def find(parent, i):
    while parent[i] != i:
        i = parent[i]
    return i


def union(parent, size, i, j):
    rootA = find(parent, i)
    rootB = find(parent, j)
    if rootA == rootB:
        return

    sizeA = size[rootA]
    sizeB = size[rootB]
    if sizeA >= sizeB:
        parent[rootB] = rootA
        size[rootA] += sizeB
    else:
        parent[rootA] = rootB
        size[rootB] += sizeA


with open("input.txt", "r") as file:
    content = file.read()
    lines = content.splitlines()

    points = []
    for line in lines:
        x, y, z = map(int, line.split(","))
        points.append((x, y, z))

    # find x smallest number of distances
    edges = []
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            distance = euclidean_distance(points[i], points[j])
            edges.append((distance, i, j))

    # Sort edges
    edges.sort(key=lambda x: x[0])

    N = len(points)
    parent = list(range(N))
    size = [1] * N
    components = N

    for _, i, j in edges:
        rootA = find(parent, i)
        rootB = find(parent, j)

        if rootA == rootB:
            continue

        union(parent, size, i, j)
        components -= 1

        if components == 1:
            # Last Union
            x1 = points[i][0]
            x2 = points[j][0]
            print(f"Answer: {x1*x2}")
            break
