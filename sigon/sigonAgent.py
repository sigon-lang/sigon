from sigon.sensors.DefaultSensor import DefaultSensor
from sigon.agent.agent import Agent
import sys
from antlr4 import *
from sigon.grammar.AgentLexer import AgentLexer
from sigon.grammar.AgentParser import AgentParser
from sigon.parsing.agent_walker import AgentWalker
from sigon.agent.contexts.beliefs.beliefs_ctx_service import BeliefsContextService
from sigon.agent.contexts.plans import plan, action, plans_ctx_service



class AgentDefinition:

    def __init__(self, file: str, contexts = [], encoding='utf-8'):
        input_stream = FileStream(
        file, encoding=encoding)
        lexer = AgentLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = AgentParser(stream)

        tree = parser.agent()
        self.agent_walker = AgentWalker()
        walker = ParseTreeWalker()

        walker.walk(self.agent_walker, tree)
        self.agent = Agent(custom_ctxs=contexts)        

    def run(self):
        self.agent.run(self.agent_walker)    
  

