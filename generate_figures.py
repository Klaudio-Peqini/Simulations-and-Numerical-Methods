from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT = Path(__file__).resolve().parent / "figures"
OUT.mkdir(parents=True, exist_ok=True)
BLUE, RED, GREEN, GOLD, GRAY = "#17365D", "#C0504D", "#3C8D40", "#D9A441", "#666666"
plt.rcParams.update({"font.family": "DejaVu Serif", "font.size": 10, "axes.titlesize": 11,
                     "axes.labelsize": 10, "legend.fontsize": 8, "figure.dpi": 130})

def save(fig, name):
    fig.tight_layout()
    fig.savefig(OUT / name, dpi=220, bbox_inches="tight", facecolor="white")
    plt.close(fig)

def workflow():
    fig, ax = plt.subplots(figsize=(9, 3)); ax.axis("off")
    labels = ["Pyetja\nfizike", "Modeli\nmatematik", "Algoritmi\nnumerik", "Kodi dhe\neksperimenti", "Interpretimi\nfizik"]
    xs = np.linspace(.08, .92, 5)
    for i,(x,s) in enumerate(zip(xs,labels)):
        ax.add_patch(FancyBboxPatch((x-.075,.43),.15,.24,boxstyle="round,pad=.02",fc=BLUE,ec=BLUE))
        ax.text(x,.55,s,ha="center",va="center",color="white",weight="bold")
        if i<4: ax.annotate("",(xs[i+1]-.085,.55),(x+.085,.55),arrowprops=dict(arrowstyle="->",lw=2,color="#4F81BD"))
    ax.annotate("verifikim, vleftësim dhe rishikim",(.1,.32),(.9,.32),ha="center",
                arrowprops=dict(arrowstyle="->",lw=1.5,color=RED),color=RED)
    save(fig,"01_cikli_simulimit.pdf")

def floating_point():
    x=np.logspace(-18,-1,300); exact=np.ones_like(x); calc=((1+x)-1)/x
    fig,ax=plt.subplots(figsize=(6.5,3.5)); ax.semilogx(x,np.abs(calc-exact),color=BLUE,lw=2)
    ax.set(xlabel=r"$x$",ylabel="gabimi absolut",title=r"Anulimi katastrofik në $((1+x)-1)/x$"); ax.grid(alpha=.25)
    save(fig,"02_anulimi_katastrofik.pdf")

def root_methods():
    f=lambda x: np.cos(x)-x; root=0.7390851332
    a,b=0.,1.; eb=[]
    for _ in range(25):
        c=(a+b)/2; eb.append(abs(c-root));
        if f(a)*f(c)<=0:b=c
        else:a=c
    x=.5; en=[]
    for _ in range(8):
        x=x-(np.cos(x)-x)/(-np.sin(x)-1); en.append(abs(x-root))
    fig,ax=plt.subplots(figsize=(6.5,3.5)); ax.semilogy(range(1,len(eb)+1),eb,"o-",ms=3,label="përgjysmimi",color=BLUE)
    ax.semilogy(range(1,len(en)+1),en,"s-",ms=4,label="Njutoni",color=RED); ax.set(xlabel="iteracioni",ylabel="gabimi absolut")
    ax.grid(alpha=.25); ax.legend(frameon=False); save(fig,"03_konvergjenca_rrenjeve.pdf")

def conditioning():
    eps=np.logspace(-8,-1,100); kapp=[]
    for e in eps: kapp.append(np.linalg.cond(np.array([[1,1],[1,1+e]])))
    fig,ax=plt.subplots(figsize=(6.5,3.5)); ax.loglog(eps,kapp,color=BLUE,lw=2); ax.loglog(eps,4/eps,"--",color=RED,label=r"$4/\varepsilon$")
    ax.set(xlabel=r"$\varepsilon$",ylabel=r"$\kappa_2(A)$",title="Kushtëzimi i një sistemi pothuaj singular"); ax.grid(alpha=.25); ax.legend(frameon=False)
    save(fig,"04_kushtzimi_matrices.pdf")

def eigenmodes():
    x=np.linspace(0,1,300); fig,axs=plt.subplots(3,1,figsize=(6.5,5),sharex=True)
    for n,ax in enumerate(axs,1): ax.plot(x,np.sin(n*np.pi*x),color=BLUE,lw=2); ax.axhline(0,color=GRAY,lw=.6); ax.set_ylabel(fr"$u_{n}(x)$"); ax.grid(alpha=.15)
    axs[-1].set_xlabel("pozicioni i normalizuar"); fig.suptitle("Tri modet e para normale"); save(fig,"05_modet_normale.pdf")

