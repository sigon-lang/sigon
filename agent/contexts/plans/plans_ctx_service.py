from mcs.bridge_rules.body import Body, BodyTerm
from mcs.bridge_rules.head import Head
from mcs.bridge_rules.bridge_rule import BridgeRule
from agent.contexts.plans.action import Action
from agent.contexts.plans.plan import Plan
from agent.contexts.intentions.intentions_ctx_service import IntentionsContextService
from agent.contexts.beliefs.beliefs_ctx_service import BeliefsContextService
from agent.contexts.communication.communication_ctx_service import CommunicationContextService
from mcs.contexts.ctx_service import ContextService
from prolog.prolog_service import PrologService


class PlansContextService (ContextService):

    _instance = None
    plans = []
    ctx_name = 'planner'
    ctxs = {}
    bindings = []

    @classmethod
    def __init__(cls) -> None:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def has_belief(cls, belief):
        return bool(BeliefsContextService.verify(belief))

    @classmethod
    def has_intention(cls, something_to_be_true):
        return bool(IntentionsContextService.verify(something_to_be_true))

    @classmethod
    def has_precondition(cls, clause):
        pass

    @classmethod
    def check_precondition(cls, plan):
        assert isinstance(plan, Plan)
        cls.bindings = []
        if len(plan.preconditions) == 0:
            return True

        for pC in plan.preconditions:  # dic com beliefs e array de terms
            # pegar pC e consultar no contexto
            terms = plan.preconditions[pC]
            for t in terms:
                if t.startswith('not '):                    
                    cls.bindings.extend(
                        cls.ctxs[pC].verify(t.replace('not', '')))
                    if bool(cls.bindings):
                        return False  # testar essa condicao
                else:
                    cls.bindings.extend(cls.ctxs[pC].verify(t))
                    if not bool(cls.bindings):
                        return False

        return True

    @classmethod
    def has_action_preconditions(cls, action_preconditions):

        for pre_condition in action_preconditions:
            if pre_condition.startswith('not'):
                if cls.has_belief(pre_condition.replace('not', '')):
                    return False

            if not cls.has_belief(pre_condition):
                return False

        return True

    @classmethod
    def find_bindings(cls, arguments):

        variables_bindings = {}
        bindings = []
        variables = arguments.split(',')
        # qual seria a melhor maneira de formar as acoes com base nos bindings retornados?
        for binding in cls.bindings:
            args = arguments
            for var in variables:
                if var[0].isupper():
                    args = args.replace(var, str(binding.get(var, var)))
            bindings.append(args)

        # for var in variables:
        #     if var[0].isupper():                 #obtem a variável com base no valor da primeira posicao
        #         arg = ''
        #         for binding in cls.bindings:
        #             arg = arguments.replace(var, binding.get(var, var))

        #             if var in binding:
        #                 if var not in variables_bindings:
        #                     variables_bindings[var] = [binding[var]]
        #                 else:
        #                     if binding[var] not in variables_bindings[var]:
        #                         variables_bindings[var].append(binding[var])

        #         args.append(arg)

        return bindings

    @classmethod
    def execute_plan_algorithm(cls):

        plans_to_be_executed = list(filter((lambda p: cls.has_intention(p.something_to_be_true)
                                            and cls.check_precondition(p)), cls.plans))
        if plans_to_be_executed:
            p = plans_to_be_executed[0]
            # assert isinstance(p, Plan)
            if p.actions:
                actions_to_be_executed = list(filter((lambda a: cls.has_action_preconditions(
                    action_preconditions=a.pre_conditions)), p.actions))
                if actions_to_be_executed:
                    a = actions_to_be_executed[0]
                    assert isinstance(a, Action)
                    args = a.arguments  # NOTE: verificar pq no sigon em java era uma lista
                    # provavelmente fazer um dict com lista
                    action_bindings = cls.find_bindings(args[0])
                    args = args[0].split(',')
                    #args = re.sub('[\\[\\]]', '', args)
                    if not args:
                        args = '_'
                    facts = []
                    # actions = map(lambda action: 'act(' + a.name +'('+ ','.join(map(str, action)) + '))', action_bindings)

                    # NOTE: com toda a certeza a maneira como foi feito o algoritmo para definir as ações
                    # não é muito bom, complexidade muito alta, porém, como na minha tese esse não era meu foco
                    # acabei por ignorar e usar essa versão
                    for action in action_bindings:
                        act = 'act(' + a.name + '(' + action + '))'                        
                        PlansContextService.append_fact(act) #NOTE é aqui o gargalo
                        # CommunicationContextService.append_fact(a.name + '(' + action + ')')

                    # actions = ['act(' + a.name +'('+ ','.join(map(str, action_bindings)) + '))']
                    # args_size = 1
                    # while args_size < len(args):
                    #     args_size += 1
                    #     for binding in action_bindings:

                    #         binded_actions = []
                    #         for variable in action_bindings[binding]:

                    #             for action in actions:
                    #                 binded_actions.append(action.replace(binding, str(variable))) #NOTE cast para string para evitar problemas

                    #         actions = binded_actions.copy()

                    # fact = 'act(' + a.name +'('+ ','.join(map(str, args)) + '))'
                    # print(actions)
                    # for action in actions:
                    #     PlansContextService.append_fact(action)
                    #     CommunicationContextService.append_fact(action)

                    body_term = BodyTerm('planner', 'act(X)')
                    body_terms = [body_term]
                    communication_head = Head('communication', 'X')
                    communication_head.ctx = cls.ctxs['communication']
                    body = Body(head=communication_head, terms=body_terms)
                    br = BridgeRule(communication_head, body)
                    br.execute()
                    cls.bindings = []
                    # print(br.execute())

    # @classmethod
    # def action_predicate(cls, action): #usada no filtro do algoritmo de planejamento
    #     pass

    @classmethod
    def verify(cls, fact):
        return PrologService.verify_custom(fact, cls.ctx_name)

    @classmethod
    def remove(cls, fact):
        return PrologService.retract(fact, cls.ctx_name)

    @classmethod
    def format_plan_conditions(cls, conditions):

        plan_conditions = []
        for (key, value) in conditions:
            for v in value:
                condition_with_ctx = '%s(%s)' % (key, v)
                plan_conditions.append(condition_with_ctx)

        return str(plan_conditions).translate(str.maketrans({'\'': ''}))

    @classmethod
    def append_facts(cls, plans):

        cls.plans = plans
        fact = ''
        for p in plans:
            assert isinstance(p, Plan)
            precondition_formatted = cls.format_plan_conditions(
                p.preconditions.items())

            if bool(p.posconditions):
                poscondition_formatted = cls.format_plan_conditions(
                    p.posconditions.items())
                # print(poscondition_formatted)
            else:
                poscondition_formatted = '_'

            plan_to_be_added = 'plan(' + p.something_to_be_true + ',_,' + \
                precondition_formatted + ',' + poscondition_formatted + ')'
            # print(plan_to_be_added)
            # TODO: pq nao estou considerando a acao aqui?
            PlansContextService.append_fact(plan_to_be_added)
        # circundar as preconds com o nome do contexto e AND
        # {'beliefs': ['aware(aux)', '(aux:-aux2)'], 'desires': ['notifyPedestrian']} -> beliefs(aware(aux))

        PrologService.verify('plan(X,Y,Z,W)', cls.ctx_name)

    @classmethod
    def append_fact(cls, fact):
        if not PrologService.verify(fact, cls.ctx_name):
            PrologService.append_fact(fact, cls.ctx_name)

    # @classmethod
    # def addBeliefs(cls, facts): #acho que esse metodo nao rola mais, pq mudou muito a maneira como trata a string
    #     if len(cls.beliefs) == 0 :
    #         cls.beliefs = facts
    #     else:
    #         for b in facts:
    #             cls.beliefs.append(b)
    #     PrologService.appendFacts(facts, cls.ctxName)
