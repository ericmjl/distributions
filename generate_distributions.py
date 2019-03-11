"""
Generates distribution plots using matplotlib.

"tomato" coloured distributions are for likelihoods/observed data.
"royalblue" coloured distributions are for parameter distributions.
"""
#%%
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats._distn_infrastructure import rv_discrete, rv_continuous
import numpy as np
import os


#%%
distributions = {
    'normal': stats.norm,
    'gamma': stats.gamma,
    't': stats.t,
    'beta': stats.beta,
    'uniform': stats.beta,
    'half_normal': stats.halfnorm,
    'half_cauchy': stats.halfcauchy,
    'exponential': stats.expon,
    'bernoulli': stats.bernoulli,
    'binomial': stats.binom,
    'poisson': stats.poisson,
}

kwargs = {
    'normal': {'loc': 0, 'scale': 1},
    'gamma': {'loc': 0, 'scale': 1, 'a': 1.5},
    't': {'loc': 0, 'scale': 1, 'df': 2},
    'beta': {'a': 3, 'b': 2},
    'uniform': {'a': 1, 'b': 1},  # uniform is a special case of beta distribution
    'half_normal': {'loc': 0, 'scale': 1},
    'half_cauchy': {'loc': 0, 'scale': 1},
    'exponential': {'loc': 0, 'scale': 1},
    'bernoulli': {'p': 0.8},
    'binomial': {'p': 0.4, 'n': 10},
    'poisson': {'mu': 2},
}


supports = {
    'normal': np.linspace(-3, 3, 1000),
    'gamma': np.linspace(0, 5, 1000),
    't': np.linspace(-3, 3, 1000),
    'beta': np.linspace(0, 1, 1000),
    'uniform': np.linspace(0, 1, 1000),
    'half_normal': np.linspace(0, 3, 1000),
    'half_cauchy': np.linspace(0, 3, 1000),
    'exponential': np.linspace(0, 3, 1000),
    'bernoulli': [0, 1],
    'binomial': np.arange(0, 10, 1000),
    'poisson': np.arange(0, 10, 1000),
}


#%%
def despine(ax):
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_xticks([])
    ax.set_xticklabels([])
    ax.set_yticks([])
    ax.set_yticklabels([])

def plot(name):
    os.makedirs(name, exist_ok=True)
    distribution = distributions[name]
    dist_kwargs = kwargs[name]
    support = supports[name]

    dist = distribution(**dist_kwargs)

    def plotdist(color):
        fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(6, 3))
        if isinstance(distribution, rv_discrete):
            ax.bar(support, dist.pmf(support), width=0.8, color=color)
        elif isinstance(distribution, rv_continuous):
            ax.plot(support, dist.pdf(support), color='black')
            ax.fill_between(support, 0, dist.pdf(support), color=color)
        ax.set_title(name, size=20)
        despine(ax)
        plt.savefig(f'{name}/{name}-{color}.pdf')
        plt.savefig(f'{name}/{name}-{color}-xs.png', dpi=50, transparent=True)
        plt.savefig(f'{name}/{name}-{color}-sm.png', dpi=75, transparent=True)
        plt.savefig(f'{name}/{name}-{color}-md.png', dpi=150, transparent=True)
        plt.savefig(f'{name}/{name}-{color}-lg.png', dpi=300, transparent=True)
        plt.close()

    plotdist('salmon')
    plotdist('royalblue')



plot('normal')
plot('gamma')
plot('t')
plot('beta')
plot('uniform')
plot('half_normal')
plot('half_cauchy')
plot('exponential')
plot('bernoulli')
plot('binomial')
plot('poisson')

#%%


#%%
