

from mcs.bridge_rules.head import Head
from posixpath import join
from prolog.prolog_service import PrologService
# from agent.agent import Agent
from pyswip.easy import Term


class Body:

    body_terms = []
    variables_to_be_added = []

    # NOTE: quando eu usava terms = [], por algum motivo o terms na segunda "iteração" chegava já preenchido
    def __init__(self, head: Head = Head(), terms=None):
        self.body_terms = terms or []
        self.head = head

    def to_string(self):
        return '\n'.join(self.body_terms)

    def create_bool_expression(self, expressions):


        return bool(eval(' '.join(str(exp) for exp in expressions)))

    # NOTE: preciso verificar cada BR como um todo, ideia é montar uma string de verificacao -> inserir numa lista o retorno booleano
    def verify_custom(self, ctxs):
        bindings = []
        boolean_operators = []
        for body_term in self.body_terms:            
            ctx = ctxs[body_term.ctx_name]
            # NOTE: each verify must return a list containing dicts with variable and its results
            # [{fact: 'verifyResult'}]
            # {'X': 'aware', 'Y': 'notifyPedestrian'} [{fact: 'verifyResults'}]
            binding_results = ctx.verify(body_term.terms)
            if body_term.negation: # NOTE: do we have to user xor?
                boolean_operators.append('not')
            if body_term.operator == ',':
                boolean_operators.append('and') 
            elif body_term.operator == '|':
                boolean_operators.append('or')     
            boolean_operators.append(bool(binding_results))    

            # TODO: check if existing binding: X -> aux, next iteration X-> aux2                        
            for variable_value_dict in binding_results:                
                bindings.append(variable_value_dict)
                
        if bool(eval(' '.join(str(exp) for exp in boolean_operators))):
            self.head.bindings = bindings 
        
        return bool(self.head.bindings)

    def verify(self):
        facts = ''
        for body_term in self.body_terms:
            assert isinstance(body_term, BodyTerm)

            fact = body_term.terms
            if body_term.operator == '':

                facts += (fact.join([body_term.ctx_name+'(', ')'])
                          ) if body_term.ctx_name is not '' else fact
            else:
                operator = body_term.operator.replace(
                    '&', ',').replace('|', ';') + ' '
                fact = operator + \
                    (body_term.terms.join(
                        [body_term.ctx_name+'(', ')']) if body_term.ctx_name is not '' else fact)
                facts += (fact)

        # verificar se a head tem uma variável
        # obter bind entre variavel e retorno do Prolog
        # adicionar em alguma variavel do body o retorno do bind do Prolog
        self.head.bindings = PrologService.verify_terms(
            facts)  # só funciona com contexto logicos
        #[{'X': 'aware', 'Y': 'notifyPedestrian'}]
        return bool(self.head.bindings)

    def get_variable_facts():
        return True


class BodyTerm:  # usar a lista de body term para formar, assumir que essa lista já tá populada

    def __init__(self, ctx_name='', terms='', negation=False) -> None:
        self.ctx_name = ctx_name
        self.terms = terms  # hoje é uma string
        self.negation = negation
        self.operator = ''

    def to_string(self):
        return str(self.negation) + ' ' + self.ctx_name + ': ' + str(self.terms)
