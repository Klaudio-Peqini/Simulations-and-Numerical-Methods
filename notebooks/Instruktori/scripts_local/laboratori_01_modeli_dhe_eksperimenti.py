import numpy as np

def euler(m,c,g,v0,T,h):
    N=int(np.ceil(T/h)); h=T/N
    t=np.linspace(0,T,N+1); v=np.empty(N+1); v[0]=v0
    for n in range(N): v[n+1]=v[n]+h*(g-(c/m)*v[n])
    return t,v

m,c,g,v0,T=1.0,0.5,9.81,0.0,8.0
for h in [0.2,0.1,0.05]:
    t,v=euler(m,c,g,v0,T,h)
    ref=m*g/c+(v0-m*g/c)*np.exp(-t/(m/c))
    print(h,np.max(np.abs(v-ref)))
