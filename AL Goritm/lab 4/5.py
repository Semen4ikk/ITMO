
with open('input.txt', 'r') as inp:
    strr = inp.readline().strip()


def prefixFunction(s):
    p = [0] * (len(s) + 1)
    i, j = 1, 0
    while i < len(s):
        if s[i] == s[j]:
            p[i + 1] = j + 1
            i += 1
            j += 1
        else:
            if j > 0:
                j = p[j]
            else:
                p[i + 1] = 0
                i += 1
    return p[1::]


res = prefixFunction(strr)
with open("output.txt", "w") as outp:
    outp.write(" ".join(map(str, res)))
    print(res)