def interpolation():
    f=lambda x:1/(1+25*x*x); xx=np.linspace(-1,1,1200); n=11
    def lag(xn,yn,x):
        y=np.zeros_like(x)
        for i in range(len(xn)):
            li=np.ones_like(x)
            for j in range(len(xn)):
                if i!=j:li*= (x-xn[j])/(xn[i]-xn[j])
            y+=yn[i]*li
        return y
    xe=np.linspace(-1,1,n); xc=np.cos((2*np.arange(n)+1)*np.pi/(2*n))[::-1]
    fig,axs=plt.subplots(1,2,figsize=(9,3.4),sharey=True)
    for ax,xn,title in [(axs[0],xe,"nyje të baraslarguara"),(axs[1],xc,"nyje të Çebishevit")]:
        ax.plot(xx,f(xx),color=BLUE,lw=2,label="funksioni"); ax.plot(xx,lag(xn,f(xn),xx),color=RED,lw=1.5,label="Lagranzhi"); ax.scatter(xn,f(xn),s=15,color=GOLD,zorder=3); ax.set_title(title); ax.grid(alpha=.2)
    axs[0].legend(frameon=False); save(fig,"06_interpolimi_runge.pdf")

def kepler_regression():
    rng=np.random.default_rng(7); a=np.array([.39,.72,1,1.52,5.2,9.54]); T=a**1.5*np.exp(rng.normal(0,.025,len(a)))
    lx,ly=np.log(a),np.log(T); m,c=np.polyfit(lx,ly,1); xx=np.linspace(lx.min()-.1,lx.max()+.1,100)
    fig,ax=plt.subplots(figsize=(6.5,3.7)); ax.scatter(lx,ly,s=42,color=RED,label="të dhënat"); ax.plot(xx,m*xx+c,color=BLUE,lw=2,label=fr"pjerrësia $={m:.3f}$")
    ax.set(xlabel=r"$\ln a$",ylabel=r"$\ln T$",title="Ligji i tretë i Keplerit si regres linear"); ax.grid(alpha=.25); ax.legend(frameon=False)
    save(fig,"07_regresioni_kepler.pdf")

def differentiation():
    hs=np.logspace(-16,-1,200); x=1.; exact=np.cos(x)
    forward=np.abs((np.sin(x+hs)-np.sin(x))/hs-exact); central=np.abs((np.sin(x+hs)-np.sin(x-hs))/(2*hs)-exact)
    fig,ax=plt.subplots(figsize=(6.5,3.7)); ax.loglog(hs,forward,color=RED,label="përpara"); ax.loglog(hs,central,color=BLUE,label="qendrore")
    ax.set(xlabel="hapi h",ylabel="gabimi absolut",title="Kompromisi këputje–rrumbullakim"); ax.grid(alpha=.25); ax.legend(frameon=False)
    save(fig,"08_gabimi_derivimit.pdf")

def quadrature():
    Ns=2**np.arange(1,10); exact=2.; et=[]; es=[]
    for n in Ns:
        x=np.linspace(0,np.pi,n+1); y=np.sin(x); et.append(abs(np.trapz(y,x)-exact))
        if n%2: es.append(np.nan)
        else: es.append(abs((x[1]-x[0])/3*(y[0]+y[-1]+4*y[1:-1:2].sum()+2*y[2:-2:2].sum())-exact))
    fig,ax=plt.subplots(figsize=(6.5,3.7)); ax.loglog(Ns,et,"o-",color=BLUE,label="trapezi"); ax.loglog(Ns,es,"s-",color=RED,label="Simpsoni")
    ax.set(xlabel="numri i nënintervaleve",ylabel="gabimi absolut",title=r"Integrimi i $\sin x$ në $[0,\pi]$"); ax.grid(alpha=.25); ax.legend(frameon=False)
    save(fig,"09_kuadratura_konvergjenca.pdf")

