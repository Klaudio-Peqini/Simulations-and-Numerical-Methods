import numpy as np
rng=np.random.default_rng(2026)
for N in [1000,10000,100000]:
 u=rng.random(N); x=-np.log1p(-u)/2
 print(N,x.mean(),x.var())
