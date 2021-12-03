with open("input.txt", "r") as f:
    l = [line.strip() for line in f.readlines()]

def f(d):
    for i in range(len((c := l[:])[0])):
        half = len(c) / 2.0
        t = sum(n[i] == "1" for n in c)
        m = "0" if (t >= half) ^ d else "1"
        c = [n for n in c if n[i] == m]
        if len(c) == 1:
            return int(c.pop(), 2)

print(f(True) * f(False))
