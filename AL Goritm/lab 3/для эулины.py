import tracemalloc
import time

t_start = time.perf_counter()
tracemalloc.start()

print("Время работы (в секундах):", time.perf_counter() - t_start)
print("Память %d, и пик %d" % tracemalloc.get_traced_memory())