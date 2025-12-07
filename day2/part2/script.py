def get_invalid_numbers(ids):
    start, end = map(int, ids.split("-"))
    all_values = range(start, end + 1)
    added_values = 0
    for number in all_values:
        string_number = str(number)
        num_length = len(string_number)
        is_odd_length = num_length % 2 != 0
        if not is_odd_length:
            first_half = string_number[: num_length // 2]
            second_half = string_number[num_length // 2 :]
            if first_half == second_half:
                added_values += number
                continue
        # Check for circular patterns and remove ends that make a trivial match
        if string_number in (string_number + string_number)[1:-1]:
            added_values += number
    return added_values


with open("input.txt", "r") as file:
    content = file.read()
    all_ids = content.split(",")
    total_invalid_amount = 0
    for ids in all_ids:
        invalid_numbers = get_invalid_numbers(ids)
        print("IDs:", ids, " Invalid Numbers:", invalid_numbers)
        total_invalid_amount += invalid_numbers

    print(total_invalid_amount)
