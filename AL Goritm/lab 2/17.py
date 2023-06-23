from collections import deque

class Node:
    def __init__(self, key, left=None, right=None, parent=None):
        self.left = left
        self.right = right
        self.parent = parent
        self.key = key


class SplayTree:
    def set_parent(self, child, parent):
        if child is not None:
            child.parent = parent

    def keep_parent(self, node):
        self.set_parent(node.left, node)
        self.set_parent(node.right, node)

    def rotate(self, parent, child):
        grandparent = parent.parent
        if grandparent is not None:
            if grandparent.left == parent:
                grandparent.left = child
            else:
                grandparent.right = child

        if parent.left == child:
            parent.left, child.right = child.right, parent
        else:
            parent.right, child.left = child.left, parent

        self.keep_parent(child)
        self.keep_parent(parent)
        child.parent = grandparent

    def splay(self, node):
        if node.parent is None:
            return node
        parent = node.parent
        grandparent = parent.parent
        if grandparent is None:
            self.rotate(parent, node)
            return node
        else:
            zigzig = (grandparent.left == parent) == (parent.left == node)
            if zigzig:
                self.rotate(grandparent, parent)
                self.rotate(parent, node)
            else:
                self.rotate(parent, node)
                self.rotate(grandparent, node)
        return self.splay(node)

    def find(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return self.splay(node)
        if key < node.key and node.left is not None:
            return self.find(node.left, key)
        if key > node.key and node.right is not None:
            return self.find(node.right, key)
        return self.splay(node)

    def split(self, root, key):
        if root is None:
            return None, None
        root = self.find(root, key)
        if root.key == key:
            self.set_parent(root.left, None)
            self.set_parent(root.right, None)
            return root.left, root.right
        if root.key < key:
            right, root.right = root.right, None
            self.set_parent(right, None)
            return root, right
        else:
            left, root.left = root.left, None
            self.set_parent(left, None)
            return left, root

    def insert(self, root, key):
        left, right = self.split(root, key)
        root = Node(key, left, right)
        self.keep_parent(root)
        return root

    def merge(self, left, right):
        if right is None:
            return left
        if left is None:
            return right
        right = self.find(right, left.key)
        right.left, left.parent = left, right
        return right

    def remove(self, root, key):
        root = self.find(root, key)
        self.set_parent(root.left, None)
        self.set_parent(root.right, None)
        return self.merge(root.left, root.right)

    def sum(self, root, l, r):
        stack = deque()
        nums = []
        if root is None:
            return 0
        while True:
            stack.append(root)
            if (root.left is None) or (root.key <= l):
                break
            root = root.left
        while True:
            if len(stack) != 0:
                nums.append(stack[-1].key)
                if (stack[-1].right is not None) and (stack[-1].key <= r):
                    root = stack.pop().right
                else:
                    stack.pop()
                    continue
                while True:
                    stack.append(root)
                    if (root.left is None) or (root.key <= l):
                        break
                    root = root.left
            if len(stack) == 0:
                summ = 0
                for num in nums:
                    if (num >= l) and (num <= r):
                        summ += num
                return summ


M = 1000000001
last_op = 0

inp = open("input.txt")
out = open("output.txt", "w")
n = int(inp.readline())

root = None
tree = SplayTree()

for i in range(n):
    line = inp.readline().split()
    num = (int(line[1]) + last_op) % M
    if line[0] == "?":
        root = tree.find(root, num)
        if (root is not None) and (root.key == num):
            out.write("Found\n")
        else:
            out.write("Not found\n")
    elif line[0] == "+":
        if root is None:
            root = Node(num)
        else:
            root = tree.insert(root, num)
    elif line[0] == "-":
        if root is not None:
            root = tree.remove(root, num)
    elif line[0] == "s":
        num_s = (int(line[2]) + last_op) % M
        last_op = tree.sum(root, num, num_s)
        out.write(f"{last_op}\n")

inp.close()
out.close()
