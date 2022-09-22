


from mcs.contexts.ctx_service import ContextService
from mcs.bridge_rules.head import Head
from mcs.bridge_rules.body import Body


class BridgeRule:
    def __init__(self, head, body):        
        self.head = head
        self.body = body
    
    def execute(self):       
        self.body.head = self.head #nao precisa disso, TODO: mudar para obter o binding se o if for true       
        if self.body.verify():
            self.head.append_facts()
            return True
        return False


    def execute_custom(self, ctxs): #esse metodo é todo errado, não deveria ser assim!!!
        assert isinstance(self.body, Body)
        self.body.head = self.head
        if self.body.verify_custom(ctxs): 
            self.head.append_facts()
        

        return True

