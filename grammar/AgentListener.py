# Generated from Agent.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AgentParser import AgentParser
else:
    from AgentParser import AgentParser

# This class defines a complete listener for a parse tree produced by AgentParser.
class AgentListener(ParseTreeListener):

    # Enter a parse tree produced by AgentParser#agent.
    def enterAgent(self, ctx:AgentParser.AgentContext):
        pass

    # Exit a parse tree produced by AgentParser#agent.
    def exitAgent(self, ctx:AgentParser.AgentContext):
        pass


    # Enter a parse tree produced by AgentParser#context.
    def enterContext(self, ctx:AgentParser.ContextContext):
        pass

    # Exit a parse tree produced by AgentParser#context.
    def exitContext(self, ctx:AgentParser.ContextContext):
        pass


    # Enter a parse tree produced by AgentParser#bridgeRule.
    def enterBridgeRule(self, ctx:AgentParser.BridgeRuleContext):
        pass

    # Exit a parse tree produced by AgentParser#bridgeRule.
    def exitBridgeRule(self, ctx:AgentParser.BridgeRuleContext):
        pass


    # Enter a parse tree produced by AgentParser#logicalContext.
    def enterLogicalContext(self, ctx:AgentParser.LogicalContextContext):
        pass

    # Exit a parse tree produced by AgentParser#logicalContext.
    def exitLogicalContext(self, ctx:AgentParser.LogicalContextContext):
        pass


    # Enter a parse tree produced by AgentParser#functionalContext.
    def enterFunctionalContext(self, ctx:AgentParser.FunctionalContextContext):
        pass

    # Exit a parse tree produced by AgentParser#functionalContext.
    def exitFunctionalContext(self, ctx:AgentParser.FunctionalContextContext):
        pass


    # Enter a parse tree produced by AgentParser#communicationContext.
    def enterCommunicationContext(self, ctx:AgentParser.CommunicationContextContext):
        pass

    # Exit a parse tree produced by AgentParser#communicationContext.
    def exitCommunicationContext(self, ctx:AgentParser.CommunicationContextContext):
        pass


    # Enter a parse tree produced by AgentParser#plannerContext.
    def enterPlannerContext(self, ctx:AgentParser.PlannerContextContext):
        pass

    # Exit a parse tree produced by AgentParser#plannerContext.
    def exitPlannerContext(self, ctx:AgentParser.PlannerContextContext):
        pass


    # Enter a parse tree produced by AgentParser#customFunctionalContext.
    def enterCustomFunctionalContext(self, ctx:AgentParser.CustomFunctionalContextContext):
        pass

    # Exit a parse tree produced by AgentParser#customFunctionalContext.
    def exitCustomFunctionalContext(self, ctx:AgentParser.CustomFunctionalContextContext):
        pass


    # Enter a parse tree produced by AgentParser#logicalContextName.
    def enterLogicalContextName(self, ctx:AgentParser.LogicalContextNameContext):
        pass

    # Exit a parse tree produced by AgentParser#logicalContextName.
    def exitLogicalContextName(self, ctx:AgentParser.LogicalContextNameContext):
        pass


    # Enter a parse tree produced by AgentParser#primitiveContextName.
    def enterPrimitiveContextName(self, ctx:AgentParser.PrimitiveContextNameContext):
        pass

    # Exit a parse tree produced by AgentParser#primitiveContextName.
    def exitPrimitiveContextName(self, ctx:AgentParser.PrimitiveContextNameContext):
        pass


    # Enter a parse tree produced by AgentParser#customLogicalContextName.
    def enterCustomLogicalContextName(self, ctx:AgentParser.CustomLogicalContextNameContext):
        pass

    # Exit a parse tree produced by AgentParser#customLogicalContextName.
    def exitCustomLogicalContextName(self, ctx:AgentParser.CustomLogicalContextNameContext):
        pass


    # Enter a parse tree produced by AgentParser#plan.
    def enterPlan(self, ctx:AgentParser.PlanContext):
        pass

    # Exit a parse tree produced by AgentParser#plan.
    def exitPlan(self, ctx:AgentParser.PlanContext):
        pass


    # Enter a parse tree produced by AgentParser#somethingToBeTrue.
    def enterSomethingToBeTrue(self, ctx:AgentParser.SomethingToBeTrueContext):
        pass

    # Exit a parse tree produced by AgentParser#somethingToBeTrue.
    def exitSomethingToBeTrue(self, ctx:AgentParser.SomethingToBeTrueContext):
        pass


    # Enter a parse tree produced by AgentParser#preConditions.
    def enterPreConditions(self, ctx:AgentParser.PreConditionsContext):
        pass

    # Exit a parse tree produced by AgentParser#preConditions.
    def exitPreConditions(self, ctx:AgentParser.PreConditionsContext):
        pass


    # Enter a parse tree produced by AgentParser#postConditions.
    def enterPostConditions(self, ctx:AgentParser.PostConditionsContext):
        pass

    # Exit a parse tree produced by AgentParser#postConditions.
    def exitPostConditions(self, ctx:AgentParser.PostConditionsContext):
        pass


    # Enter a parse tree produced by AgentParser#planConditions.
    def enterPlanConditions(self, ctx:AgentParser.PlanConditionsContext):
        pass

    # Exit a parse tree produced by AgentParser#planConditions.
    def exitPlanConditions(self, ctx:AgentParser.PlanConditionsContext):
        pass


    # Enter a parse tree produced by AgentParser#condition.
    def enterCondition(self, ctx:AgentParser.ConditionContext):
        pass

    # Exit a parse tree produced by AgentParser#condition.
    def exitCondition(self, ctx:AgentParser.ConditionContext):
        pass


    # Enter a parse tree produced by AgentParser#conditionTerm.
    def enterConditionTerm(self, ctx:AgentParser.ConditionTermContext):
        pass

    # Exit a parse tree produced by AgentParser#conditionTerm.
    def exitConditionTerm(self, ctx:AgentParser.ConditionTermContext):
        pass


    # Enter a parse tree produced by AgentParser#planPostconditions.
    def enterPlanPostconditions(self, ctx:AgentParser.PlanPostconditionsContext):
        pass

    # Exit a parse tree produced by AgentParser#planPostconditions.
    def exitPlanPostconditions(self, ctx:AgentParser.PlanPostconditionsContext):
        pass


    # Enter a parse tree produced by AgentParser#contextReference.
    def enterContextReference(self, ctx:AgentParser.ContextReferenceContext):
        pass

    # Exit a parse tree produced by AgentParser#contextReference.
    def exitContextReference(self, ctx:AgentParser.ContextReferenceContext):
        pass


    # Enter a parse tree produced by AgentParser#conditions.
    def enterConditions(self, ctx:AgentParser.ConditionsContext):
        pass

    # Exit a parse tree produced by AgentParser#conditions.
    def exitConditions(self, ctx:AgentParser.ConditionsContext):
        pass


    # Enter a parse tree produced by AgentParser#conditions1.
    def enterConditions1(self, ctx:AgentParser.Conditions1Context):
        pass

    # Exit a parse tree produced by AgentParser#conditions1.
    def exitConditions1(self, ctx:AgentParser.Conditions1Context):
        pass


    # Enter a parse tree produced by AgentParser#action.
    def enterAction(self, ctx:AgentParser.ActionContext):
        pass

    # Exit a parse tree produced by AgentParser#action.
    def exitAction(self, ctx:AgentParser.ActionContext):
        pass


    # Enter a parse tree produced by AgentParser#actionPreconditions.
    def enterActionPreconditions(self, ctx:AgentParser.ActionPreconditionsContext):
        pass

    # Exit a parse tree produced by AgentParser#actionPreconditions.
    def exitActionPreconditions(self, ctx:AgentParser.ActionPreconditionsContext):
        pass


    # Enter a parse tree produced by AgentParser#actionPostconditions.
    def enterActionPostconditions(self, ctx:AgentParser.ActionPostconditionsContext):
        pass

    # Exit a parse tree produced by AgentParser#actionPostconditions.
    def exitActionPostconditions(self, ctx:AgentParser.ActionPostconditionsContext):
        pass


    # Enter a parse tree produced by AgentParser#functionInvocation.
    def enterFunctionInvocation(self, ctx:AgentParser.FunctionInvocationContext):
        pass

    # Exit a parse tree produced by AgentParser#functionInvocation.
    def exitFunctionInvocation(self, ctx:AgentParser.FunctionInvocationContext):
        pass


    # Enter a parse tree produced by AgentParser#functionName.
    def enterFunctionName(self, ctx:AgentParser.FunctionNameContext):
        pass

    # Exit a parse tree produced by AgentParser#functionName.
    def exitFunctionName(self, ctx:AgentParser.FunctionNameContext):
        pass


    # Enter a parse tree produced by AgentParser#sensor.
    def enterSensor(self, ctx:AgentParser.SensorContext):
        pass

    # Exit a parse tree produced by AgentParser#sensor.
    def exitSensor(self, ctx:AgentParser.SensorContext):
        pass


    # Enter a parse tree produced by AgentParser#sensorIdentifier.
    def enterSensorIdentifier(self, ctx:AgentParser.SensorIdentifierContext):
        pass

    # Exit a parse tree produced by AgentParser#sensorIdentifier.
    def exitSensorIdentifier(self, ctx:AgentParser.SensorIdentifierContext):
        pass


    # Enter a parse tree produced by AgentParser#sensorImplementation.
    def enterSensorImplementation(self, ctx:AgentParser.SensorImplementationContext):
        pass

    # Exit a parse tree produced by AgentParser#sensorImplementation.
    def exitSensorImplementation(self, ctx:AgentParser.SensorImplementationContext):
        pass


    # Enter a parse tree produced by AgentParser#actuator.
    def enterActuator(self, ctx:AgentParser.ActuatorContext):
        pass

    # Exit a parse tree produced by AgentParser#actuator.
    def exitActuator(self, ctx:AgentParser.ActuatorContext):
        pass


    # Enter a parse tree produced by AgentParser#actuatorIdentifier.
    def enterActuatorIdentifier(self, ctx:AgentParser.ActuatorIdentifierContext):
        pass

    # Exit a parse tree produced by AgentParser#actuatorIdentifier.
    def exitActuatorIdentifier(self, ctx:AgentParser.ActuatorIdentifierContext):
        pass


    # Enter a parse tree produced by AgentParser#actuatorImplementation.
    def enterActuatorImplementation(self, ctx:AgentParser.ActuatorImplementationContext):
        pass

    # Exit a parse tree produced by AgentParser#actuatorImplementation.
    def exitActuatorImplementation(self, ctx:AgentParser.ActuatorImplementationContext):
        pass


    # Enter a parse tree produced by AgentParser#internalOperator.
    def enterInternalOperator(self, ctx:AgentParser.InternalOperatorContext):
        pass

    # Exit a parse tree produced by AgentParser#internalOperator.
    def exitInternalOperator(self, ctx:AgentParser.InternalOperatorContext):
        pass


    # Enter a parse tree produced by AgentParser#beliefAdition.
    def enterBeliefAdition(self, ctx:AgentParser.BeliefAditionContext):
        pass

    # Exit a parse tree produced by AgentParser#beliefAdition.
    def exitBeliefAdition(self, ctx:AgentParser.BeliefAditionContext):
        pass


    # Enter a parse tree produced by AgentParser#beliefRemotion.
    def enterBeliefRemotion(self, ctx:AgentParser.BeliefRemotionContext):
        pass

    # Exit a parse tree produced by AgentParser#beliefRemotion.
    def exitBeliefRemotion(self, ctx:AgentParser.BeliefRemotionContext):
        pass


    # Enter a parse tree produced by AgentParser#desireAdition.
    def enterDesireAdition(self, ctx:AgentParser.DesireAditionContext):
        pass

    # Exit a parse tree produced by AgentParser#desireAdition.
    def exitDesireAdition(self, ctx:AgentParser.DesireAditionContext):
        pass


    # Enter a parse tree produced by AgentParser#desireRemotion.
    def enterDesireRemotion(self, ctx:AgentParser.DesireRemotionContext):
        pass

    # Exit a parse tree produced by AgentParser#desireRemotion.
    def exitDesireRemotion(self, ctx:AgentParser.DesireRemotionContext):
        pass


    # Enter a parse tree produced by AgentParser#argumentList.
    def enterArgumentList(self, ctx:AgentParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by AgentParser#argumentList.
    def exitArgumentList(self, ctx:AgentParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by AgentParser#expression.
    def enterExpression(self, ctx:AgentParser.ExpressionContext):
        pass

    # Exit a parse tree produced by AgentParser#expression.
    def exitExpression(self, ctx:AgentParser.ExpressionContext):
        pass


    # Enter a parse tree produced by AgentParser#compoundAction.
    def enterCompoundAction(self, ctx:AgentParser.CompoundActionContext):
        pass

    # Exit a parse tree produced by AgentParser#compoundAction.
    def exitCompoundAction(self, ctx:AgentParser.CompoundActionContext):
        pass


    # Enter a parse tree produced by AgentParser#plansFormulas.
    def enterPlansFormulas(self, ctx:AgentParser.PlansFormulasContext):
        pass

    # Exit a parse tree produced by AgentParser#plansFormulas.
    def exitPlansFormulas(self, ctx:AgentParser.PlansFormulasContext):
        pass


    # Enter a parse tree produced by AgentParser#contextName.
    def enterContextName(self, ctx:AgentParser.ContextNameContext):
        pass

    # Exit a parse tree produced by AgentParser#contextName.
    def exitContextName(self, ctx:AgentParser.ContextNameContext):
        pass


    # Enter a parse tree produced by AgentParser#head.
    def enterHead(self, ctx:AgentParser.HeadContext):
        pass

    # Exit a parse tree produced by AgentParser#head.
    def exitHead(self, ctx:AgentParser.HeadContext):
        pass


    # Enter a parse tree produced by AgentParser#body.
    def enterBody(self, ctx:AgentParser.BodyContext):
        pass

    # Exit a parse tree produced by AgentParser#body.
    def exitBody(self, ctx:AgentParser.BodyContext):
        pass


    # Enter a parse tree produced by AgentParser#otherBodyRules.
    def enterOtherBodyRules(self, ctx:AgentParser.OtherBodyRulesContext):
        pass

    # Exit a parse tree produced by AgentParser#otherBodyRules.
    def exitOtherBodyRules(self, ctx:AgentParser.OtherBodyRulesContext):
        pass


    # Enter a parse tree produced by AgentParser#bodyTerm.
    def enterBodyTerm(self, ctx:AgentParser.BodyTermContext):
        pass

    # Exit a parse tree produced by AgentParser#bodyTerm.
    def exitBodyTerm(self, ctx:AgentParser.BodyTermContext):
        pass


    # Enter a parse tree produced by AgentParser#logicalOperator.
    def enterLogicalOperator(self, ctx:AgentParser.LogicalOperatorContext):
        pass

    # Exit a parse tree produced by AgentParser#logicalOperator.
    def exitLogicalOperator(self, ctx:AgentParser.LogicalOperatorContext):
        pass


    # Enter a parse tree produced by AgentParser#term.
    def enterTerm(self, ctx:AgentParser.TermContext):
        pass

    # Exit a parse tree produced by AgentParser#term.
    def exitTerm(self, ctx:AgentParser.TermContext):
        pass


    # Enter a parse tree produced by AgentParser#term2.
    def enterTerm2(self, ctx:AgentParser.Term2Context):
        pass

    # Exit a parse tree produced by AgentParser#term2.
    def exitTerm2(self, ctx:AgentParser.Term2Context):
        pass


    # Enter a parse tree produced by AgentParser#formulas.
    def enterFormulas(self, ctx:AgentParser.FormulasContext):
        pass

    # Exit a parse tree produced by AgentParser#formulas.
    def exitFormulas(self, ctx:AgentParser.FormulasContext):
        pass


    # Enter a parse tree produced by AgentParser#atom.
    def enterAtom(self, ctx:AgentParser.AtomContext):
        pass

    # Exit a parse tree produced by AgentParser#atom.
    def exitAtom(self, ctx:AgentParser.AtomContext):
        pass


    # Enter a parse tree produced by AgentParser#operator.
    def enterOperator(self, ctx:AgentParser.OperatorContext):
        pass

    # Exit a parse tree produced by AgentParser#operator.
    def exitOperator(self, ctx:AgentParser.OperatorContext):
        pass


    # Enter a parse tree produced by AgentParser#negation.
    def enterNegation(self, ctx:AgentParser.NegationContext):
        pass

    # Exit a parse tree produced by AgentParser#negation.
    def exitNegation(self, ctx:AgentParser.NegationContext):
        pass


    # Enter a parse tree produced by AgentParser#annotation.
    def enterAnnotation(self, ctx:AgentParser.AnnotationContext):
        pass

    # Exit a parse tree produced by AgentParser#annotation.
    def exitAnnotation(self, ctx:AgentParser.AnnotationContext):
        pass


    # Enter a parse tree produced by AgentParser#preAction.
    def enterPreAction(self, ctx:AgentParser.PreActionContext):
        pass

    # Exit a parse tree produced by AgentParser#preAction.
    def exitPreAction(self, ctx:AgentParser.PreActionContext):
        pass


    # Enter a parse tree produced by AgentParser#gradedValue.
    def enterGradedValue(self, ctx:AgentParser.GradedValueContext):
        pass

    # Exit a parse tree produced by AgentParser#gradedValue.
    def exitGradedValue(self, ctx:AgentParser.GradedValueContext):
        pass


    # Enter a parse tree produced by AgentParser#cost.
    def enterCost(self, ctx:AgentParser.CostContext):
        pass

    # Exit a parse tree produced by AgentParser#cost.
    def exitCost(self, ctx:AgentParser.CostContext):
        pass


