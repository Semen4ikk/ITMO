def apples(h, x):
    x = sorted(x, key=lambda apple: apple[1])
    x.reverse()

    res = []
    while len(x) > 0:
        for i in range(len(x)):
            if h - x[i][0] > 0:
                h += x[i][1]
                res.append(x[i][2])
                del x[i]
                break
            elif i == len(x) - 1:
                return -1
    return " ".join(map(str, res))

if __name__ == "__main__":
    n, s = map(int, input().split())
    x = []
    for i in range(n):
        x.append(list(map(int, input().split())))
        x[i][1] = x[i][1] - x[i][0]
        x[i].append(i + 1)

    f = open('output.txt', 'w')
    f.write(str((apples(s, x))))
