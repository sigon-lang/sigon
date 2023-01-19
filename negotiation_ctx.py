from mcs.contexts.ctx_service import ContextService
import re
from prolog.prolog_service import PrologService

# this class will handle the AAT part of the reasoning cycle

class NegotiationCtx(ContextService):

    _instance = None    
    urgencies = [] # ter um metodo que adicione a urgencia no prolog
    negotiation_goals = []
    salaries = []
    urgency_level = 10
    
    # Load model
    
    @classmethod
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def verify(self, fact):  
        # r = PrologService.verify_custom(fact, self.ctx_name)
        # print("tamanho do verify", len(r))
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
    def append_fact(self, fact) -> bool: # NOTE: what this context will append?
        
        
        if 'avgSalary(' in fact:
            value = fact[fact.find('(')+1: fact.find(')')]    
            self.update_urgency(value)
        
        if 'salary(' in fact:
            value = fact[fact.find('(')+1: fact.find(')')]
            #if value not in self.salaries:
            self.salaries.append(value)
        # todo vez que adicionar algo, posso dar update na urgencia
        # greater(84000) 
        # 86668.31970214844 - adding this is wrong - TODO: check!
        # I could format fact in a dict
        if 'urgency' in str(fact): # ugly workaround
            if fact not in self.urgencies:
                # print(fact)
                self.urgencies.append(fact)  # ALWAYS ADD NEW FACT EVEN IF THIS FACT ALREADY EXISTS
                PrologService.append_fact(fact, self.ctx_name)
        

    @classmethod
    def add_initial_fact(self, fact) -> bool:
        return True

    @classmethod
    def find_urgency(self, fact) -> str:
        number = re.findall('[0-9]+', fact)
        for urgencies in self.urgencies:
            urgency_value = re.findall('[0-9]+', urgencies)
            if urgency_value == number:
                return urgencies

        return ''                




# NegotiationCtx.ctx_name = '_negotiation'
# # "salary": [7000, 12000, 20000]
# NegotiationCtx.append_fact('salary(7000)')
# NegotiationCtx.append_fact('salary(12000)')
# NegotiationCtx.append_fact('salary(20000)')
# print(NegotiationCtx.salaries)

# NegotiationCtx.append_fact('avgSalary(7500)')


