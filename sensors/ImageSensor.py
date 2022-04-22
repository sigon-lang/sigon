from prolog.prolog_service import PrologService
import os
from pubsub import pub
from agent.contexts.communication.sensor import Sensor
from agent.contexts.communication.communication_ctx_service import CommunicationContextService
import re
import cv2
import numpy as np

import cv2

class ImageSensor(Sensor):
    

    def __init__(self, name):
        self.name = name
        self.col_images = None
        
    def perceive(self, perception):        
        pub.sendMessage(self.name, literal=perception, function=self.add) 

    def add(self, *args): #Add do deepface
        # self.img = cv2.imread(args[0])
        # get file names of the frames
            
        CommunicationContextService.verify_implementation.append({'X': args[0]})
        
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

    def verify(self, fact): #NOTE aqui poderia fazer um parsing para conter varios facts
        if self.col_images is not None:
            return [{fact: self.col_images}]
        
        return []