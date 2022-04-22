from pyswip.easy import Variable

from pyswip.prolog import *
from prolog.prolog_service import PrologService
from mcs.contexts.ctx_service import ContextService


class IntentionsContextService(ContextService):

    
    # #__instance = BeliefsContextService how can i do this?
    _instance = None
    intentions = []
    ctx_name = 'intentions'

    # def getInstance():
    #     return BeliefsContextService.__instance
    
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
       cls.intentions.append(fact)
       PrologService.append_fact(fact, cls.ctx_name)

    @classmethod
    def add_intentions(cls, facts):
        if len(cls.intentions) == 0 :
            cls.intentions = facts
        else:
            for b in facts:
                cls.intentions.append(b)
        PrologService.append_facts(facts, cls.ctx_name)
        
    @classmethod
    def print(cls):
        print(cls.intentions)

    @classmethod
    def get_clauses(cls):
        return cls.intentions
	
    @classmethod
    def add_initial_fact(cls, fact):        
        cls.append_fact(fact)

    @classmethod
    def get_Name(cls) -> str:
        return cls.ctx_name

    @classmethod
    def check_intentions(cls):
        for d in DesiresContextService.desires: #seria mais consistente consultar a base de crenças toda vez?
            if not BeliefsContextService.verify(d): #aqui estou seguindo o que foi feito na primeira versao do sigon, checando na kb se existe esse desejo
                cls.append_fact(d)
                #check exceptions



