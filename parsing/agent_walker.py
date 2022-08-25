from mcs.bridge_rules.bridge_rule import BridgeRule
from mcs.bridge_rules.body import Body, BodyTerm
from mcs.bridge_rules.head import Head
from parsing.languages.lang_sensor import LangSensor
from parsing.languages.lang_actuator import LangActuator
from grammar.AgentListener import AgentListener
from grammar.AgentParser import AgentParser
from parsing.languages.lang_ctx import LangContext
from agent.contexts.plans.plan import Plan
from agent.contexts.plans.action import Action


class AgentWalker(AgentListener):

    def __init__(self):
        self.plans = []
        self.plan = Plan()

        self.lang_contexts = []
        self.lang_actuators = []
        self.lang_sensors = []
        self.bridge_rules = []
        self.pre_conditions = {}
        self.pos_conditions = {}

        self.last_actuator = LangActuator()
        self.last_sensor = LangSensor()
        self.last_head = Head()
        self.last_body = Body()

    # DISCLAIMER: It was ANTLR that did not follow pep8 conventions

    def enterActuator(self, ctx: AgentParser.ActuatorContext):
        return super().enterActuator(ctx)

    def enterActuatorIdentifier(self, ctx: AgentParser.ActuatorIdentifierContext):
        self.last_actuator.identifier = ctx.getText().replace('\"', '')
        return super().enterActuatorIdentifier(ctx)

    def enterActuatorImplementation(self, ctx: AgentParser.ActuatorImplementationContext):
        self.last_actuator.implementation = ctx.getText().replace('\"', '')
        self.lang_actuators.append(self.last_actuator)
        return super().enterActuatorImplementation(ctx)

    def enterSensor(self, ctx: AgentParser.SensorContext):
        return super().enterSensor(ctx)

    def enterSensorIdentifier(self, ctx: AgentParser.SensorIdentifierContext):
        self.last_sensor.identifier = ctx.getText().replace('\"', '')

        return super().enterSensorIdentifier(ctx)

    def enterSensorImplementation(self, ctx: AgentParser.SensorImplementationContext):
        self.last_sensor.implementation = ctx.getText().replace('\"', '')
        self.lang_sensors.append(LangSensor(self.last_sensor.identifier, self.last_sensor.implementation))
        return super().enterSensorImplementation(ctx)

    def enterLogicalContext(self, ctx: AgentParser.LogicalContextContext):
        lCxt = LangContext(ctx.logicalContextName().getText(), clauses=[])
        for t in ctx.formulas().term():
            lCxt.clauses.append(t.getText())

        super().enterLogicalContext(ctx)
        self.lang_contexts.append(lCxt)

    def enterBridgeRule(self, ctx: AgentParser.BridgeRuleContext):
        self.bridge_rules.append(ctx)
        return super().enterBridgeRule(ctx)

    def enterSomethingToBeTrue(self, ctx: AgentParser.SomethingToBeTrueContext):
        self.plan = Plan()
        self.plan.something_to_be_true = ctx.getText()
        self.plans.append(self.plan)
        return super().enterSomethingToBeTrue(ctx)

    def enterPreConditions(self, ctx: AgentParser.PreConditionsContext):
        pre_condition = {}
        for cond in ctx.planConditions().condition():
            # NOTE: I replaced '_' to avoid problems with prolog parsing
            current_context = cond.contextReference().getText().replace('_', '')

            pre_condition.setdefault(current_context, [])
            pre_condition[current_context].append(
                cond.conditionTerm().getText())

        self.plan.preconditions = pre_condition
        return super().enterPreConditions(ctx)

    def enterPostConditions(self, ctx: AgentParser.PostConditionsContext):
        pos_condition = {}
        for cond in ctx.planConditions().condition():
            currentContext = cond.contextReference().getText()
            pos_condition.setdefault(currentContext, [])
            pos_condition[currentContext].append(
                cond.conditionTerm().getText())

        self.plan.posconditions = pos_condition
        return super().enterPostConditions(ctx)

    def enterFunctionName(self, ctx: AgentParser.FunctionNameContext):
        self.action = Action(ctx.getText())
        self.plan.actions.append(self.action)
        return super().enterFunctionName(ctx)

    def enterArgumentList(self, ctx: AgentParser.ArgumentListContext):
        self.action.arguments.append(ctx.getText())
        return super().enterArgumentList(ctx)

    def enterActionPreconditions(self, ctx: AgentParser.ActionPreconditionsContext):
        self.action.pre_conditions.append(ctx.getText())
        return super().enterActionPreconditions(ctx)

    def enterActionPostconditions(self, ctx: AgentParser.ActionPostconditionsContext):
        self.action.pos_conditions.append(ctx.getText())
        return super().enterActionPostconditions(ctx)

    def enterBridgeRule(self, ctx: AgentParser.BridgeRuleContext):
        return super().enterBridgeRule(ctx)

    # TODO execute test with negation and variable
    def enterHead(self, ctx: AgentParser.HeadContext):
        self.last_head = Head()
        self.last_head.ctxNegation = False if not ctx.negation() else True
        self.last_head.ctxName = ctx.contextName().getText().replace(
            '_', '')  # replace to avoid problems with prolog parsing

        self.last_head.clause = ctx.term().getText(
        ) if not ctx.VARIABLE() else ctx.VARIABLE().getText()

        return super().enterHead(ctx)

    def enterBody(self, ctx: AgentParser.BodyContext):
        self.last_body = Body()
        current_body_rule_term = BodyTerm()

        current_body_rule_term.negation = True if ctx.negation() is not None else False
        current_body_rule_term.ctx_name = ctx.contextName().getText().replace(
            '_', '')  # replace to avoid problems with prolog parsing
        # NOTE: I think here we should have spĺit with & and |
        current_body_rule_term.terms = ctx.bodyTerm().getText()
        self.last_body.body_terms.append(current_body_rule_term)
        if ctx.otherBodyRules() is not None:
            for idx, ctxName in enumerate(ctx.otherBodyRules().contextName()):
                other_body_rule_term = BodyTerm()
                other_body_rule_term.ctx_name = ctxName.getText()
                other_body_rule_term.negation = True if ctx.otherBodyRules().negation(
                    idx) is not None else False
                # otherBodyRuleTerm.bodyTerms = ctx.otherBodyRules().bodyTerm(idx).getText()
                other_body_rule_term.terms = ctx.otherBodyRules().bodyTerm(idx).getText()
                operator = ctx.otherBodyRules().logicalOperator(idx).getText(
                ) if ctx.otherBodyRules().logicalOperator(idx) is not None else ''
                # if operator == '&':
                #     otherBodyRuleTerm.operator = ','
                # elif operator == '|':
                #     otherBodyRuleTerm.operator = ';'
                # else:
                #     otherBodyRuleTerm.operator = ''
                other_body_rule_term.operator = ',' if operator == '&' else ';' if operator == '' else ''
                self.last_body.body_terms.append(other_body_rule_term)

        self.bridge_rules.append(BridgeRule(self.last_head, self.last_body))

        return super().enterBody(ctx)
