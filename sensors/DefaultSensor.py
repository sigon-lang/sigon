from prolog.prolog_service import PrologService
from pubsub import pub
from agent.contexts.communication.sensor import Sensor
from agent.contexts.communication.communication_ctx_service import CommunicationContextService

class DefaultSensor(Sensor):

    def __init__(self, name):
        self.name = name
        
    def perceive(self, perception):
        #NOTE: Poderia ter um objeto com a estrutura que quero utilizar
        pub.sendMessage(self.name, literal=perception, function=self.add) 


    def add(self, *args):      
        # Use a JSON or DICT with N fields and then add N new beliefs  
        return CommunicationContextService.append_fact(args[0].join(['sense(', ')']))