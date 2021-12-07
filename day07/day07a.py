l = [int(n) for n in open("input.txt", "r").read().strip().split(",")]
median = sorted(l)[len(l)//2]
print(sum(abs(median - n) for n in l))
