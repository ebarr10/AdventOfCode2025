def count_rolls(line, positions):
    total = 0
    for pos in positions:
        if pos < 0 or pos >= len(line):
            continue
        if line[pos] == "@":
            total += 1
    return total


def number_of_rolls(lines, main_line_index, check_top=False, check_bottom=False):
    total_rolls = 0
    line_copy = list(lines[main_line_index])
    for index, char in enumerate(lines[main_line_index]):
        if char == "@":
            rolls = 0
            if check_top:
                rolls += count_rolls(
                    lines[main_line_index - 1], [index - 1, index, index + 1]
                )
            rolls += count_rolls(lines[main_line_index], [index - 1, index + 1])
            if check_bottom:
                rolls += count_rolls(
                    lines[main_line_index + 1], [index - 1, index, index + 1]
                )

            if rolls < 4:
                line_copy[index] = "."
                total_rolls += 1
    return total_rolls, "".join(line_copy)


def available_rolls(lines, last_line=False):
    if len(lines) == 2 and last_line:
        return number_of_rolls(lines, 1, check_top=True)
    elif len(lines) == 2:
        return number_of_rolls(lines, 0, check_bottom=True)
    else:
        return number_of_rolls(lines, 1, check_top=True, check_bottom=True)


def run_simulation(lines):
    last_line = False
    total_rolls = 0
    new_lines = []
    for index, line in enumerate(lines):
        matrix_lines = []
        if index - 1 >= 0:
            matrix_lines.append(lines[index - 1])

        matrix_lines.append(line)

        if index + 1 < len(lines):
            matrix_lines.append(lines[index + 1])
        else:
            last_line = True
        rolls, line_copy = available_rolls(matrix_lines, last_line)
        new_lines.append(line_copy)
        total_rolls += rolls
    return total_rolls, new_lines


with open("input.txt", "r") as file:
    content = file.read()
    lines = content.splitlines()
    last_line = False
    total_rolls = 0
    returned_rolls = -1
    while returned_rolls != 0:
        returned_rolls, new_lines = run_simulation(lines)
        lines = new_lines
        total_rolls += returned_rolls
    print(total_rolls)
