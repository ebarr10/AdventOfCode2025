def calculate_area(p1, p2):
    x1, y1 = map(int, p1.split(","))
    x2, y2 = map(int, p2.split(","))

    x = abs(x2 - x1) + 1
    y = abs(y2 - y1) + 1
    return x * y


with open("input.txt", "r") as file:
    content = file.read()
    lines = content.splitlines()

    areas = {}
    areas_totals = []
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            area = calculate_area(lines[i], lines[j])
            areas_totals.append(area)

    areas_totals.sort(reverse=True)
    print(f"Largest Area: {areas_totals[0]}")
