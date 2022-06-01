# Generated from Agent.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AgentParser import AgentParser
else:
    from AgentParser import AgentParser

# This class defines a complete generic visitor for a parse tree produced by AgentParser.

class AgentVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AgentParser#agent.
    def visitAgent(self, ctx:AgentParser.AgentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#context.
    def visitContext(self, ctx:AgentParser.ContextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#bridgeRule.
    def visitBridgeRule(self, ctx:AgentParser.BridgeRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#logicalContext.
    def visitLogicalContext(self, ctx:AgentParser.LogicalContextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#functionalContext.
    def visitFunctionalContext(self, ctx:AgentParser.FunctionalContextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#communicationContext.
    def visitCommunicationContext(self, ctx:AgentParser.CommunicationContextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#plannerContext.
    def visitPlannerContext(self, ctx:AgentParser.PlannerContextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#customFunctionalContext.
    def visitCustomFunctionalContext(self, ctx:AgentParser.CustomFunctionalContextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#logicalContextName.
    def visitLogicalContextName(self, ctx:AgentParser.LogicalContextNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#primitiveContextName.
    def visitPrimitiveContextName(self, ctx:AgentParser.PrimitiveContextNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#customLogicalContextName.
    def visitCustomLogicalContextName(self, ctx:AgentParser.CustomLogicalContextNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#plan.
    def visitPlan(self, ctx:AgentParser.PlanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#somethingToBeTrue.
    def visitSomethingToBeTrue(self, ctx:AgentParser.SomethingToBeTrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#preConditions.
    def visitPreConditions(self, ctx:AgentParser.PreConditionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#postConditions.
    def visitPostConditions(self, ctx:AgentParser.PostConditionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#planConditions.
    def visitPlanConditions(self, ctx:AgentParser.PlanConditionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#condition.
    def visitCondition(self, ctx:AgentParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#conditionTerm.
    def visitConditionTerm(self, ctx:AgentParser.ConditionTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#planPostconditions.
    def visitPlanPostconditions(self, ctx:AgentParser.PlanPostconditionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#contextReference.
    def visitContextReference(self, ctx:AgentParser.ContextReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#conditions.
    def visitConditions(self, ctx:AgentParser.ConditionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#conditions1.
    def visitConditions1(self, ctx:AgentParser.Conditions1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#action.
    def visitAction(self, ctx:AgentParser.ActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#actionPreconditions.
    def visitActionPreconditions(self, ctx:AgentParser.ActionPreconditionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#actionPostconditions.
    def visitActionPostconditions(self, ctx:AgentParser.ActionPostconditionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#functionInvocation.
    def visitFunctionInvocation(self, ctx:AgentParser.FunctionInvocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#functionName.
    def visitFunctionName(self, ctx:AgentParser.FunctionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#sensor.
    def visitSensor(self, ctx:AgentParser.SensorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#sensorIdentifier.
    def visitSensorIdentifier(self, ctx:AgentParser.SensorIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#sensorImplementation.
    def visitSensorImplementation(self, ctx:AgentParser.SensorImplementationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#actuator.
    def visitActuator(self, ctx:AgentParser.ActuatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#actuatorIdentifier.
    def visitActuatorIdentifier(self, ctx:AgentParser.ActuatorIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#actuatorImplementation.
    def visitActuatorImplementation(self, ctx:AgentParser.ActuatorImplementationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#internalOperator.
    def visitInternalOperator(self, ctx:AgentParser.InternalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#beliefAdition.
    def visitBeliefAdition(self, ctx:AgentParser.BeliefAditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#beliefRemotion.
    def visitBeliefRemotion(self, ctx:AgentParser.BeliefRemotionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#desireAdition.
    def visitDesireAdition(self, ctx:AgentParser.DesireAditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#desireRemotion.
    def visitDesireRemotion(self, ctx:AgentParser.DesireRemotionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#argumentList.
    def visitArgumentList(self, ctx:AgentParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#expression.
    def visitExpression(self, ctx:AgentParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#compoundAction.
    def visitCompoundAction(self, ctx:AgentParser.CompoundActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#plansFormulas.
    def visitPlansFormulas(self, ctx:AgentParser.PlansFormulasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#contextName.
    def visitContextName(self, ctx:AgentParser.ContextNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#head.
    def visitHead(self, ctx:AgentParser.HeadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#body.
    def visitBody(self, ctx:AgentParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#otherBodyRules.
    def visitOtherBodyRules(self, ctx:AgentParser.OtherBodyRulesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#bodyTerm.
    def visitBodyTerm(self, ctx:AgentParser.BodyTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#logicalOperator.
    def visitLogicalOperator(self, ctx:AgentParser.LogicalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#term.
    def visitTerm(self, ctx:AgentParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#term2.
    def visitTerm2(self, ctx:AgentParser.Term2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#formulas.
    def visitFormulas(self, ctx:AgentParser.FormulasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#atom.
    def visitAtom(self, ctx:AgentParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#operator.
    def visitOperator(self, ctx:AgentParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#negation.
    def visitNegation(self, ctx:AgentParser.NegationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#annotation.
    def visitAnnotation(self, ctx:AgentParser.AnnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#preAction.
    def visitPreAction(self, ctx:AgentParser.PreActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#gradedValue.
    def visitGradedValue(self, ctx:AgentParser.GradedValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentParser#cost.
    def visitCost(self, ctx:AgentParser.CostContext):
        return self.visitChildren(ctx)



del AgentParser