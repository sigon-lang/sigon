
class ContextService:
    
    ctx_name = ''

    def __init__(self, ctx_name):
        self.ctx_name = ctx_name

    def verify(self, fact):
        raise NotImplementedError

    def append_fact(self, fact) -> bool: #it seems that these two methods do the same thing haha
        raise NotImplementedError
	
    def add_initial_fact(self, fact) -> bool:
        raise NotImplementedError

    #public Theory getTheory(); - I've removed this method, since a context could be implemented without a prolog engine