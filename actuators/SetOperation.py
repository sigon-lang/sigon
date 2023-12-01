from pubsub import pub
from agent.contexts.communication.actuator import Actuator
from agent.contexts.communication.communication_ctx_service import CommunicationContextService


class SetOperation(Actuator):

    def act(self, args):
        # this will set the operation based on the selected plan      
        
        CommunicationContextService.append_fact(args)
        
