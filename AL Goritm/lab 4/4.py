def poly_hash(P, p, x=128):
    h = 0
    for i in reversed(range(len(P))):
        h = (h * x + ord(P[i])) % p
    return h % p


def precompute_hashes(T, P, p, x):
    H = [0] * (len(T) - len(P) + 1)
    S = T[len(T) - len(P): len(T)]
    ind = len(T) - len(P)
    H[ind] = poly_hash(S, p, x)
    y = 1
    for i in range(1, len(P) + 1):
        y = (y * x) % p
    for i in range(len(T) - len(P) - 1, -1, -1):
        H[i] = (x * H[i + 1] + ord(T[i]) - y * ord(T[i + len(P)]) + p) % p
    return H


with open("input.txt") as inp:
    word = inp.readline()[:-1]
    n = int(inp.readline())
    sp = []
    for _ in range(n):
        sp.append(list(map(int, inp.readline().split())))

hashes = dict()
coll = dict()
k = 1
l = len(word)
p, o = 10 ** 9 + 7, 10 ** 9 + 9

while k <= l:
    hashes[k] = []
    coll[k] = []
    for i in range(l - k + 1):
        hashes[k].append(poly_hash(word[i:i + k], p))
        coll[k].append(poly_hash(word[i:i + k], o))
    k += 1

with open('output.txt', 'w') as outp:
    for i in range(n):
        count = sp[i][-1]
        first = sp[i][0]
        second = sp[i][1]
        if hashes[count][first] == hashes[count][second] and coll[count][first] == coll[count][second]:
            outp.write(f'YES\n')
        else:
            outp.write(f'NO\n')
