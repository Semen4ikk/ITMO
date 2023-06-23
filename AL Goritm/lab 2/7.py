class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


def check(root):
    if root is None:
        return None
    que = [(root, -1000000000, 10000000000)]
    while len(que) > 0:
        line = que.pop(0)
        isnode = line[0]
        if isnode.left is not None:
            if (isnode.left.key >= isnode.key) or (isnode.left.key >= line[2]) or (isnode.left.key <= line[1]):
                return False
            que.append((isnode.left, line[1], isnode.key))
        if isnode.right is not None:
            if (isnode.right.key < isnode.key) or (isnode.right.key > line[2]) or (isnode.right.key <= line[1]):
                return False
            que.append((isnode.right, isnode.key, line[2]))
    return True


filein = open('input.txt')
n = int(filein.readline())
lines = [filein.readline() for _ in range(n)]
nodes = []
K = []
L = []
R = []

for i in range(n):
    Ki, Li, Ri = lines[i].split()
    node = Node(int(Ki))
    nodes.append(node)
    K.append(int(Ki))
    L.append(int(Li))
    R.append(int(Ri))

for i in range(n):
    left = L[i]
    right = R[i]
    if left != -1:
        nodes[i].left = nodes[left]
    if right != -1:
        nodes[i].right = nodes[right]
filein.close()

result = 0
if nodes:
    result = check(nodes[0])
else:
    result = True

fileout = open('output.txt', 'w')
if result:
    fileout.write("CORRECT")
else:
    fileout.write("INCORRECT")
fileout.close()
