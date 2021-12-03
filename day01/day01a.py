with open("input.txt", "r") as f:
    l = [int(line) for line in f.readlines()]

print(sum(l[i+1] > l[i] for i in range(len(l) - 1)))
