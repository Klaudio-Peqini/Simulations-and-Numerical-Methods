import numpy as np
rng=np.random.default_rng(2026)
x=np.zeros(50000); acc=0
for n in range(1,len(x)):
 p=x[n-1]+rng.normal(); la=min(0.,-.5*p*p+.5*x[n-1]**2)
 if np.log(rng.random())<la: x[n]=p; acc+=1
 else: x[n]=x[n-1]
print('accept=',acc/(len(x)-1),'mean=',x[5000:].mean(),'std=',x[5000:].std())
