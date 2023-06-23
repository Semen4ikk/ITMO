with open('input.txt') as file:
    K, n = map(int, file.readline().split())
    time_for_each = list(map(int, file.readline().split()))
time_spent = 0
shoes_done = 0

time_for_each.sort()

while time_spent < K and time_for_each:
    for item in time_for_each:
        if item + time_spent <= K:
            shoes_done += 1
            time_spent += item
            del time_for_each[time_for_each.index(item)]
        else:
            continue

f = open('output.txt', 'w')
f.write(str(shoes_done))
