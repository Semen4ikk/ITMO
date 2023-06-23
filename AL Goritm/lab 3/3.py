from collections import defaultdict

def dfs(v, p=-1):
    used[v] = True
    for u in graph[v]:
        if not used[u]:
            dfs(u, v)
        elif u != p:
            f.write("1")
            exit()
    used[v] = False

graph = {}

with open("input.txt") as file:
    n, m = map(int, file.readline().split())
    for i in range(n):
        graph[i + 1] = []
    for i in range(m):
        u, v = map(int, file.readline().split())
        graph[u].append(v)

f = open("output.txt", "w")

used = defaultdict(lambda: False)

for i in range(n):
    if not used[i + 1]:
        dfs(i + 1)

f.write("0")
