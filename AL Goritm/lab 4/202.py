with open('input.txt') as inp:
    t = str(inp.readline().rstrip())
    s = str(inp.readline().rstrip())
x = len(s)
S = s + '#' + t
w = len(S)


def prefix(s):
    n = len(s)
    p = [0] * n
    for i in range(1, n):
        j = p[i - 1]
        while j > 0 and s[i] != s[j]:
            j = p[j - 1]
        if s[i] == s[j]:
            j += 1
        p[i] = j
    return p


pi = prefix(S)
ans = 0
tmp = []
for i in range(w):
    if pi[i] == x:
        ans += 1
        tmp.append(i - x - x)

# print(pi)

# print(ans)
for k in range(len(tmp)):
    tmp[k] = str(tmp[k])
stroke = ' '.join(tmp)

with open('output.txt', 'w') as outp:
    outp.write(str(stroke))
