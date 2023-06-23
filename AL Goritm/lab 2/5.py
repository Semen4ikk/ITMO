class Node:
    def __init__(self, v=int()):
        self.value = v
        self.left = None
        self.right = None
        self.height_left = 0
        self.height_right = 0
        self.parent = None


class Tree:
    root = None

    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.find(value):
            time = Node(value)
            if self.root is None:
                self.root = time
            else:
                index = self.root
                flag = True
                while flag:
                    if time.value > index.value and index.right is not None:
                        index = index.right
                    elif time.value < index.value and index.left is not None:
                        index = index.left
                    else:
                        flag = False
                if time.value > index.value:
                    time.parent = index
                    index.right = time
                else:
                    time.parent = index
                    index.left = time
                while index is not None:
                    self.root = index
                    index = index.parent
            return time

    def delete(self, value):
        self.delete_top(self.find(value))

    def delete_top(self, time):
        if time:
            if max(time.height_right, time.height_left) == 0:
                if time.parent is None:
                    self.root = None
                else:
                    index = time.parent
                    if time.parent.left == time:
                        time.parent.left = None
                    else:
                        time.parent.right = None
                    while index is not None:
                        self.root = index
                        index = index.parent
            else:
                if time.height_right > time.height_left:
                    time.value = time.right.value
                    self.delete_top(time.right)
                else:
                    time.value = time.left.value
                    self.delete_top(time.left)

    def find(self, value):
        index = self.root
        flag = True
        while flag and index is not None:
            if value > index.value:
                index = index.right
            elif value < index.value:
                index = index.left
            else:
                flag = False
        if index is None:
            return None
        else:
            return index

    def exists(self, value):
        if self.find(value):
            return 'true'
        return 'false'

    def next(self, value):
        time = self.next_time(value, self.root)
        if time == 10 ** 10:
            return 'none'
        else:
            return time

    def next_time(self, value, link):
        if link is not None:
            min_l = self.next_time(value, link.left)
            if min_l <= value:
                min_l = 10 ** 10
            min_r = self.next_time(value, link.right)
            if min_r <= value:
                min_r = 10 ** 10
            return min(min_l, min_r, link.value if link.value > value else 10 ** 10)
        else:
            return 10 ** 10

    def prev(self, value):
        time = self.prev_time(value, self.root)
        if time == -10 ** 11:
            return 'none'
        else:
            return time

    def prev_time(self, value, link):
        if link is not None:
            min_l = self.prev_time(value, link.left)
            if min_l >= value:
                min_l = -10 ** 11
            min_r = self.prev_time(value, link.right)
            if min_r >= value:
                min_r = -10 ** 11
            return max(min_l, min_r, link.value if link.value < value else -10 ** 11)
        else:
            return -10 ** 11


def main(f):
    tree = Tree()
    n = f.readlines()
    for s in n:
        s = s.split()
        if s[0] == 'insert':
            tree.insert(int(s[1]))
        elif s[0] == 'exists':
            print(tree.exists(int(s[1])))
        elif s[0] == 'prev':
            print(tree.prev(int(s[1])))
        elif s[0] == 'next':
            print(tree.next(int(s[1])))
        else:
            tree.delete(int(s[1]))


main(open('input.txt'))
