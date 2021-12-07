l = [int(n) for n in open("input.txt", "r").read().strip().split(",")]
mean = sum(l)/len(l)
print(sum(abs(mean - n) * (abs(mean - n) + 1) / 2 for n in l))
