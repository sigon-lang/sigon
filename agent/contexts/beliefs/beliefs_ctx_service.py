from pyswip.easy import Variable

from pyswip.prolog import *
from prolog.prolog_service import PrologService
from mcs.contexts.ctx_service import ContextService

# nessa classe já vai receber o functor certinho, 
# a classe anterior é responsável por tratar as infos 
# e deixar com que elas cheguem certas

class BeliefsContextService(ContextService):

    _instance = None
    beliefs = []
    ctx_name = 'beliefs'
    
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
        return PrologService.retract(fact, cls.ctx_name)

    @classmethod
    def append_fact(cls, fact):
       cls.beliefs.append(fact)
       PrologService.append_fact(fact, cls.ctx_name)

    @classmethod
    def add_beliefs(cls, facts): #acho que esse metodo nao rola mais, pq mudou muito a maneira como trata a string
        if len(cls.beliefs) == 0 :
            cls.beliefs = facts
        else:
            for b in facts:
                cls.beliefs.append(b)
        PrologService.append_facts(facts, cls.ctx_name)
        
    @classmethod
    def print_beliefs(cls):
        print(cls.beliefs)

    @classmethod
    def get_clauses(cls):
        return cls.beliefs
	
    @classmethod
    def add_initial_fact(cls, fact):        
        cls.append_fact(fact)

    @classmethod
    def get_name(cls) -> str:
        return cls.ctx_name


    #Notes how sigon-j deals with arity = 0 and arity > 0 in the same context??