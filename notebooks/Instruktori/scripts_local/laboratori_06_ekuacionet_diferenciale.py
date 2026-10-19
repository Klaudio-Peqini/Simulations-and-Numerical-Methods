import numpy as np

def euler(lam,T,h):
    N=int(np.ceil(T/h)); h=T/N; y=1.0
    for _ in range(N): y+=h*lam*y
    return y
for h in [0.2,0.1,0.05]: print(h,euler(-2,3,h),np.exp(-6))
