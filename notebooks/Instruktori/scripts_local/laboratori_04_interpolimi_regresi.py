import numpy as np
x=np.linspace(0,10,40); rng=np.random.default_rng(2026)
y=2+0.7*x+rng.normal(0,0.8,x.size)
X=np.c_[np.ones_like(x),x]
b=np.linalg.lstsq(X,y,rcond=None)[0]
print('beta=',b,'RMSE=',np.sqrt(np.mean((y-X@b)**2)))
