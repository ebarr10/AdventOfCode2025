def parse_json(line):
    largest_values = []
    count = 0
    for value in line:
        count += 1
        # no values --> store next two
        if len(largest_values) < 2:
            largest_values.append(value)

        elif value >= min(largest_values):
            # Smaller than the second value --> move it to the top
            if value < largest_values[1]:
                largest_values = [largest_values[1], value]
            elif value < largest_values[0]:
                largest_values[1] = value

            # If larger than first value
            elif value > largest_values[0] and count < len(line):
                if largest_values[1] > largest_values[0]:
                    largest_values = [largest_values[1], value]
                else:
                    largest_values = [value]

            # If larger than second value --> replace that value
            elif value > largest_values[1]:
                if largest_values[1] > largest_values[0]:
                    largest_values = [largest_values[1], value]
                else:
                    largest_values[1] = value

    return f"{largest_values[0]}{largest_values[1]}"


with open("input.txt", "r") as file:
    content = file.read()
    total = 0
    for line in content.splitlines():
        value = int(parse_json(line))
        total += value
    print(total)
