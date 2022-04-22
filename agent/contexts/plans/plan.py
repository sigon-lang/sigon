

class Plan:
    def __init__(self, preconditions = {}, posconditions = {},
    actions = []):
        self.preconditions = preconditions
        self.posconditions = posconditions
        self.actions = actions
        self.something_to_be_true = ''

    