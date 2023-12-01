from mcs.contexts.ctx_service import ContextService
import re
import numpy as np
from prolog.prolog_service import PrologService

# this class will handle the AAT part of the reasoning cycle

class MetricsCtx(ContextService):

    _instance = None    
    
    
    @classmethod
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def verify(self, fact):         
        # returns performance(X)
        return PrologService.verify_custom(fact, self.ctx_name)

    @classmethod
    def update_urgency(self, fact):
        # fact contem avgSalary(Valor)
        # pŕeciso formatar antes o avgSalary
        # find the lowest difference from salary and fact
        if len(self.salaries) > 0:
            min_value = abs(float(self.salaries[0]) - float(fact))
            current_salary = self.salaries[0]
            for i in range(1, len(self.salaries), 1):
                current_value = abs(float(self.salaries[i]) - float(fact)) 
                if min_value > current_value:
                    min_value = current_value
                    current_salary = self.salaries[i]

            defined_urgency = 'urgency(salary, {}, {})'.format(current_salary, self.urgency_level)
            if defined_urgency not in self.urgencies:
                self.urgencies.append(defined_urgency)
                #if not PrologService.verify_custom(defined_urgency, self.ctx_name):        
                PrologService.append_fact(defined_urgency, self.ctx_name)

        

    @classmethod
    def append_fact(self, fact) -> bool:       
        


        print(fact) # can have history from training and history from evaluation        

    #         //performance(low). < 60
    # //performance(medium).  >= 60 < 83
    # //performance(high).  >= 83 < 100    

        
        PrologService.append_fact(self.parse_metrics(fact), self.ctx_name)

    @classmethod
    def parse_metrics(self, history):
        # [{'accuracy': 0.8767322301864624, 'loss': 0.2873293161392212}]
        accuracy = round(history[0]['accuracy']*100)
        # loss = round(history[0]['loss'])
        
        

        if accuracy < 60:
            return 'performance(low)'
        elif accuracy >= 60 and accuracy < 83:
            return 'performance(medium)'
        
        return 'performance(high)'            

    @classmethod
    def add_initial_fact(self, fact) -> bool:
        return True

    



# NegotiationCtx.ctx_name = '_negotiation'
# # "salary": [7000, 12000, 20000]
# NegotiationCtx.append_fact('salary(7000)')
# NegotiationCtx.append_fact('salary(12000)')
# NegotiationCtx.append_fact('salary(20000)')
# print(NegotiationCtx.salaries)

# NegotiationCtx.append_fact('avgSalary(7500)')


