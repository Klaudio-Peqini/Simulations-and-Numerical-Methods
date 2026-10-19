import numpy as np
from time import perf_counter

def horner(a, x):
    y = 0.0
    for ak in reversed(a):
        y = y*x + ak
    return y

for n in [10, 100, 1000, 10000]:
    a = np.ones(n + 1)
    t0 = perf_counter()
    y = horner(a, 0.99)
    dt = perf_counter() - t0
    print(f"n={n:5d}, p(0.99)={y:.8g}, koha={dt:.3e} s")
