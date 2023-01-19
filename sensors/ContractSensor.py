import os
from pubsub import pub
from agent.contexts.communication.sensor import Sensor
from agent.contexts.communication.communication_ctx_service import CommunicationContextService
import json

from prolog.prolog_service import PrologService


class ContractSensor(Sensor):
    
    

    def __init__(self, name):
        self.name = name
        self.contract_options = ''
        
    def perceive(self, perception):        
        pub.sendMessage(self.name, literal=perception, function=self.add) 

    def add(self, *args):     
        # acho que nao é assim o correto
        self.contract_options = json.loads(args[0])
        for key in self.contract_options.keys():
            for option in self.contract_options[key]:
                # predicate = 'sense' + '(' + key + '(' + str(option) + ')'+ ')'
                predicate = key + '(' + str(option) + ')'
                PrologService.append_fact(predicate, self.name)
                # CommunicationContextService.append_fact(predicate)
        # print(self.contract_options)
        # CommunicationContextService.verify_implementation.append({'contractSensor': args[0]})
        
    # def add(self, *args):
    #     # self.img = cv2.imread(args[0])
    #     # get file names of the frames
    #     col_frames = os.listdir(args[0])

    #     # sort file names
    #     col_frames.sort(key=lambda f: int(re.sub('\D', '', f)))

    #     # empty list to store the frames
    #     self.col_images=[]

    #     for i in col_frames:
    #         # read the frames
    #         img = cv2.imread(args[0]+'/'+i)
    #         # append the frames to the list
            
    #         self.col_images.append(img[604:1068, 836:1175])
            
    #     CommunicationContextService.verify_implementation.append({'imageSensor': self.col_images})
    #     # CommunicationContextService.verifyImplementation.update({'imageSensor': self.col_images})
    #     # return CommunicationContextService.appendFact(args[0].join(['sense(', ')']))

    # aqui só posso mandar a variável
    def verify(self, fact): #NOTE aqui poderia fazer um parsing para conter varios facts
        # TODO: reescrever para adequar ao novo formato
        # print(self.contract_options)
        if len(str(self.contract_options)) > 0:     
            result = PrologService.verify_custom(fact, self.name)
            # print(result)                   
            return result #['X': ['a', 'b', 'c']]
        
        return []

    def clear_data(self):
        self.contract_options = ''
   