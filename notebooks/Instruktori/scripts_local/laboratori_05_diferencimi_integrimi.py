import numpy as np

def simpson(f,a,b,n):
    if n%2: raise ValueError('n çift')
    x=np.linspace(a,b,n+1); y=f(x); h=(b-a)/n
    return h/3*(y[0]+y[-1]+4*y[1:-1:2].sum()+2*y[2:-1:2].sum())
for n in [4,8,16,32]: print(n,simpson(np.sin,0,np.pi,n))
