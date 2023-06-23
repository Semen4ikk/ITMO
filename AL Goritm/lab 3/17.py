import time

start_time = time.time()

inp = open("input.txt")
out = open("output.txt", "w")

n, m = map(int, inp.readline().split())
grh = [[float("inf") for j in range(n)] for i in range(n)]
amount = 0

for _ in range(m):
    city1, city2 = map(int, inp.readline().split())
    city1, city2 = city1 - 1, city2 - 1
    grh[city1][city2] = 0
    grh[city2][city1] = min(grh[city2][city1], 1)

for k in range(n):
    for i in range(n):
        for j in range(n):
            grh[i][j] = min(grh[i][j], grh[i][k] + grh[k][j])

for l in range(n):
    for m in range(n):
        amount = max(amount, grh[l][m])

out.write(str(amount))
print(time.time() - start_time)
