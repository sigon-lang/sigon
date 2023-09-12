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
        "salary": [2000, 2500, 3000, 3500, 4000],
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
    cv_data = {
        'Rating': 2,
        'Size': '51 to 200 employees',
        'Type of ownership': 'Unknown',
        'Industry': 'Architectural & Engineering Services',
        'Sector': 'Business Services',
        'Revenue': '$25 to $50 million (USD)',
        'num_comp': 0,
        'hourly': 0,
        'employer_provided': 0,
        'job_state': 'AL',
        'same_state': 0,
        'age': 20,
        'python_yn': 0,
        'spark': 0,
        'aws': 0,
        'excel': 0,
        'job_simp': 'na',
        'seniority': 'junior'
    }
     

    NNCtx.ctx_name = '_nn'

    NegotiationCtx.ctx_name = '_negotiation'

    ctxs = []
    ctxs.append(NNCtx)
    ctxs.append(NegotiationCtx)

    read_sensor = ContractSensor('contractSensor')

    cv_sensor = CVSensor('cvSensor')   

    agent = AgentDefinition('experiment3_agents_v2/aat_agent_nn_salary_experience_v2-scenario3_low_salary.on', ctxs,
                            [read_sensor, cv_sensor])
    
    agent.run()    

    cv_sensor.perceive(json.dumps(cv_data))

    read_sensor.perceive(json.dumps(job_contract_competition))
    
    


number_executions = 20
times = []
for i in range(number_executions):
    start_time = time.time()
    execute()
    result = time.time() - start_time
    #print("Iteration %d - %s " % (i, result))
    times.append(result)   


print(times)
    

# acting  ['salary', ' 2000']
# acting  ['careerPossibilities', ' low']
# [0.09042787551879883]


# salary - 2000 (peso 1) - peso na f.u 0.64
# careerPossibilities - low (1) - peso na f.u 0.36
# F.U 1
