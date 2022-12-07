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
    job_contract = {
        # Salary: The possible values are (a) \$7,000, (b) \$12,000, or (c) \$20,000; - changed to year
        "salary": [84000, 144000, 240000],
        # Responsibilities given to the employer. The possible values are (a) QA, (b) Programmer, (c) Team Manager, or (d) Project Manager;
        "jobDescription": ["qa", "programmer", "teamManager", "projectManager"],
        # (a) providing a leased company car, (b) no leased car, or (c) no agreement;
        "carBenefits": ["yes", "no", "noAgreement"],
        # Pension benefits: The possible value for the percentage of the salary deposited in pension funds are (a) 0\%, (b) 10\%, (c) 20\%, or (d) no agreement;
        "pensionBenefits": ["0", "10", "20", "noAgreement"],
        # The possible values are (a) fast promotion track (2 years), (b) slow promotion track (4 years), or (c) no agreement;
        "promotionPossibilities": ["2", "4", "noAgreement"],
        # This issue describes the number of working hours required by the employee per day  The possible values are (a) 8 h, (b) 9 h, or (c) 10 h.
        "workingHours": [8, 9, 10],
        "negotiate": ["contract"]
    }

    job_contract_competition = {
        # Salary: The possible values are (a) \$7,000, (b) \$12,000, or (c) \$20,000; - changed to year
        "salary": [2000*12, 2500*12, 3000*12, 3500*12, 4000*12],
        # Responsibilities given to the employer. The possible values are (a) QA, (b) Programmer, (c) Team Manager, or (d) Project Manager;
        # "jobDescription": ["qa", "programmer", "teamManager", "projectManager"],
        # (a) providing a leased company car, (b) no leased car, or (c) no agreement;
        "carBenefits": ["yes", "no"],
        "permanentContract": ["yes", "no"],
        "careerPossibilities": ["low", "medium", "high"],
        # This issue describes the number of working hours required by the employee per day  The possible values are (a) 8 h, (b) 9 h, or (c) 10 h.
        "fte": [24, 32, 40]
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

    agent = AgentDefinition('sigon/experiment1_agents/aat_agent_salary_2.on', ctxs,
                            [read_sensor])
    
    agent.run()    

    read_sensor.perceive(json.dumps(job_contract))
    


number_executions = 51
times = []
for i in range(number_executions):
    start_time = time.time()
    execute()
    result = time.time() - start_time
    #print("Iteration %d - %s " % (i, result))
    times.append(result)   


print(times)
    
