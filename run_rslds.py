import pystan
import numpy as np

pystan.StanModel(file="RSLDS.stan")

y=np.loadtxt("data.csv",delimiter=",")
N=y.shape[0]
T=y.shape[1]
M=3
K=2

data={"T":T,"N":N,"M":M,"K":K,"y":y}
fit= smodel.sampling(data, iter=31000, warmup=1000, thin=10, chains=3, seed=71)
res=fit.extract()
print res   

