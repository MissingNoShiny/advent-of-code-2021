with open("input.txt", "r") as f:
    l = [[int(b) for b in line.strip()] for line in f.readlines()]

c = [sum(x) for x in zip(*l)]

gamma = int("".join(str(int(d > len(l) / 2)) for d in c), 2)
print(gamma * (2**len(c) - 1 - gamma))
