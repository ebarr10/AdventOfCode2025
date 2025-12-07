def calculate_position(current_position, direction, steps):
    if steps == 0:
        return current_position

    if direction == "L":
        temp_position = current_position - steps
        if temp_position < 0:
            return calculate_position(100, direction, steps - current_position)
        else:
            return temp_position
    elif direction == "R":
        temp_position = current_position + steps
        if temp_position >= 100:
            return calculate_position(0, direction, steps - (100 - current_position))
        else:
            return temp_position


with open("input.txt", "r") as file:
    content = file.read()
    number_of_times_zero = 0
    current_position = 50
    for rotation in content.splitlines():
        direction = rotation[0]
        steps = int(rotation[1:])
        current_position = calculate_position(current_position, direction, steps)
        print("CURRENT POSITION: ", current_position)
        if current_position == 0:
            number_of_times_zero += 1

    print(number_of_times_zero)
