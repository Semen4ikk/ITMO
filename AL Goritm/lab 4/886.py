with open('input.txt', 'r') as inp:
    strr = inp.readline().strip()

M = 1
coef = len(strr)
lenn_ = len(strr)

while M ** 2 <= lenn_:
    if lenn_ % M == 0:
        H = lenn_ // M
        # print(H)
        if strr[:M] * H == strr:
            coef = M
            break

    M += 1
result = len(strr) // coef
# print(result)
with open('output.txt', 'w') as outp:
    outp.write(str(result))
