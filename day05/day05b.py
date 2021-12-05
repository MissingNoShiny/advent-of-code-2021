with open("input.txt", "r") as f:
    l = [[[int(n) for n in point.split(",")] for point in line.strip().split(" -> ")] for line in f.readlines()]

count = 0
points = {}
for line in l:
    [[x1, y1], [x2, y2]] = line
    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2) + 1):
            points[x1][i] = points.setdefault(x1, {}).get(i, 0) + 1
            if points[x1][i] == 2:
                count +=1
    elif y1 == y2:
        for i in range(min(x1, x2), max(x1, x2) + 1):
            points[i][y1] = points.setdefault(i, {}).get(y1, 0) + 1
            if points[i][y1] == 2:
                count +=1
    elif abs(x1 - x2) == abs(y1 - y2):
        for i in range(abs(x1 - x2) + 1):
            x, y = x1 + i * (1 if x2 > x1 else -1), y1 + i * (1 if y2 > y1 else -1)
            points[x][y] = points.setdefault(x, {}).get(y, 0) + 1
            if points[x][y] == 2:
                count +=1

print(count)
