size_allowed = 12


def efficient_parse_json(line):
    largest_values = []
    while len(line) > 1:
        back_values = line[-(size_allowed - len(largest_values)) + 1 :]

        front_values = line[: -len(back_values)]
        if not front_values:
            break
        max_front_value = max(front_values)
        max_front_index = front_values.index(max_front_value)

        largest_values.append(max_front_value)
        line = line[max_front_index + 1 :]

    largest_values.append(max(line))

    return "".join(v for v in largest_values)


with open("input.txt", "r") as file:
    content = file.read()
    total = 0
    location = 1
    for line in content.splitlines():
        str_value = efficient_parse_json(line)
        total += int(str_value)
        location += 1
    print(total)


# Try to get to work later
def parse_json(line):
    largest_values = []
    count = 0
    for value in line:
        print("Current Value:", value)
        print("Current Largest Values:", largest_values)
        print(
            "Length:",
            len(line),
            "\nCount:",
            count,
            "\nLargest Values:",
            len(largest_values),
        )

        left_in_line = len(line) - count
        print("Left in line:", left_in_line)
        to_compare = largest_values[size_allowed - left_in_line :]
        print("To compare with:", to_compare, "Length:", len(to_compare))

        if (
            largest_values
            and value > largest_values[0]
            and left_in_line > size_allowed - 1
        ):
            largest_values = [value]

        elif (
            to_compare
            and min(to_compare) < value
            and len(largest_values) - len(to_compare) + left_in_line >= size_allowed
        ):
            to_compare_count = 0
            for v in to_compare:
                if v < value:
                    cut_index = len(largest_values) - (
                        len(to_compare) - to_compare_count
                    )
                    print("BEFORE CUT INDEX:", largest_values, " CUT INDEX:", cut_index)
                    largest_values = largest_values[:cut_index] + [value]
                    print("AFTER CUT INDEX:", largest_values)
                    break
                to_compare_count += 1
        elif len(largest_values) == size_allowed and value > largest_values[-1]:
            largest_values[-1] = value

        elif len(largest_values) < size_allowed:
            largest_values.append(value)
        print("\n")
        count += 1

    return "".join(v for v in largest_values)
