from sigonAgent import AgentDefinition
from sensors.DefaultSensor import DefaultSensor
from sensors.ContractSensor import ContractSensor
import torch
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import pickle
from nn_ctx import NNCtx
from negotiation_ctx import NegotiationCtx
import json

aux = {'python_yn': 0,
       'spark': 1,
       'aws': 1,
       'excel': 0,
       'job_simp': 'data scientist',
       'seniority': 'na',
       'teste': 2
       }

NNCtx.ctx_name = '_nn'

NegotiationCtx.ctx_name = '_negotiation'

ctxs = []
ctxs.append(NNCtx)
ctxs.append(NegotiationCtx)

read_sensor = ContractSensor('contractSensor')


agent = AgentDefinition('sigon/aat_agent_nn.on', ctxs, [read_sensor])
agent.run()

read_sensor.perceive(json.dumps(aux))
