


class Actuator:
    name = ''
    
    def act(args):
        raise NotImplementedError
    
    def __init__(self, name):
        self.name = name

    