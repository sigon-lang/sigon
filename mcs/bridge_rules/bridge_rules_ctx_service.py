

from mcs import bridge_rules
from mcs.bridge_rules import bridge_rule
from mcs.bridge_rules.bridge_rule import BridgeRule
from mcs.bridge_rules.head import Head
from mcs.bridge_rules.body import Body, BodyTerm


class BridgeRulesContextService():
    bridge_rules = []
    ctxs = {}


    @classmethod
    def execute_bridge_rules(cls):
        for br in cls.bridge_rules:  
            assert isinstance(br, BridgeRule)          
            br.head.ctx = cls.ctxs[br.head.ctxName]
            br.head.bindings = [] #talvez aqui tenha o bug da inicializacao
            br.execute_custom(cls.ctxs)
            #print("Result of BR",  br.head.ctx, br.execute_custom(cls.ctxs))

    @classmethod
    def execute_BDI_rules(cls):
        communication_body_term = BodyTerm('communication', 'sense(X)') #NOTE implementacao do sensor "default" deve adicionar sense(X) com o uso do prolog
        plan_body_term = BodyTerm('planner', 'plan(Y,_,Z,_)')
        plan_body_term.operator = '&'
        plan_body_terms_member = BodyTerm('', 'member(beliefs(X),Z)') # como generalizar para outros casos?
        plan_body_terms_member.operator = '&'
        desire_body_term = BodyTerm('desires', 'Y')
        desire_body_term.operator = '&'
        body_terms  = []
        body_terms.append(communication_body_term)
        body_terms.append(plan_body_term)
        body_terms.append(plan_body_terms_member)
        body_terms.append(desire_body_term)

        belief_head = Head('beliefs', 'X')
        belief_head.ctx = cls.ctxs.get('beliefs')
        body = Body(head=belief_head, terms=body_terms)

        br = BridgeRule(belief_head, body)
        r = br.execute()
        
        
    

        

