f1 = open("input.txt", "r")
f2 = open("output.txt", "w")
import time
start_time = time.time()
class BST:
    def __init__(self):
        self.mas = []

    def binarySearch(self, arr, low, high, x):
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] == x:
                return None
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                high = mid - 1
            else:
                low = mid + 1
        return high

    def insert(self, val):
        indexpos = self.binarySearch(self.mas, 0, len(self.mas) - 1, val)
        if indexpos != None:
            self.mas = self.mas[: indexpos + 1] + [val] + self.mas[indexpos + 1 :]

bst = BST()
answer = ""
iter = 0
for i in f1.readlines():
    iter += 1
    if iter % 1000 == 0:
        print(str(iter) + "/300000")
    cmd = i.split(" ")
    v, cmd = cmd[1], cmd[0]

    if cmd == "+" and int(v):
        bst.insert(int(v))
    if cmd == "?":
        v = int(v)
        answer += str(bst.mas[-v]) + "\n"
f2.write(answer)

print("--- %s seconds ---" % (time.time() - start_time))
