import time
start_time = time.time()
inp = open("input.txt")
out = open("output.txt", "w")
n, m = map(int, inp.readline().split())
graph = {str(i): set() for i in range(1, n + 1)}
for i in range(m):
    edge1, edge2 = inp.readline().split()
    graph[edge1].add(edge2)
    graph[edge2].add(edge1)
def dfs(start, graph, bypassed):
    bypassed.add(start)
    for neighbor in graph[start]:
        if neighbor not in bypassed:
            dfs(neighbor, graph, bypassed)
bypassed = set()
amount = 0
for vertex in graph:
    if vertex not in bypassed:
        dfs(vertex, graph, bypassed)
        amount += 1
out.write(str(amount))
print(time.time() - start_time)
