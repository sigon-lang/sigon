from sigonAgent import AgentDefinition
from sensors.DefaultSensor import DefaultSensor
import torch
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# Load model
model = torch.jit.load('sigon/regressorv1-f.pt')
model.eval()


df = pd.read_csv('sigon/eda_data.csv')

# choose relevant columns
df.columns

df_model = df[['avg_salary', 'Rating', 'Size', 'Type of ownership', 'Industry', 'Sector', 'Revenue', 'num_comp', 'hourly', 'employer_provided',
               'job_state', 'same_state', 'age', 'python_yn', 'spark', 'aws', 'excel', 'job_simp', 'seniority', 'desc_len']]


# get dummy data

example = dict(df_model.iloc[1])

print(example)

aux = {'python_yn': 0,
       'spark': 1,
       'aws': 1,
       'excel': 0,
       'job_simp': 'data scientist',
       'seniority': 'na',
       'teste': 2
    }


print(example)

keys_to_remove = []
for key in aux.keys():
    if key not in example:
        keys_to_remove.append(key)

for key in keys_to_remove:
    del aux[key]
    
example.update(aux)

df_dum = pd.get_dummies(df_model)
X = df_dum.drop('avg_salary', axis=1)

X_test_torch = torch.tensor(np.array(X), dtype=torch.float)

print(model.forward(X_test_torch))


agent = AgentDefinition('example.on')
agent.run()

read_sensor = DefaultSensor('defaultSensor')
read_sensor.perceive("start")
