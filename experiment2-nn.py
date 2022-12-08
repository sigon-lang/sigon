from sigonAgent import AgentDefinition
from sensors.DefaultSensor import DefaultSensor
from sensors.ContractSensor import ContractSensor
from sensors.CVSensor import CVSensor
from nn_ctx import NNCtx
from negotiation_ctx import NegotiationCtx
import json
import time
# from memory_profiler import profile


# Description

# Initial evalutation for setup 1- salary definition
# Compare time to execute - 21 executions - excluding the first one - reason: modules loading time
# files to be tested: aat_agent_nn_salary_v2_sem_experiencia x aat_agent_salary_2

# @profile
def execute():
    
    job_contract_competition = {
        # Salary: The possible values are (a) \$7,000, (b) \$12,000, or (c) \$20,000; - changed to year
        "salary": [2000*12, 2500*12, 3000*12, 3500*12, 4000*12],
        # Responsibilities given to the employer. The possible values are (a) QA, (b) Programmer, (c) Team Manager, or (d) Project Manager;
        # "jobDescription": ["qa", "programmer", "teamManager", "projectManager"],
        # (a) providing a leased company car, (b) no leased car, or (c) no agreement;
        "carBenefits": ["yes", "no"], # distancia
        "permanentContract": ["yes", "no"], # nao sei - pode ser atraves das horas ocupadas
        "careerPossibilities": ["low", "medium", "high"], # idade ou experiencia ok
        # This issue describes the number of working hours required by the employee per day  The possible values are (a) 8 h, (b) 9 h, or (c) 10 h.
        "fte": [24, 32, 40] # horas ocupadas
    }

    # the agent can read this data to trigger from sensor to NN
    cv_data = {'python_yn': 1,
               'spark': 1,
               'aws': 1,
               'excel': 1,
               'job_simp': 'data scientist',
               'seniority': 'senior'
               }

    NNCtx.ctx_name = '_nn'

    NegotiationCtx.ctx_name = '_negotiation'

    ctxs = []
    ctxs.append(NNCtx)
    ctxs.append(NegotiationCtx)

    read_sensor = ContractSensor('contractSensor')

    cv_sensor = CVSensor('cvSensor')   

    agent = AgentDefinition('sigon/experiment2_agents/aat_agent_nn_salary_experience_v2-scenario2.on', ctxs,
                            [read_sensor, cv_sensor])
    
    agent.run()    

    read_sensor.perceive(json.dumps(job_contract_competition))
    cv_sensor.perceive(json.dumps(cv_data))
    


number_executions = 1
times = []
for i in range(number_executions):
    start_time = time.time()
    execute()
    result = time.time() - start_time
    #print("Iteration %d - %s " % (i, result))
    times.append(result)   


print(times)
    

# acting  ['car', ' yes']
# acting  ['workingHours', ' 32']
# acting  ['permanentContract', ' yes']
# acting  ['car', ' yes']
# acting  ['workingHours', ' 32']
# acting  ['permanentContract', ' yes']
# acting  ['car', ' yes']
# acting  ['workingHours', ' 32']
# acting  ['permanentContract', ' yes']
# acting  ['salary', ' 3000']
# acting  ['careerPossibilities', ' high']
# tempo 0.10880613327026367
# calcular f.u


# salary - 3000 (peso 1) - peso na f.u 0.2900838579284962
# workingHours - 32 (0.5) -  peso na f.u 0.38507247973666225
# car - yes (1) - peso na f.u 0.07628234656996354
# permanentContract - yes (1) - peso na f.u 0.19444527477051546
# careerPossibilities - high (1) - peso na f.u 0.05411415124288346

# 1*0.2900838579284962 + 0.5*0.38507247973666225 + 1*0.07628234656996354 + 1*0.19444527477051546 + 1*0.05411415124288346 -
# F.U 0.8074618703801898


# acting  ['car', ' yes']
# acting  ['workingHours', ' 40']
# acting  ['car', ' yes']
# acting  ['workingHours', ' 40']
# acting  ['car', ' yes']
# acting  ['workingHours', ' 40']
# acting  ['salary', ' 3000']
# acting  ['careerPossibilities', ' high']
# [0.0989532470703125]

# 1*0.2900838579284962 + 1*0.38507247973666225 + 1*0.07628234656996354 + 1*0.19444527477051546 + 1*0.05411415124288346
# F.U 1
