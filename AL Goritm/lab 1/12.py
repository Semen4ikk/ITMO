import time

t_start = time.perf_counter()
import tracemalloc

tracemalloc.start()


def find_a_middle(x):
    if sum(x) % 2 == 0:
        s = sum(x) / 2
        x = sorted(x, reverse=True)
        a = []
        for i in range(2):
            y = []
            j = 0
            while sum(y) != s:
                if (sum(y) + x[j]) <= s:
                    y.append(x[j])
                    del(x[j])
                else:
                    j += 1
                if j > len(x):
                    return '-1'
            a.append(y)
        return a
    else:
        return '-1'


with open('input.txt') as inp:
    ln = inp.readlines()
arr = list(map(int, ln[1].split()))
answ = find_a_middle(arr)
print(answ)
with open('output.txt', 'wt') as outp:
    if answ == '-1':
        outp.write("-1")
        exit
    outp.write(str(len(answ[0])) + "\n")
    out = ''
    for i in range(len(answ[0])):
        out += str(answ[0][i]) + " "
    outp.write(out)

print("Время работы: %s секунд " % (time.perf_counter() - t_start))
mc, mp = tracemalloc.get_traced_memory()
print("Memory: current %f KiB, peak %f KiB" % (mc / 1024, mp / 1024))