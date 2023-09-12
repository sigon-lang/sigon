from sigonAgent import AgentDefinition
from sensors.DefaultSensor import DefaultSensor
from sensors.ContractSensor import ContractSensor
from sensors.CVSensor import CVSensor
from nn_ctx import NNCtx
from negotiation_ctx import NegotiationCtx
import json
import time
from prolog.prolog_service import PrologService
# from memory_profiler import profile


job_contract = {
    # Salary: The possible values are (a) \$7,000, (b) \$12,000, or (c) \$20,000; - changed to year
    "salary": [7000, 12000, 20000],
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

# @profile
def execute():
    NNCtx.ctx_name = '_nn'

    NegotiationCtx.ctx_name = '_negotiation'
    NegotiationCtx.salaries = []

    ctxs = []
    ctxs.append(NNCtx)
    ctxs.append(NegotiationCtx)

    read_sensor = ContractSensor('contractSensor')

    cv_sensor = CVSensor('cvSensor')

    agent = AgentDefinition('experiment2/aat_nn_agent_paper.on', ctxs,
                            [read_sensor, cv_sensor])

    agent.run()

    cv_sensor.perceive(json.dumps(cv_data))
    # one can use clear_data() to simulate triggering the NN in every reasoning cycle
    # cv_sensor.clear_data()
    

    read_sensor.perceive(json.dumps(job_contract))
    read_sensor.clear_data()  


def main():
    number_executions = 1
    times = []

    for i in range(number_executions):
        start_time = time.time()
        execute()
        result = time.time() - start_time        
        times.append(result*1000)

    print(times)


if __name__ == "__main__":
    main()
