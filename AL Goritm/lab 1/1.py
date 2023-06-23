with open('input.txt') as file:
    n, W = list(map(int, file.readline().split()))
    items = [list(map(int, file.readline().split())) for i in range(n)]

items.sort(key=lambda item: (item[0] / item[1]), reverse=True)

taken = 0
max_parts = 0

for k, current in items:
    if taken + current <= W:
        max_parts += k
        taken += current
    else:
        max_parts += (k / current) * (W - taken)
        break
f = open('output.txt', 'w')
f.write(str((round(max_parts, 4))))
