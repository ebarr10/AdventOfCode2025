def find_all_enumerate(s, c):
    return [i for i, x in enumerate(s) if c == x]


with open("input.txt", "r") as file:
    content = file.read()
    lines = content.splitlines()
    current_beam_positions = set()
    locations_of_splits = set()
    width = 0
    for index, line in enumerate(lines):
        if "S" in line:
            current_beam_positions = set([line.find("S")])
            width = len(line)
        manifold_locations = find_all_enumerate(line, "^")
        print(
            f"Index: {index}"
            f"\nLine: {line}"
            f"\nMainfold Locations: {manifold_locations}"
            f"\nCurrent Beam Locations: {sorted(list(current_beam_positions))}"
        )
        if manifold_locations:
            new_beam_positions = set()
            for beam in current_beam_positions:
                if beam in manifold_locations:
                    # Beam hit a fold
                    locations_of_splits.add((beam, index))

                    # Add new beam locations
                    if beam + 1 <= width:
                        new_beam_positions.add(beam + 1)
                    if beam - 1 >= 0:
                        new_beam_positions.add(beam - 1)
                else:
                    # Didn't hit anything so carry on
                    new_beam_positions.add(beam)
            print(f"New Beam Locations: {sorted(list(new_beam_positions))}")
            current_beam_positions = new_beam_positions
        print("\n")
    print(len(locations_of_splits))
