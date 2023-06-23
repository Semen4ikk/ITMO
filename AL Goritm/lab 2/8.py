inp = open("input.txt")

n = int(inp.readline())
woods = []
deeps = [0] * (n + 1)

for _ in range(n):
    value, left, right = map(int, inp.readline().split())
    woods.append((left, right))

inp.close()

# starts from leaves
for i in range(n - 1, -1, -1):
    if (woods[i][0] == 0) and (woods[i][1] == 0):
        deeps[i + 1] = 1
    else:
        deeps[i + 1] = max(deeps[woods[i][0]], deeps[woods[i][1]]) + 1

out = open("output.txt", "w")
out.write(str(deeps[1]) if n > 0 else "0")
out.close()
