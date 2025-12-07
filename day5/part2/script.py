with open("input.txt", "r") as file:
    content = file.read()
    ingredients = content.split("\n\n")
    sort_ids = {}
    for value in ingredients[0].split("\n"):
        start, end = value.split("-")
        if start in sort_ids:
            v = sort_ids[start]
            if int(end) > int(v):
                sort_ids[start] = end
        else:
            sort_ids[start] = end

    sort_ids = dict(sorted(sort_ids.items(), key=lambda item: int(item[0])))

    position = 0
    while position < len(sort_ids) - 1:
        current_start = list(sort_ids.keys())[position]
        current_end = sort_ids[current_start]
        next_start = list(sort_ids.keys())[position + 1]
        next_end = sort_ids[next_start]
        if int(current_end) >= int(next_start):
            if int(current_end) < int(next_end):
                sort_ids[current_start] = next_end
            del sort_ids[next_start]
        else:
            position += 1

    total_fresh = 0
    for k, v in sort_ids.items():
        total_fresh += int(v) - int(k) + 1
    print(total_fresh)
