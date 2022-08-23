

from mcs.bridge_rules.bridge_rules_ctx_service import BridgeRulesContextService
from agent.contexts.plans.plan import Plan
from parsing.languages.lang_actuator import LangActuator
from agent.exception import CtxNotFound
from parsing.languages.lang_ctx import LangContext
from parsing.languages.lang_sensor import LangSensor
from mcs.contexts.ctx_service import ContextService
from agent.contexts.communication.communication_ctx_service import CommunicationContextService
from pubsub import pub
from agent.contexts.intentions.intentions_ctx_service import IntentionsContextService
from agent.contexts.plans.plans_ctx_service import PlansContextService
from agent.contexts.beliefs.beliefs_ctx_service import BeliefsContextService
from agent.contexts.desires.desires_ctx_service import DesiresContextService
from parsing.agent_walker import AgentWalker
from agent.contexts.communication.actuator import Actuator
import importlib 
import threading





class Agent:
    ctxs = {} #dic com o nome dos ctxs e suas referencias
    sensors = []
    received_sensors = []
    actuators = []
    def __init__(self, custom_ctxs = [], sensors = []): #metodo dummy só para testes
        self.ctxs[BeliefsContextService.ctx_name] = BeliefsContextService
        self.ctxs[DesiresContextService.ctx_name] = DesiresContextService
        self.ctxs[IntentionsContextService.ctx_name] = IntentionsContextService
        self.ctxs[PlansContextService.ctx_name] = PlansContextService
        self.ctxs[CommunicationContextService.ctx_name] = CommunicationContextService
        self.received_sensors = sensors
        for custom_ctx in custom_ctxs:
            custom_ctx.ctx_name = custom_ctx.ctx_name.replace('_', '')
            self.ctxs[custom_ctx.ctx_name] = custom_ctx
        

    def run(self, walker: AgentWalker):
        self.init_contexts(walker)
        self.subscribe_sensors()
        CommunicationContextService.actuators = self.actuators
        CommunicationContextService.sensors = self.sensors
        


    # def subscribeSensors(self):
    #     for sensor in self.sensors:
    #         pub.subscribe(self.bdiAlgorithm, sensor.name)


    # def startSensors(self): TODO: como lidar com o multithreading?
    #     for sensor in self.sensors:
    #         threading.Thread(target=)
    #         pass
    #     pass   

    def init_contexts(self, walker: AgentWalker): # eu podia iniciar de forma generica aqui
        for lang_ctx in walker.lang_contexts:                       
            
            for c in lang_ctx.clauses:
                try:
                    ctx = self.ctxs.get(lang_ctx.name)
                    
                    if ctx:
                        ctx.append_fact(c)
                    else:
                        message = f'Context {lang_ctx.name} not found'
                        raise CtxNotFound(message)

                except CtxNotFound as ctxNotFound:
                    print(str(ctxNotFound.message))


        for lang_sensor in walker.lang_sensors:
            sensor_implementation = lang_sensor.implementation.split('.')
            sensor_implementation_module = sensor_implementation[0]
            class_name = sensor_implementation[1]
            # NOTE: poderia usar um dict para obter de forma rapida o sensor
            for rcv_sensor in self.received_sensors:
                if rcv_sensor.name == lang_sensor.identifier:
                    self.sensors.append(rcv_sensor)
            # sensor_implementation = importlib.find_loader(sensor_implementation_module)
            # if sensor_implementation is not None:

                # mod = __import__(lang_sensor.implementation, fromlist=[class_name])
                # Sensor = getattr(mod, class_name)                
                # s = Sensor(name=lang_sensor.identifier)
                # self.sensors.append(s) #TODO: é feito um append de um sensor que nao executou o perceive

        for lang_actuator in walker.lang_actuators:
            # assert isinstance(langActuator, LangActuator)                    
            actuator_implementation = lang_actuator.implementation.split('.')
            actuator_implementation_module = actuator_implementation[0]
            class_name = actuator_implementation[1]
            actuator_implementation = importlib.find_loader(actuator_implementation_module)
            if actuator_implementation is not None:
                mod = __import__(lang_actuator.implementation, fromlist=[class_name])
                Actuator = getattr(mod, class_name)                
                a = Actuator(name=lang_actuator.identifier)
                self.actuators.append(a)                

        PlansContextService.ctxs = self.ctxs
        PlansContextService.append_facts(walker.plans)
        
        BridgeRulesContextService.bridge_rules = walker.bridge_rules
        BridgeRulesContextService.ctxs = self.ctxs
 
        

    def bdi_algorithm(self, literal, function):        
        # with self.lock:
        # if literal.startswith('-'):            
        #     literal = literal.replace('-', '').trim()
        #     self.removeBelief = True
        # elif literal.startswith('not'):
        #     literal = literal.replace('not', '\\+').trim()

        # self.cycles += 1
        # sense = literal.join(['sense(', ')'])
        
        
        CommunicationContextService.append_perception(literal, function)
        #jogar lógica de removeBelief com base no retorno do método de CC

        #NOTE: ideia 2- usar decorator para definir como adicionar uma nova percepção - 
        # sensor diz para o CC como adicionar e verificar novas percepções

        #bridge rules to execute a bdi algorithm
        BridgeRulesContextService.execute_BDI_rules()
        BridgeRulesContextService.execute_bridge_rules()

        PlansContextService.execute_plan_algorithm()
        
            
                
    def subscribe_sensors(self):
        for observables in self.sensors:
            pub.subscribe(self.bdi_algorithm, observables.name)
        

