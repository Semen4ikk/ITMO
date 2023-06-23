from collections import defaultdict


with open("input.txt", "r") as inp:
    n, m = map(int, inp.readline().split())
    list1 = []
    for i in range(m):
        d1, d2, d3 = map(int, inp.readline().split())
        list1.append([d1 - 1, d2 - 1, d3])

    a, b = map(int, inp.readline().split())
    a -= 1
    b -= 1


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v, w):
        self.graph[u].append((v, w))

    def topologicalSortUtil(self, v, visited, stack):
        visited[v] = True
        if v in self.graph.keys():
            for node, weight in self.graph[v]:
                if not visited[node]:
                    self.topologicalSortUtil(node, visited, stack)
        stack.append(v)

    def shortestPath(self, s):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if not visited[i]:
                self.topologicalSortUtil(s, visited, stack)
        dist = [10 ** 18] * self.V
        dist[s] = 0

        while stack:
            i = stack.pop()
            for node, weight in self.graph[i]:
                if dist[node] > dist[i] + weight:
                    dist[node] = dist[i] + weight

        l = []
        for i in range(self.V):
            c = dist[i] if dist[i] != 10 ** 18 else 10 ** 18
            l.append(c)
        return l


g = Graph(n)
for i in list1:
    g.addEdge(i[0], i[1], i[2])

result = g.shortestPath(a)
answ = result[b]
with open("output.txt", "w") as outp:
    if answ == 10 ** 18:
        print(-1)
        outp.write(str(-1))
    else:
        print(answ)
        outp.write(str(answ))

