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
                self.balance_number(index)
                while index is not None:
                    self.balance_number(index)
                    index = self.balance(index)
                    self.root = index
                    index = index.parent
            return time

    def delete(self, value):
        self.delete_vertex(self.find(value))

    def delete_vertex(self, time):
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
                        self.balance_number(index)
                        index = self.balance(index)
                        self.root = index
                        index = index.parent
            else:
                if time.height_right > time.height_left:
                    time.value = time.right.value
                    self.delete_vertex(time.right)
                else:
                    time.value = time.left.value
                    self.delete_vertex(time.left)

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

    # log(n)
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

    def balance_number(self, vertex):
        if vertex:
            vertex.height_left = 0
            vertex.height_right = 0
            if vertex.left:
                vertex.height_left = 1 + max(vertex.left.height_right, vertex.left.height_left)
            if vertex.right:
                vertex.height_right = 1 + max(vertex.right.height_right, vertex.right.height_left)

    def balance(self, vertex):
        vertex = self.slt(vertex)
        vertex = self.srt(vertex)
        vertex = self.blt(vertex)
        vertex = self.brt(vertex)
        return vertex

    def slt(self, vertex):
        if vertex is not None and vertex.height_right - vertex.height_left == 2 and vertex.right.height_left <= vertex.right.height_right:
            time_par = vertex.parent
            time_left = vertex.right.left
            vertex.right.left = vertex
            vertex.parent = vertex.right
            vertex.right = time_left
            vertex.parent.parent = time_par
            if time_par is not None:
                if time_par.left == vertex:
                    time_par.left = vertex.parent
                else:
                    time_par.right = vertex.parent
            self.balance_number(vertex)
            vertex = vertex.parent
            self.balance_number(vertex)
        return vertex

    def srt(self, vertex):
        if vertex is not None and vertex.height_left - vertex.height_right == 2 and vertex.left.height_right <= vertex.left.height_left:
            time_par = vertex.parent
            time_right = vertex.left.right
            vertex.left.right = vertex
            vertex.parent = vertex.left
            vertex.left = time_right
            vertex.parent.parent = time_par
            if time_par is not None:
                if time_par.left == vertex:
                    time_par.left = vertex.parent
                else:
                    time_par.left = vertex.parent
            self.balance_number(vertex)
            vertex = vertex.parent
            self.balance_number(vertex)
        return vertex

    def blt(self, vertex):
        if vertex is not None and vertex.height_right - vertex.height_left == 2 and vertex.right.height_left > vertex.right.height_right:
            vertex.right = self.srt(vertex.right)
            vertex = self.slt(vertex)
        return vertex

    def brt(self, vertex):
        if vertex is not None and vertex.height_left - vertex.height_right == 2 and vertex.left.height_right <= vertex.left.height_left:
            vertex.left = self.slt(vertex.left)
            vertex = self.srt(vertex)
        return vertex


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
