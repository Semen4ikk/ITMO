filein = open("input.txt")
n, height = filein.readline().split()
n = int(n)
height = float(height)
filein.close()

error = 0.1 ** 10


def equal(a, b):
    return abs(a - b) <= error


def less(a, b):
    return (a < b) and (not equal(a, b))

Ц
def more(a, b):
    return (a > b) and (not equal(a, b))


heights = [0] * n
heights[0] = height
res = 1000000000
left = 0
right = heights[0]

while less(left, right):
    heights[1] = (left + right) / 2
    heights[-1] = 0
    isUp = False
    for i in range(2, n):
        heights[i] = 2 * heights[i-1] - heights[i-2] + 2
        if not more(heights[i], 0):
            isUp = True
            break
    if more(heights[-1], 0):
        res = min(res, heights[-1])
    if isUp:
        left = heights[1]
    else:
        right = heights[1]

fileout = open("output.txt", "w")
fileout.write("%.6f" % res)
fileout.close()
