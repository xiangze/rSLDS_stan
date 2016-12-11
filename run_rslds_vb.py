import pystan
import numpy as np

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
fit= smodel.vb(data=data,seed=71)
res=fit.extract()
print res   

import draws
draws.drawline()

