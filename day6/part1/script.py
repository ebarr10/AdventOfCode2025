from functools import reduce


def evaluate_operation(x, y, action):
    return eval(f"{x}{action}{y}")


with open("input.txt", "r") as file:
    content = file.read()
    lines = content.splitlines()
    mathimatical_operations = list(filter(None, lines[len(lines) - 1].split(" ")))
    lines = lines[: len(lines) - 1]
    for index, line in enumerate(lines):
        lines[index] = list(filter(None, line.split(" ")))

    total = 0
    for index, action in enumerate(mathimatical_operations):
        total += reduce(
            lambda x, y: evaluate_operation(x, y, action),
            list(map(lambda x: x[index], lines)),
        )
    print(total)
