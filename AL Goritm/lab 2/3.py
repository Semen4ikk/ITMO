class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        parent = None
        node = self.root
        while node is not None:
            parent = node
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return
        new = Node(key)
        if parent is None:
            self.root = new
        elif key < parent.key:
            parent.left = new
        elif key > parent.key:
            parent.right = new
    
    def min(self, x):
        if self.root is None:
            return 0
        way = []
        node = self.root
        while True:
            way.append(node)
            if x > node.key:
                if node.right is None:
                    break
                node = node.right
            elif x < node.key:
                if node.left is None:
                    return node.key
                node = node.left
            else:
                if node.right is None:
                    break
                node = node.right
                while node.left is not None:
                    node = node.left
                return node.key
        for i in range(len(way) - 1, -1, -1):
            if way[i].key > x:
                return way[i].key
        return 0


filein = open("input.txt")
fileout = open("output.txt", "w")

tree = Tree()


line = filein.readline()
while line != "":
    items = line.split()
    if items[0] == "+":
        tree.insert(int(items[1]))
    else:
        fileout.write(f"{tree.min(int(items[1]))}\n")
    line = filein.readline()


filein.close()
fileout.close()
