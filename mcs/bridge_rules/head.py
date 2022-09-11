
class Head:
    bindings = []
    variables = []

    def __init__(self, ctxName = None, clause : str = '', ctxNegation = False, ctx = None):
        self.ctxNegation = ctxNegation
        self.ctxName = ctxName
        self.clause = clause
        self.ctx = ctx
        
    
    def to_string(self):
        return str(self.ctxNegation) + ' ' + self.ctxName + ': ' + self.clause


   

    def append_facts(self):               
       for variable in self.bindings:
            #obter keys de variable
            current_clause = self.clause
            for key in variable: 
                #TODO: verificar se a variável currentClause possui ( e ), caso sim,
                # o replace deve ser feito após o primeiro (, se não apenas substitui o clause inteiro
                if type(variable.get(key)) is str:
                    current_clause = current_clause.replace(key, variable.get(key))
                else:
                    #TODO: iterar sobre a lista e obter valores
                    current_clause = variable.get(key)

            self.ctx.append_fact(current_clause)
        
