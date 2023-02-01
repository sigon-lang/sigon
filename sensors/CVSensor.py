import os
from pubsub import pub
from agent.contexts.communication.sensor import Sensor
from agent.contexts.communication.communication_ctx_service import CommunicationContextService


class CVSensor(Sensor):    
    

    def __init__(self, name):
        self.name = name
        self.contract_options = ''
        
    def perceive(self, perception):        
        pub.sendMessage(self.name, literal=perception, function=self.add) 

    def add(self, *args):     
        # acho que nao é assim o correto
        self.contract_options = args[0]
        #print(self.contract_options)
        # print(self.contract_options)
        # CommunicationContextService.verify_implementation.append({'contractSensor': args[0]})

    def verify(self, fact): #NOTE aqui poderia fazer um parsing para conter varios facts
        # print(self.contract_options)
        if len(str(self.contract_options)) > 0:            
            contract_options = self.contract_options
            #self.contract_options = ''
            return [{fact: contract_options}]
        
        return []

    def clear_data(self):
        self.contract_options = ''