with open("input.txt", "r") as f:
    numbers = f.readline().strip().split(",")
    l = [line.strip().split() for line in f.readlines()]
    grids = [l[i+1:i+6] for i in range(0, len(l), 6)]

def f():
    for number in numbers:
        for grid in grids:
            for i in range(5):
                for j in range(5):
                    if grid[i][j] == number:
                        grid[i][j] = "X"
                        if all(el == "X" for el in grid[i]) or all(el == "X" for el in list(zip(*grid))[j]):
                            score = sum([sum(int(el) if el != "X" else 0 for el in line) for line in grid]) * int(number)
                            print(score)
                            return

f()
