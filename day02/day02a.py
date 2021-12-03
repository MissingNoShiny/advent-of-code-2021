with open("input.txt", "r") as f:
    l = [line.split(" ") for line in f.readlines()]

depth = sum(int(line[1]) for line in l if line[0] == "down") - sum(int(line[1]) for line in l if line[0] == "up")
position = sum(int(line[1]) for line in l if line[0] == "forward")

print(position * depth)
