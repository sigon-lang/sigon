from mcs.contexts.ctx_service import ContextService

# this class will handle the AAT part of the reasoning cycle

class NegotiationCtx(ContextService):

    _instance = None    
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
       
        return True

    @classmethod
    def add_initial_fact(self, fact) -> bool:
        return True