def ode_pendulum():
    def sim(dt,method):
        t=np.arange(0,30+dt,dt); th=np.zeros_like(t); om=np.zeros_like(t); th[0]=1.2
        for i in range(len(t)-1):
            if method=="Euler": th[i+1]=th[i]+dt*om[i]; om[i+1]=om[i]-dt*np.sin(th[i])
            else:
                omh=om[i]-.5*dt*np.sin(th[i]); th[i+1]=th[i]+dt*omh; om[i+1]=omh-.5*dt*np.sin(th[i+1])
        return t,.5*om**2+1-np.cos(th)
    fig,ax=plt.subplots(figsize=(6.5,3.7))
    for meth,col in [("Euler",RED),("Verlet",BLUE)]:
        t,E=sim(.05,meth); ax.plot(t,(E-E[0])/E[0],color=col,label=meth)
    ax.set(xlabel="koha",ylabel="gabimi relativ i energjisë",title="Lavjerrësi jolinear"); ax.grid(alpha=.25); ax.legend(frameon=False)
    save(fig,"10_energjia_lavjerresit.pdf")

def two_body():
    dt=.001; n=8000; r=np.zeros((n,2)); v=np.zeros((n,2)); r[0]=[1,0]; v[0]=[0,.82]
    a=lambda q:-q/np.linalg.norm(q)**3
    for i in range(n-1):
        vh=v[i]+.5*dt*a(r[i]); r[i+1]=r[i]+dt*vh; v[i+1]=vh+.5*dt*a(r[i+1])
    fig,ax=plt.subplots(figsize=(5,5)); ax.plot(r[:,0],r[:,1],color=BLUE,lw=1.5); ax.scatter([0],[0],s=90,color=GOLD,label="trupi qendror")
    ax.set_aspect("equal"); ax.set(xlabel="x",ylabel="y",title="Orbitë numerike me skemën Verlet"); ax.grid(alpha=.2); ax.legend(frameon=False)
    save(fig,"11_orbita_dy_trupave.pdf")

def wave():
    x=np.linspace(0,1,301); times=[0,.12,.24,.36]; fig,ax=plt.subplots(figsize=(7,3.8))
    for t,c in zip(times,[BLUE,RED,GREEN,GOLD]):
        u=np.exp(-((x-.25-t)/.06)**2)-np.exp(-((x-.25+t)/.06)**2)*0
        # fixed-boundary reflection by odd images
        u-=np.exp(-((x-(1.75-t))/.06)**2)
        ax.plot(x,u,label=fr"$t={t:.2f}$",color=c)
    ax.set(xlabel="x",ylabel="u(x,t)",title="Puls bredhës dhe reflektim"); ax.grid(alpha=.2)
    ax.legend(ncol=2, loc="upper right", frameon=True, framealpha=.92,
              edgecolor="#B8B8B8", columnspacing=1.2, handlelength=2.2)
    save(fig,"12_vala_bredhese.pdf")

def dispersion():
    q=np.linspace(.001,np.pi,400); ratio=2*np.sin(q/2)/q
    fig,ax=plt.subplots(figsize=(6.5,3.5)); ax.plot(q/np.pi,ratio,color=BLUE,lw=2); ax.axhline(1,color=GRAY,ls="--")
    ax.set(xlabel=r"$k\Delta x/\pi$",ylabel=r"$\omega_{num}/(ck)$",title="Dispersimi numerik i skemës së valës"); ax.grid(alpha=.25)
    save(fig,"13_dispersimi_numerik.pdf")

def probability():
    from math import factorial
    k=np.arange(0,21); p=np.array([factorial(20)/(factorial(int(i))*factorial(20-int(i)))*.5**20 for i in k])
    fig,ax=plt.subplots(figsize=(6.5,3.5)); ax.bar(k,p,color="#6F91B8",edgecolor=BLUE); ax.set(xlabel="numri i stemave",ylabel="probabiliteti",title="Shpërndarja binomiale për 20 hedhje")
    save(fig,"14_shperndarja_binomiale.pdf")

def clt():
    rng=np.random.default_rng(12); fig,axs=plt.subplots(1,3,figsize=(9,3),sharey=True)
    for ax,n in zip(axs,[1,5,30]):
        z=rng.uniform(-1,1,(40000,n)).mean(axis=1); ax.hist(z,bins=55,density=True,color="#D9EAF7",edgecolor=BLUE); ax.set_title(fr"$n={n}$"); ax.set_xlabel("mesatarja")
    axs[0].set_ylabel("dendësia"); fig.suptitle("Teorema qendrore kufitare"); save(fig,"15_teorema_qendrore.pdf")

