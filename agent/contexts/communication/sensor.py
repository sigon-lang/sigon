from pubsub import pub



class Sensor: #TODO: como testar o multi threading do sigon?
    name = ''
    
    def __init__(self, name):
        self.name = name

    def perceive(self, perception, function):
        pub.sendMessage(self.name, literal=perception, function=function) #isso poderia ser feito na classe que extende sensor - acho que é o funcionamento correto

    def add(self, *args):
        pass