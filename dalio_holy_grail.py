
"""
This code uses the multivariate_normal numpy function to simulate the
performance of hypothetical portfolios based on a given number of assets
with given levels of correlations.
"""

import matplotlib.pyplot as plt
import numpy as np


asset_counts = list(range(1, 20))
line_styles = ["solid", "dotted", "dashed",  "dashdot"] 
correlations = [0, 0.2, 0.4, 0.6 ]
returns = 10
stdev = 10
variance = stdev ** 2

for correlation, style in zip(correlations, line_styles):
    stdevs = []
    for asset_count in asset_counts :

        covariance = stdev * stdev * correlation
        mean = [returns] * asset_count 
        cov = [ [covariance for _ in range(asset_count)] for _ in range(asset_count)]
        for i in range(asset_count):
            cov[i][i] = variance
        matr = np.random.default_rng().multivariate_normal(mean, cov, 100000).T
        row_means = matr.mean(axis=0)
        stdevs.append(row_means.std())
        

    plt.plot(asset_counts , stdevs, linestyle=style, label=str(correlation) + " correlation" )

plt.legend()
plt.title("The Holy Grail")
plt.ylabel("Std. Deviation")
plt.xlabel("# of Assets")
plt.xticks(list(range(21)))
plt.grid()
plt.ylim([0, 10])
plt.show()
