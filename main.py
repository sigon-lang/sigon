from sigonAgent import AgentDefinition
from sensors.DefaultSensor import DefaultSensor
import torch
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import pickle
from aat_ctx import AATCtx

aux = {'python_yn': 0,
       'spark': 1,
       'aws': 1,
       'excel': 0,
       'job_simp': 'data scientist',
       'seniority': 'na',
       'teste': 2
       }

AATCtx.ctx_name = 'AAT'
AATCtx.append_fact(aux)

agent = AgentDefinition('sigon/example.on')
agent.run()

read_sensor = DefaultSensor('defaultSensor')
read_sensor.perceive("start")
