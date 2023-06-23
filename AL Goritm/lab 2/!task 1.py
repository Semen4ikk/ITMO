import time

t_start = time.perf_counter()
import tracemalloc

tracemalloc.start()

from common.Node import Node
from common.TreeBuilder import TreeBuilder


def in_order(tree: Node):
    if tree is not None:
        in_order(tree.leftChild)
        print(tree.node, end=" ")
        in_order(tree.rightChild)


def pre_order(tree: Node):
    if tree is not None:
        print(tree.node, end=" ")
        pre_order(tree.leftChild)
        pre_order(tree.rightChild)


def post_order(tree: Node):
    if tree is not None:
        post_order(tree.leftChild)
        post_order(tree.rightChild)
        print(tree.node, end=" ")

f1 = open('input.txt')
n = int(f1.readline())
input_data = []
for line in f1:
    k, l, r = map(int, line.split(" "))
    input_data.append([k, l, r])

tree = TreeBuilder.buildBST(input_data)
in_order(tree)
print()
pre_order(tree)
print()
post_order(tree)


print("Время работы: %s секунд " % (time.perf_counter() - t_start))
mc, mp = tracemalloc.get_traced_memory()
print("Memory: current %f KiB, peak %f KiB" % (mc / 1024, mp / 1024))

