import numpy as np

def bisect(f,a,b,tol):
    while (b-a)/2>tol:
        m=(a+b)/2
        if f(a)*f(m)<0: b=m
        else: a=m
    return (a+b)/2

f=lambda x:x*x-2
for tol in [1e-3,1e-6,1e-9]: print(tol,bisect(f,1,2,tol))
A=np.array([[2.,1.],[1.,3.]])
print('eig=',np.linalg.eigvalsh(A))
