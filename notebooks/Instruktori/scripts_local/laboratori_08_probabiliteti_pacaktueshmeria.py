import numpy as np
rng=np.random.default_rng(2026)
for N in [100,1000,10000,100000]:
 x=rng.random(N)<.3
 print(N,x.mean(),np.sqrt(.3*.7/N))
