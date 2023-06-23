from cmath import inf
import time

start = time.time()

f = open('input.txt')
N = int(f.readline())
numbers = [[10**j, int(f.readline())] for j in range(7)]
numbers = list(map(lambda k: [k[0], k[1], k[1] / k[0]], numbers))
numbers.sort(key=lambda amount: amount[2])

min_in, min_sum = inf, 0
N_ = N

for i in numbers:
    if i[0] > N and i[1] < min_in:
        min_in = i[1]
        continue
    while N_ >= i[0]:
        N_ -= i[0]
        min_sum += i[1]

f = open('output.txt', 'w')
f.write(str(min(min_in, min_sum)))
