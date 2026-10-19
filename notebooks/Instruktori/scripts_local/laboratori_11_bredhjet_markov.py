import numpy as np
rng=np.random.default_rng(2026)
for N in [100,1000,10000]:
 M=5000; X=np.where(rng.random((M,N))<.5,-1,1).sum(axis=1)
 print(N,X.mean(),np.mean(X*X))
