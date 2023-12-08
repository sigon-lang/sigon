from mcs.contexts.ctx_service import ContextService
import re
import numpy as np
from prolog.prolog_service import PrologService

# this class will handle the AAT part of the reasoning cycle

class MetricsCtx(ContextService):

    _instance = None    
    metrics = []
    
    
    @classmethod
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        
        return cls._instance

    @classmethod
    def verify(self, fact):         
        # returns performance(X)
        if 'findParameters' not in fact:
            return PrologService.verify_custom(fact, self.ctx_name)
        elif 'findParameters' in fact:
            parameters = self.find_parameters()
            
            return [{fact: parameters}]

    @classmethod
    def find_parameters(self):
        performance_value = PrologService.verify_custom('performance(X)', self.ctx_name)
        if len(performance_value) > 0:
            print(performance_value)           
            return {
                'low': {
                    'patience': 'increase2x',
                    'min_delta': 'decrease'
                },
                'medium': {
                    'patience': 'increase',
                    'min_delta': 'keep'
                },
                'high': {
                    'patience': 'decrease',
                    'min_delta': 'increase'
                }
            }.get(performance_value[0].get('X', 'medium'))
            
        
    


        
        

    @classmethod
    def append_fact(self, fact) -> bool:       
        print(fact) # can have history from training and history from evaluation        

        if type(fact) == list and 'accuracy' in fact[0]:
            PrologService.retract_all('performance(X)', self.ctx_name)
            PrologService.append_fact(self.parse_metrics(fact), self.ctx_name)
        elif 'operation' in fact:
            PrologService.append_fact(fact, self.ctx_name)

    @classmethod
    def parse_metrics(self, history):
        # [{'accuracy': 0.8767322301864624, 'loss': 0.2873293161392212}]
        accuracy = round(history[-1]['accuracy']*100)
        self.metrics.append(history[-1])
        # loss = round(history[0]['loss'])       
        

        if accuracy < 60:
            return 'performance(low)'
        elif accuracy >= 60 and accuracy < 92:
            return 'performance(medium)'
        
        return 'performance(high)'            

    @classmethod
    def add_initial_fact(self, fact) -> bool:
        return True

    



