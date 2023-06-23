from collections import deque
import time

start_time = time.time()
inp = open("input.txt")
out = open("output.txt", "w")

n = int(inp.readline())
curr_graph = dict()

for i in range(n):
    main_p = inp.readline()
    curr_graph[main_p] = set()
    m = int(inp.readline())
    for j in range(m):
        curr_graph[main_p].add(inp.readline())
    inp.readline()


def check_recursion(graph, proc):
    queue, bypassed, queue_set = deque(), set(), set()
    queue.append(proc)
    queue_set.add(proc)
    while queue:
        c = queue.popleft()
        queue_set.remove(c)
        bypassed.add(c)
        for node in graph[c]:
            if node == proc:
                return True
            if node not in bypassed and node not in queue_set:
                queue.append(node)
                queue_set.add(node)
    return False


for proc in curr_graph:
    if check_recursion(curr_graph, proc):
        out.write("YES" + "\n")
    else:
        out.write("NO" + "\n")

print(time.time() - start_time)
