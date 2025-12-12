def find_all_enumerate(s, c):
    return [i for i, x in enumerate(s) if c == x]


with open("test.txt", "r") as file:
    content = file.read()
    lines = content.splitlines()
    width = len(lines[0])

    keys = range(0, width)
    column_timelines = {key: 0 for key in keys}

    for index, line in enumerate(lines):
        if "S" in line:
            starting_position = line.find("S")
            column_timelines[starting_position] = 1

        manifold_locations = find_all_enumerate(line, "^")
        if manifold_locations:
            new_column_timelines = {key: 0 for key in keys}
            for beam, count in column_timelines.items():
                if beam in manifold_locations and count > 0:
                    # All counts in current beam transfer to all positions
                    if beam + 1 <= width:
                        new_column_timelines[beam + 1] += count
                    if beam - 1 >= 0:
                        new_column_timelines[beam - 1] += count
                else:
                    # Didn't hit anything so carry over count on same position
                    new_column_timelines[beam] += count
            column_timelines = new_column_timelines
    print([(k, v) for k, v in column_timelines.items() if v != 0])
    print(sum(column_timelines.values()))
