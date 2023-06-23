with open('input.txt', 'r') as inp:
    strr = inp.readline().strip()


def zfun(s):
    out = []
    if not s:
        return out
    i, slen = 1, len(s)
    out.append(slen)
    while i < slen:
        left, right = 0, i
        while right < slen and s[left] == s[right]:
            left += 1
            right += 1
        out.append(left)
        i += 1
    return out[1::]


def z_func(s):
    z = [0] * len(s)
    left, right = 0, 0
    for i in range(1, len(s)):
        z[i] = max(0, min(z[i - left], right - i))
        while i + z[i] < len(s) and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > right:
            left, right = i, i + z[i]
    return z[1::]


res = z_func(strr)

with open("output.txt", "w") as outp:
    outp.write(" ".join(map(str, res)))

