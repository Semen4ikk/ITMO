import random


def PolyHash(P, l, p, x):
    res = 0
    for i in reversed(range(l)):
        res = (res * x + ord(P[i])) % p
    return res % p


def CalculateHashes(T, l, k, p, x):
    H = [0] * (l - k + 1)
    S = T[l - k : l]
    H[l - k] = PolyHash(S, k, p, x)
    y = 1
    for i in range(1, k + 1):
        y = (y * x) % p
    for i in range(l - k - 1, -1, -1):
        H[i] = (x * H[i + 1] + ord(T[i]) - y * ord(T[i + k]) + p) % p
    return H


with open("input.txt") as f_read:
    with open("output.txt", "w") as f_write:
        while True:
            line = f_read.readline()
            if not line:
                exit()
            s, t = map(str, line.split())
            lS, lT = len(s), len(t)
            k = min(lS, lT)
            p = 10**9 + 7
            x = random.randint(1, p - 1)
            flag = False
            for i in reversed(range(1, k + 1)):
                Hs = CalculateHashes(s, lS, i, p, x)
                Ht = CalculateHashes(t, lT, i, p, x)
                for j in range(len(Hs)):
                    for h in range(len(Ht)):
                        if Hs[j] == Ht[h]:
                            f_write.write(str(j) + " " + str(h) + " " + str(i) + "\n")
                            flag = True
                            break
                    if flag:
                        break
                if flag:
                    break
            if not flag:
                f_write.write("0" + " " + "1" + " " + "0" + "\n")
