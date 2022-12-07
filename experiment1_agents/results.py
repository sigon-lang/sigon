import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt


# H0: using nn does not affect reasoning time

# HA:using nn increase the reasoning time

df = pd.read_csv("sigon/experiment1_agents/experiment1_50_transposed.csv")

df[['aat','nn']].describe()


stats.probplot(df['aat'], dist="norm", plot=plt)
plt.title("Agent AAT only")
plt.savefig("Agent_AAT_only.png")

stats.probplot(df['nn'], dist="norm", plot=plt)
plt.title("Agent AAT with NN")
plt.savefig("Agent_AAT_with_NN.png")


print(stats.shapiro(df['aat']))


print(stats.shapiro(df['nn']))



print(stats.wilcoxon(df['aat'], df['nn']))


# ShapiroResult(statistic=0.9339360594749451, pvalue=0.007810808252543211)
# ShapiroResult(statistic=0.9563485383987427, pvalue=0.06252649426460266)
# WilcoxonResult(statistic=11.0, pvalue=1.4685612927356851e-09)
# https://www.statology.org/wilcoxon-signed-rank-test-python/


print(stats.ttest_rel(df['aat'], df['nn']))
# Ttest_relResult(statistic=-13.219428084589529, pvalue=8.838829037355637e-18)




