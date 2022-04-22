from pubsub import pub
from agent.contexts.communication.actuator import Actuator


class DefaultActuator(Actuator):

    def act(self, args):
        print('acting ', args)
