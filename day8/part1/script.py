import math
from heapq import heapreplace, heappush, heapify


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
    max_heap = []
    heapify(max_heap)

    points = []
    for line in lines:
        x, y, z = map(int, line.split(","))
        points.append((x, y, z))

    # find x smallest number of distances
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            pointA = points[i]
            pointB = points[j]
            distance = -euclidean_distance(pointA, pointB)

            if len(max_heap) < 1000:
                heappush(max_heap, (distance, i, j))
            else:
                if distance > max_heap[0][0]:
                    heapreplace(max_heap, (distance, i, j))

    # convert into edges
    edges = [(-distance, i, j) for (distance, i, j) in max_heap]
    edges.sort(key=lambda x: x[0])

    N = len(points)
    parent = list(range(N))
    size = [1] * N

    for _, i, j in edges:
        if i == j:
            continue

        union(parent, size, i, j)

    components = []

    for i in range(N):
        if parent[i] == i:
            components.append(size[i])

    components.sort(reverse=True)

    # multiply largest 3
    result = components[0] * components[1] * components[2]
    print(result)
