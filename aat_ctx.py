from mcs.contexts.ctx_service import ContextService


class AATCtx(ContextService):

    _instance = None        
    
    
    @classmethod
    def __new__(cls):        
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def verify(self, fact): 
        return [{fact: self.avg_salary}]

    @classmethod
    def append_fact(self, fact) -> bool:
        
        return True

    @classmethod
    def add_initial_fact(self, fact) -> bool:
        return True
            

