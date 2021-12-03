with open("input.txt", "r") as f:
    l = [int(line) for line in f.readlines()]

print(sum(l[i+3] > l[i] for i in range(len(l) - 3)))