def prng():
    def lcg(a,c,m,x0,n):
        x=np.empty(n,dtype=np.int64); x[0]=x0
        for i in range(n-1):x[i+1]=(a*x[i]+c)%m
        return x/m
    bad=lcg(17,43,256,5,500); good=np.random.default_rng(3).random(500)
    fig,axs=plt.subplots(1,2,figsize=(8,3.5))
    for ax,u,title in [(axs[0],bad,"LCG me modul të vogël"),(axs[1],good,"gjenerator modern")]: ax.scatter(u[:-1],u[1:],s=8,alpha=.65,color=BLUE); ax.set(xlabel=r"$u_n$",ylabel=r"$u_{n+1}$",title=title)
    save(fig,"16_testi_cifteve_prng.pdf")

def sampling():
    rng=np.random.default_rng(5); u=rng.random(20000); x=-np.log(1-u)/1.5; xx=np.linspace(0,5,300)
    fig,ax=plt.subplots(figsize=(6.5,3.5)); ax.hist(x,bins=70,density=True,color="#D9EAF7",edgecolor="none",label="mostrat"); ax.plot(xx,1.5*np.exp(-1.5*xx),color=RED,lw=2,label="dendësia teorike")
    ax.set(xlabel="x",ylabel="dendësia",title="Kampionimi me transformimin e anasjelltë"); ax.legend(frameon=False); save(fig,"17_kampionimi_eksponencial.pdf")

def monte_carlo():
    rng=np.random.default_rng(9); N=50000; xy=rng.random((N,2)); inside=(xy[:,0]**2+xy[:,1]**2)<=1; est=4*np.cumsum(inside)/np.arange(1,N+1)
    fig,axs=plt.subplots(1,2,figsize=(9,3.6))
    axs[0].scatter(xy[:1800,0],xy[:1800,1],s=4,c=np.where(inside[:1800],BLUE,RED),alpha=.55); q=np.linspace(0,1,200); axs[0].plot(q,np.sqrt(1-q*q),color="black"); axs[0].set_aspect("equal"); axs[0].set_title("vlerësimi gjeometrik i π")
    n=np.arange(1,N+1); axs[1].semilogx(n,est,color=BLUE,lw=1); axs[1].axhline(np.pi,color=RED,ls="--",label="π"); axs[1].set(xlabel="N",ylabel=r"$\hat\pi_N$"); axs[1].legend(frameon=False); axs[1].grid(alpha=.2)
    save(fig,"18_monte_carlo_pi.pdf")

def mc_error():
    rng=np.random.default_rng(11); Ns=2**np.arange(4,17); rms=[]
    exact=(np.e-1)**4
    for n in Ns:
        vals=[]
        for _ in range(80):
            x=rng.random((n,4)); vals.append(np.mean(np.exp(x.sum(axis=1))))
        rms.append(np.sqrt(np.mean((np.array(vals)-exact)**2)))
    fig,ax=plt.subplots(figsize=(6.5,3.6)); ax.loglog(Ns,rms,"o-",color=BLUE,label="RMS empirike"); ax.loglog(Ns,rms[0]*np.sqrt(Ns[0]/Ns),"--",color=RED,label=r"$N^{-1/2}$")
    ax.set(xlabel="N",ylabel="gabimi RMS",title="Konvergjenca Monte Carlo në katër përmasa"); ax.grid(alpha=.2); ax.legend(frameon=False)
    save(fig,"19_gabimi_monte_carlo.pdf")

def spacecraft():
    rng=np.random.default_rng(21); n=1200; t=np.linspace(0,90,500); g=1.62
    h0=rng.normal(1500,40,n); v0=rng.normal(-15,1.2,n); thrust=rng.normal(1.48,0.05,n)
    land=[]
    for H,V,A in zip(h0,v0,thrust):
        h=H+V*t+.5*(A-g)*t*t; hit=np.where(h<=0)[0];
        if len(hit): land.append(V+(A-g)*t[hit[0]])
    fig,ax=plt.subplots(figsize=(6.5,3.5)); ax.hist(land,bins=50,color="#D9EAF7",edgecolor=BLUE); ax.axvline(-2,color=RED,ls="--",label="kufi i sigurisë")
    ax.set(xlabel="shpejtësia në ulje",ylabel="numri i realizimeve",title="Zbritja e mjetit hapësinor me hyrje të pacaktuara"); ax.legend(frameon=False)
    save(fig,"20_zbritja_mjetit_monte_carlo.pdf")

