import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import math


# H0: using nn does not affect reasoning time

# HA:using nn increase the reasoning time

df = pd.read_csv("sigon/experiment3_agents/funcoes_util.csv", sep=';')

df[['max.util.']].describe()

result = 1.0 # atingido pelo AAT + NN
counter = 0 #

for util in df['max.util.']:
    util_value = util.replace(',', '.')   
    
    if float(result) > float(util_value):
        counter += 1


print(counter) # 121 - mair ou igual; 41 - maior
