with open("input.txt", "r") as file:
    content = file.read()
    ingredients = content.split("\n\n")
    total_fresh = 0
    ids_list = []
    for value in ingredients[1].split("\n"):
        for range_ids in ingredients[0].split("\n"):
            start, end = range_ids.split("-")
            if int(start) <= int(value) <= int(end):
                total_fresh += 1
                break

    print(total_fresh)
