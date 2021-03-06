

from sigon.mcs.bridge_rules.head import Head
from posixpath import join
from sigon.prolog.prolog_service import PrologService
# from agent.agent import Agent



class Body:

    body_terms = []
    variables_to_be_added = []

    # NOTE: quando eu usava terms = [], por algum motivo o terms na segunda "iteração" chegava já preenchido
    def __init__(self, head: Head = Head(), terms=None):
        self.body_terms = terms or []
        self.head = head

    def to_string(self):
        return '\n'.join(self.body_terms)

    # NOTE: preciso verificar cada BR como um todo, ideia é montar uma string de verificacao -> inserir numa lista o retorno booleano
    def verify_custom(self, ctxs):

        for body_term in self.body_terms:
            # assert isinstance(bodyTerm, BodyTerm)
            ctx = ctxs[body_term.ctx_name]
            # vai retornar um dict com os bindings {'X': 'aware', 'Y': 'notifyPedestrian'} [{fact: 'resultadoVerify'}]
            result = ctx.verify(body_term.terms)
            # TODO: colocar regras de or, and -> converter para bool
            # TODO: verificar se já não existe um binding, exemplo: X -> aux, aí na proxima iteração, X -> aux2
            # TODO: ir montando string de resultados
            for r in result:
                self.head.bindings.append(r)

        #self.head.bindings = results
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
