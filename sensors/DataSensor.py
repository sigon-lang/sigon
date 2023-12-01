import os
from pubsub import pub
from agent.contexts.communication.sensor import Sensor
from agent.contexts.communication.communication_ctx_service import CommunicationContextService


class DataSensor(Sensor):    
    
    months = ['2018-01', '2018-02', '2018-03', '2018-04', '2018-05', '2018-06', '2018-07', '2018-08', '2018-09',
              '2018-10', '2018-11', '2018-12']   
    

    def __init__(self, name, base_dir):
        self.name = name
        self.base_dir = base_dir
        
    def perceive(self, perception):        
        pub.sendMessage(self.name, literal=perception, function=self.add) 

    def add(self, *args):           
        #args contain the current month to be processed        
        self.current_dir = os.path.join(self.base_dir, args[0])
        

    def verify(self, fact): 

        if len(str(self.current_dir)) > 0:                                    
            return [{fact: self.current_dir}]
                
        return []

    def clear_data(self):
        self.current_dir = ''