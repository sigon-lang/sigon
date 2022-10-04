from mcs.contexts.ctx_service import ContextService
import re

# this class will handle the AAT part of the reasoning cycle

class NegotiationCtx(ContextService):

    _instance = None    
    urgencies = []
    # Load model
    
    @classmethod
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def verify(self, fact):  # what this context will verify?

        return [{fact: True}]

    @classmethod
    def append_fact(self, fact) -> bool: # NOTE: what this context will append?
        print(fact)
        # greater(84000) 
        # 86668.31970214844 - adding this is wrong - TODO: check!
        # I could format fact in a dict
        if 'urgency' in str(fact): # ugly workaround
            self.urgencies.append(fact)

        return True

    @classmethod
    def add_initial_fact(self, fact) -> bool:
        return True

    @classmethod
    def find_urgency(self, fact) -> str:
        numbers = re.findall('[0-9]+', fact)
        for urgencies in self.urgencies:
            urgency_value = re.findall('[0-9]+', urgencies)





