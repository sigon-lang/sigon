from sigonAgent import AgentDefinition
from sensors.DefaultSensor import DefaultSensor
from sensors.ContractSensor import ContractSensor
from sensors.CVSensor import CVSensor
from nn_ctx import NNCtx
from negotiation_ctx import NegotiationCtx
import json

# from sensor to beliefs
contract = {
       "salary": [7000, 12000, 20000], # Salary: The possible values are (a) \$7,000, (b) \$12,000, or (c) \$20,000;
       "jobDescription": ["QA", "Programmer", "Team Manager", "Project Manager"], # Responsibilities given to the employer. The possible values are (a) QA, (b) Programmer, (c) Team Manager, or (d) Project Manager;
       "carBenefits": ["yes", "no", "no agreement"], # (a) providing a leased company car, (b) no leased car, or (c) no agreement;
       "pensionBenefits": ["0", "10", "20", "no agreement"], # Pension benefits: The possible value for the percentage of the salary deposited in pension funds are (a) 0\%, (b) 10\%, (c) 20\%, or (d) no agreement;
       "promotionPossibilities": ["2", "4", "no agreement"], # The possible values are (a) fast promotion track (2 years), (b) slow promotion track (4 years), or (c) no agreement;
       "workingHours": [8, 9, 10] # This issue describes the number of working hours required by the employee per day  The possible values are (a) 8 h, (b) 9 h, or (c) 10 h.
}

# the agent can read this data to trigger from sensor to NN
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

cv_sensor = CVSensor('cvSensor')


agent = AgentDefinition('sigon/aat_agent_nn.on', ctxs, [read_sensor, cv_sensor])
agent.run()

cv_sensor.perceive(json.dumps(aux))


read_sensor.perceive(json.dumps(aux))
