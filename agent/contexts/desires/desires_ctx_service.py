from pyswip.easy import Variable
from mcs.contexts.ctx_service import ContextService
from pyswip.prolog import *
from prolog.prolog_service import PrologService



class DesiresContextService(ContextService):

    
    _instance = None
    prolog = Prolog()
    desires = []
    ctx_name = 'desires'

    
    @classmethod
    def get_theory(cls):
        return cls.prolog       


    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def verify(cls, fact):  
        return PrologService.verify_custom(fact, cls.ctx_name)
        

    @classmethod
    def remove(cls, fact):
        cls.desires.remove(fact)
        return PrologService.retract(fact, cls.ctx_name)

    @classmethod
    def append_fact(cls, fact):
       cls.desires.append(fact)
       PrologService.append_fact(fact, cls.ctx_name)

    @classmethod
    def add_desires(cls, facts):
        if len(cls.desires) == 0 :
            cls.desires = facts
        else:
            for b in facts:
                cls.desires.append(b)
        PrologService.append_facts(facts, cls.ctx_name)
        
    @classmethod
    def print_desires(cls):
        print(cls.desires)

    @classmethod
    def get_clauses(cls):
        return cls.desires
	
    @classmethod
    def add_initial_fact(cls, fact):        
        cls.append_fact(fact)

    @classmethod
    def get_name(cls) -> str:
        return cls.ctx_name


