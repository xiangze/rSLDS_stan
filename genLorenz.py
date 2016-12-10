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

if __name__ == '__main__':
    import numpy as np 
    x0=[0.2,0.2,0.1]
    out=Lorenz(x0,10000)
    out=np.array(out).T
    np.savetxt("data.csv",out.T,delimiter=",")    

