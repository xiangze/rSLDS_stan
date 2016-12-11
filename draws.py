from scipy.stats.mstats import mquantiles

def drawline(res,name,fname="fig.png",start=0):
    _val=zip(*res[name])[start:-1]
    _range=zip(*[ mquantiles(i) for i in _val])
    fig, a = plt.subplots(1,sharex=True)
    a.fill_between(range(len(_range[0])),_range[0],_range[2], color='blue',alpha=0.5)
    a.plot(_range[1], lw=2, color='black')
    a.plot([0]*len(_val))
    plt.title(name)
    plt.savefig(fname)

