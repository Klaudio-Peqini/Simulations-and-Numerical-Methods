import numpy as np
rng=np.random.default_rng(2026)
for N in [1000,10000,100000]:
 u=rng.random(N); y=u*u
 print(N,y.mean(),y.std(ddof=1)/np.sqrt(N))
