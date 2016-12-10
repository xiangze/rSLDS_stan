import pystan
import numpy as np

pystan.StanModel(file="RSLDS.stan")

y=np.loadtxt("data.csv",delimiter=",")
N=y.shape[0]
M=y.shape[1]
K=2

data={"N":N,"M":M,"K":K,"y":d}

fit= smodel.sampling(data, iter=31000, warmup=1000, thin=10, chains=3, seed=71)
res=fit.extract()
   

