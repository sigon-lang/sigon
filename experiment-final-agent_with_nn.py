from sigonAgent import AgentDefinition
from sensors.DefaultSensor import DefaultSensor
from sensors.ContractSensor import ContractSensor
from sensors.DataSensor import DataSensor
from nn_ctx import NNCtx
from metrics_ctx import MetricsCtx
import json
import time
from prolog.prolog_service import PrologService
# from memory_profiler import profile




# @profile
def execute():
    NNCtx.ctx_name = '_nn'

    MetricsCtx.ctx_name = '_metrics'
    

    ctxs = []
    ctxs.append(NNCtx)
    ctxs.append(MetricsCtx)


    data_sensor = DataSensor('dataSensor', '/home/rr/repositorios/experimento-final-tese/continual-learning-malware/ember2018/month_based_processing_with_family_labels')
    

    agent = AgentDefinition('malware-agent-v1/agent_malware_finetuning.on', ctxs,
                            [data_sensor])

    agent.run()

    months = ['2018-01', '2018-02', '2018-03', '2018-04', '2018-05', '2018-06', '2018-07', '2018-08', '2018-09',
              '2018-10', '2018-11', '2018-12']
    
    # months = ['2018-01', '2018-02']
    
    for month in months:
        data_sensor.perceive(month)

    
    print({
        'histories_evaluate': NNCtx.histories_evaluate,
        'histories_training': NNCtx.histories_training
    })

    print({
        'metrics': MetricsCtx.metrics
    })

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
