import pystan
import numpy as np

isvb=True
isinit=True
print(pystan.__version__)
smodel=pystan.StanModel(file="RSLDS.stan")

oN=500
oT=10
y=np.loadtxt("data.csv",delimiter=",")
N=min(y.shape[0],oN)
T=min(y.shape[1],oT)
y=y[:N,:T]
M=3
K=2


data={"T":T,"N":N,"M":M,"K":K,"y":y}

if(isinit):
    xs=np.loadtxt("data_source.csv",delimiter=",")
    xs=xs[:N,:M]
    def initf():
        return dict(x=xs,
                    A=np.random.normal(size=(K,M,M)),
                    C=np.random.normal(size=K),
                    R=np.random.normal(size=(K,M)),
                    b=np.random.normal(size=(K,M)),
                    r=np.random.normal(size=K),
                    d=np.random.normal(size=K),
                    s=1,
                    corr_ch=np.random.uniform(-1,1,size=(M,M)),
                    sv=np.repeat(1.,M)
                )
else:
    initf="random"
        
if(isvb):
    fit= smodel.vb(data=data,init=initf,seed=71)
else:
    fit= smodel.sampling(data,init=initf,iter=31000, warmup=1000,
                         thin=10, chains=3, seed=71)

res=fit.extract()
print res   

import draws
draws.drawline()
