from itertools import combinations


def check_subsets(subsets, answer):
    return False


def calculate_min_presses(line):
    k = 0
    answer = line[0]
    print(answer)
    buttons = [set(map(int, b.strip("()").split(","))) for b in line[1:-1]]
    watts = line[-1]

    print(buttons)
    print(f"XOR: {buttons[0]}, {buttons[1]} --> {buttons[0]^buttons[1]}")

    found_answer = False
    while not found_answer and k <= len(buttons):
        subsets = list(combinations(buttons, k))
        print(f"Subsets: {subsets}")
        found_answer = check_subsets(subsets, answer)
        k += 1


with open("test.txt", "r") as file:
    content = file.read()
    lines = content.splitlines()
    total = 0
    for line in lines:
        parsed_line = line.split(" ")
        calculate_min_presses(parsed_line)
