from agent.contexts.communication.actuator import Actuator
from agent.contexts.beliefs.beliefs_ctx_service import BeliefsContextService
from agent.contexts.desires.desires_ctx_service import DesiresContextService
from pyswip.easy import Variable
from agent.contexts.communication.sensor import Sensor

from pyswip.prolog import *
from prolog.prolog_service import PrologService
from mcs.contexts.ctx_service import ContextService
import re


class CommunicationContextService(ContextService):

    _instance = None
    actuators = []
    sensors = []
    ctx_name = 'communication'
    verify_implementation = []
    

    @classmethod
    def get_theory(cls):
        return cls.prolog

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def verify(cls, fact):
        # NOTE: fact tem que ter alguma maneira de ligar com o sensor - quando for um sensor que não usa prolog

        # NOTE: se for enviado algo sem variavel, então o verify custom deve retornar apenas o fact e o seu correspondente

        sensor_name = ''

        if fact.find('(') == -1:
            sensor_name = fact
        else:
            sensor_name = fact[0:fact.index('(')]
            # variable =  fact[fact.index('(')+1:fact.index(')')]
            # variable = re.findall('\(.*?\)', fact)[fact.index('(')]
            # NOTE: these solution does not considered that inlined parenthesis can be used during reasoning
            variable = fact[fact.find('(')+1:fact.rfind(')')]

        for sensor in cls.sensors:
            if sensor_name == sensor.name:
                # NOTE aqui nao pega o valor certo
                return sensor.verify(variable)
                # return cls.verify_implementation # invocar a funcao de verify - opcao 2

        # NOTE: eu poderia jogar a implementacao do verify e add dentro do sensor
        return PrologService.verify(fact, cls.ctx_name)

    @classmethod
    def remove(cls, fact):
        return PrologService.retract(fact, cls.ctx_name)

    @classmethod
    def append_fact(cls, fact):

        if fact.startswith('sense'):
            PrologService.append_fact(fact, cls.ctx_name)

        else:
            i = fact.index('(')
            name = fact[0: i]

            actuators = list(filter((lambda a: a.name == name), cls.actuators))            
            
            if actuators:
                actuator = actuators[0]
                arg = fact[i + 1: len(fact)-1]
                args = arg.split(",")
                actuator.act(args)
                # actuator.act(args) #verificar pq é feito o split e depois convertido para string novamente

    @classmethod
    # metodo encarregado de adicionar percepcao utilizando a funcao passada por parametro
    def append_perception(cls, fact, function=None):
        function(fact)

    @classmethod
    def append_facts(cls, fact):

        i = fact.index('(')
        name = fact[0: i]
        actuators = list(filter((lambda a: a.name == name), cls.actuators))
        if actuators:
            arg = fact[i + 1: len(fact)-1]
            args = arg.split(",")
            print(args)  # TODO: Implementar e testar actuator
            # actuator.act(args) #verificar pq é feito o split e depois convertido para string novamente

    @classmethod
    def add_initial_fact(cls, fact):
        cls.append_fact(fact)

    @classmethod
    def get_name(cls) -> str:
        return cls.ctx_name
