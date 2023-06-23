class Node:
    def __init__(self, num):
        self.key = num
        self.left = None
        self.right = None
        self.height = 1


class Tree:
    def height(self, root):
        return root.height if root is not None else 0

    def balance_factor(self, root):
        return self.height(root.right) - self.height(root.left)

    def fix_height(self, root):
        left = self.height(root.left)
        right = self.height(root.right)
        root.height = max(left, right) + 1

    def rotateR(self, root):
        q = root.left
        root.left = q.right
        q.right = root
        self.fix_height(root)
        self.fix_height(q)
        return q

    def rotateL(self, root):
        p = root.right
        root.right = p.left
        p.left = root
        self.fix_height(root)
        self.fix_height(p)
        return p

    def balance(self, root):
        self.fix_height(root)
        if self.balance_factor(root) == 2:
            if self.balance_factor(root.right) < 0:
                root.right = self.rotateR(root.right)
            return self.rotateL(root)
        if self.balance_factor(root) == -2:
            if self.balance_factor(root.left) > 0:
                root.left = self.rotateL(root.left)
            return self.rotateR(root)
        return root

    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return self.balance(root)

    def get_str(self, root):
        que = []
        number = 1
        que.append(root)
        ans = []
        while len(que) > 0:
            node = que.pop(0)
            line = f"{node.key} "
            if node.left is not None:
                number += 1
                line += f"{number} "
                que.append(node.left)
            else:
                line += "0 "

            if node.right is not None:
                number += 1
                line += f"{number}\n"
                que.append(node.right)
            else:
                line += "0\n"
            ans.append(line)
        return ans


inp = open("input.txt")

n = int(inp.readline())
lines = [inp.readline() for _ in range(n)]
lines.reverse()
nodes = {}

tree = Tree()
for i in range(n):
    Ki, Li, Ri = map(int, lines[i].split())
    node = Node(int(Ki))
    nodes[n - i] = node
    if Li != 0 and Ri != 0:
        node.left = nodes[Li]
        node.right = nodes[Ri]
        tree.fix_height(node)
    elif Li != 0:
        node.left = nodes[Li]
        tree.fix_height(node)
    elif Ri != 0:
        node.right = nodes[Ri]
        tree.fix_height(node)
    else:
        node.height = 1

if len(nodes) == 0:
    nodes[1] = None

key = int(inp.readline())
root = tree.insert(nodes[1], key)

out = open("output.txt", "w")
ans = tree.get_str(root)
out.write(f"{len(ans)}\n")
for i in ans:
    out.write(i)

out.close()
inp.close()
