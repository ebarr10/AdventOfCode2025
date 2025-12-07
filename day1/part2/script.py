def calculate_position(current_position, direction, steps, extra_zeros):
    if steps == 0:
        return (current_position, extra_zeros)

    if direction == "L":
        temp_position = current_position - steps
        if temp_position < 0:
            if current_position != 0:
                extra_zeros += 1
            return calculate_position(
                100, direction, steps - current_position, extra_zeros
            )
        else:
            return (temp_position, extra_zeros)
    elif direction == "R":
        temp_position = current_position + steps
        if temp_position >= 100:
            if temp_position != 100:
                extra_zeros += 1
            return calculate_position(
                0, direction, steps - (100 - current_position), extra_zeros
            )
        else:
            return (temp_position, extra_zeros)


with open("input.txt", "r") as file:
    content = file.read()
    number_of_times_zero = 0
    number_of_extra_zeros = 0
    current_position = 50
    for rotation in content.splitlines():
        direction = rotation[0]
        steps = int(rotation[1:])
        result = calculate_position(
            current_position, direction, steps, number_of_extra_zeros
        )
        current_position = result[0]
        number_of_extra_zeros = result[1]
        if current_position == 0:
            number_of_times_zero += 1

    print(number_of_times_zero)
    print(number_of_extra_zeros)
    print(number_of_times_zero + number_of_extra_zeros)
