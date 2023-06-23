
class BNode:
    def __init__(self, value=0, left=0, right=0):
        self.value = value
        self.left = left
        self.right = right


def tree_input():
    inp = open("input.txt")
    n = int(inp.readline())

    if n == 0:
        return True
    arr = []
    for _ in range(n):
        inp = list(input().split())
        arr.append(BNode(int(inp[0]), int(inp[1]) - 1, int(inp[2]) - 1))
    print(arr)
    result = binary_tree_check(arr, 0, -float('inf'), float('inf'))
    if result:
        return True
    return False


def binary_tree_check(inp, i, left, right):
    if i == -1:
        return True
    if inp[i].value <= left or inp[i].value >= right:
        return False
    check = binary_tree_check(inp, inp[i].left, left, inp[i].value) and binary_tree_check(
        inp, inp[i].right, inp[i].value, right)
    return check


if __name__ == "__main__":
    res = tree_input()
    if res:
        print('YES')
    else:
        print('NO')
