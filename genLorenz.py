import math

def dLorenz(x,a,b,c,dt):
    return [x[0]+a*(x[1]-x[0])*dt,
            x[1]+(x[0]*(b-x[2])-x[1])*dt,
            x[2]+(x[0]*x[1]-c*x[2])*dt
            ]

def Lorenz(x0,T,a=10,b=28,c=2.66,dt=0.01):
    xs=[x0]
    x=x0
    for t in range(T):
        x=dLorenz(x,a,b,c,dt)
        xs.append(x);
    return xs


def sigmoid(x):
  return 1 / (1 + math.exp(-x))

if __name__ == '__main__':
    import numpy as np 
    from scipy.stats import bernoulli
    obsnum=20

    x0=[0.2,0.2,0.1]
    out=Lorenz(x0,10000)
    out=np.array(out)
    print out.shape
    out=out[::10,:]
#    out=out[::10,:]

    obs=[]
    for on in out:    
        obs.append([bernoulli.rvs(sigmoid(on[0])) for j in xrange(obsnum)])
    obs=np.array(obs)
    np.savetxt("data.csv",obs,delimiter=",")    

