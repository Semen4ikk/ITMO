import math

def countDiff(sub, mx):
    subLen = len(sub)
    sub1 = sub[:math.floor(subLen/2)]
    sub2 = sub[math.ceil(subLen/2):]
    sub2 = sub2[::-1]
    diff = 0
    for i in range(subLen//2):
        if sub1[i] != sub2[i]: diff += 1
        if diff > mx: return False
    return True

f = open('input.txt', 'r')
n, k = map(int, f.readline().split())
word = f.readline()
pols = []


halfPolyAmount = 0
for i in range(n):
    for j in range(i+1, n+1):
        if len(word[i:j]) <= (k+1+k%2):
            halfPolyAmount += 1
        elif countDiff(word[i:j], k):
            halfPolyAmount += 1
print(halfPolyAmount)
