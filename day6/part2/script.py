from functools import reduce


def evaluate_operation(x, action, y):
    return eval(f"{x}{action}{y}")


with open("input.txt", "r") as file:
    content = file.read()
    lines = content.splitlines()
    operators = {
        index: value
        for index, value in enumerate(lines[len(lines) - 1])
        if value in ["*", "+"]
    }

    lines = lines[: len(lines) - 1]
    largest_line = len(max(lines, key=len))

    new_lines = []
    pos = 0
    for k, v in operators.items():
        col_digits = []
        col = k
        while True:
            new_value = ""
            for line in lines:
                if col < len(line) and line[col] != " ":
                    new_value += line[col]
            if col >= largest_line or new_value == "":
                break
            col_digits.append(new_value)
            col += 1
        new_lines.append(col_digits)
        pos += 1

    total = 0
    for index, action in enumerate(operators):
        total += reduce(
            lambda x, y: evaluate_operation(x, operators[action], y),
            new_lines[index],
        )
    print(total)