def random_walk():
    rng=np.random.default_rng(4); fig,axs=plt.subplots(1,2,figsize=(9,3.8))
    for _ in range(20):
        s=rng.choice([-1,1],500); axs[0].plot(np.r_[0,np.cumsum(s)],alpha=.45,lw=.8)
    Ns=np.unique(np.logspace(1,4,35).astype(int)); msd=[]
    for n in Ns:
        s=rng.choice([-1,1],(3000,n)); msd.append(np.mean(np.sum(s,axis=1)**2))
    axs[0].set(xlabel="hapi",ylabel="pozicioni",title="realizime të bredhjes 1D"); axs[0].grid(alpha=.15)
    axs[1].loglog(Ns,msd,"o",ms=3,color=BLUE,label="simulimi"); axs[1].loglog(Ns,Ns,color=RED,label=r"$\langle x^2\rangle=N$"); axs[1].set(xlabel="N",ylabel=r"$\langle x^2\rangle$"); axs[1].legend(frameon=False); axs[1].grid(alpha=.2)
    save(fig,"21_bredhja_e_rastit.pdf")

def diffusion():
    x=np.linspace(-6,6,500); fig,ax=plt.subplots(figsize=(6.5,3.5))
    for t,c in zip([.2,.5,1,2],[GOLD,RED,GREEN,BLUE]): ax.plot(x,np.exp(-x*x/(4*t))/np.sqrt(4*np.pi*t),color=c,label=f"t={t}")
    ax.set(xlabel="x",ylabel="p(x,t)",title="Zgjidhja themelore e ekuacionit të difuzionit"); ax.legend(frameon=False); ax.grid(alpha=.2)
    save(fig,"22_difuzioni_gaussian.pdf")

def markov():
    P=np.array([[.9,.1],[.25,.75]]); p=np.array([1.,0.]); hist=[p.copy()]
    for _ in range(30): p=p@P; hist.append(p.copy())
    h=np.array(hist); pi=np.array([.25/(.25+.1),.1/(.25+.1)])
    fig,ax=plt.subplots(figsize=(6.5,3.5)); ax.plot(h[:,0],color=BLUE,lw=2,label="gjendja 0"); ax.plot(h[:,1],color=RED,lw=2,label="gjendja 1"); ax.axhline(pi[0],color=BLUE,ls="--",alpha=.5); ax.axhline(pi[1],color=RED,ls="--",alpha=.5)
    ax.set(xlabel="hapi",ylabel="probabiliteti",title="Përafrimi te shpërndarja stacionare"); ax.legend(frameon=False); ax.grid(alpha=.2)
    save(fig,"23_zinxhiri_markov.pdf")

def ising():
    rng=np.random.default_rng(2)
    def run(T,L=48,sweeps=700):
        s=rng.choice([-1,1],(L,L))
        for _ in range(sweeps*L*L):
            i,j=rng.integers(0,L,2); dE=2*s[i,j]*(s[(i+1)%L,j]+s[(i-1)%L,j]+s[i,(j+1)%L]+s[i,(j-1)%L])
            if dE<=0 or rng.random()<np.exp(-dE/T):s[i,j]*=-1
        return s
    low,high=run(1.6),run(3.4)
    fig,axs=plt.subplots(1,2,figsize=(7,3.5))
    for ax,s,T in [(axs[0],low,1.6),(axs[1],high,3.4)]: ax.imshow(s,cmap="coolwarm",vmin=-1,vmax=1,interpolation="nearest"); ax.set_title(fr"$T={T}$"); ax.axis("off")
    fig.suptitle("Konfigurime të modelit Ising 2D"); save(fig,"24_ising_konfigurime.pdf")
    Ts=np.linspace(1.4,3.5,24); mags=[]
    for T in Ts: mags.append(abs(run(T,L=24,sweeps=300).mean()))
    fig,ax=plt.subplots(figsize=(6.5,3.5)); ax.plot(Ts,mags,"o-",color=BLUE); ax.axvline(2.269,color=RED,ls="--",label=r"$T_c\approx2.269$"); ax.set(xlabel="temperatura T",ylabel=r"$|m|$",title="Magnetizimi në modelin Ising"); ax.grid(alpha=.2); ax.legend(frameon=False)
    save(fig,"25_ising_magnetizimi.pdf")

for fn in [workflow,floating_point,root_methods,conditioning,eigenmodes,interpolation,kepler_regression,differentiation,quadrature,ode_pendulum,two_body,wave,dispersion,probability,clt,prng,sampling,monte_carlo,mc_error,spacecraft,random_walk,diffusion,markov,ising]:
    fn()
print(f"U krijuan figurat në {OUT}")
