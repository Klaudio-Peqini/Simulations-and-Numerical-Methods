import numpy as np
L=c=1.; Nx=201; dx=L/(Nx-1); r=.9; dt=r*dx/c; T=1.; Nt=int(np.ceil(T/dt)); dt=T/Nt; r=c*dt/dx
x=np.linspace(0,L,Nx); um=np.exp(-.5*((x-.35)/.06)**2); um[[0,-1]]=0
u=um.copy(); u[1:-1]=um[1:-1]+.5*r*r*(um[2:]-2*um[1:-1]+um[:-2])
for _ in range(1,Nt):
 up=np.zeros_like(u); up[1:-1]=2*u[1:-1]-um[1:-1]+r*r*(u[2:]-2*u[1:-1]+u[:-2]); um,u=u,up
print('r=',r,'max|u|=',np.max(np.abs(u)))
