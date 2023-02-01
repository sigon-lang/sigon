import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt


# H0: using nn does not affect reasoning time

# HA:using nn increase the reasoning time

df = pd.read_csv("sigon/experiment1_agents_v2/experiment1_50_transposed_v2.csv")

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




# ShapiroResult(statistic=0.3511784076690674, pvalue=1.553141567179478e-13)
# ShapiroResult(statistic=0.22776424884796143, pvalue=9.219696132847094e-15)
# WilcoxonResult(statistic=97.0, pvalue=1.8125918393095056e-07)



print(stats.ttest_rel(df['aat'], df['nn']))
# Ttest_relResult(statistic=2.8539500112362193, pvalue=0.006310850857993183)




