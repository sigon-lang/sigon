from pubsub import pub
from agent.contexts.communication.actuator import Actuator
from agent.contexts.communication.communication_ctx_service import CommunicationContextService


class ProcessData(Actuator):

    

    def __init__(self, sensor):
        self.current_month = 0
        self.sensor = sensor
    def act(self, args):
        print(args)
        # triggers the sensor to process new data
        self.sensor.perceive(self.current_month)        
        self.current_month += 1

        
