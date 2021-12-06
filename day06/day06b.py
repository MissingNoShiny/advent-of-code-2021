counters = [0] * 9
for n in open("input.txt", "r").read().strip().split(","):
    counters[int(n)] += 1

for _ in range(256):
    counters.append(counters.pop(0))
    counters[6] += counters[8]

print(sum(counters))
