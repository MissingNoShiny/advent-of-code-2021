with open("input.txt", "r") as f:
    l = [line.split(" ") for line in f.readlines()]

position = sum(int(line[1]) for line in l if line[0] == "forward")

aim = 0
depth = 0

for line in l:
    if line[0] == "down":
        aim += int(line[1])
    elif line[0] == "up":
        aim -= int(line[1])
    else:
        depth += int(line[1]) * aim

print(depth * position)
