from sensors.DefaultSensor import DefaultSensor
from agent.agent import Agent
import sys
from antlr4 import *
from grammar.AgentLexer import AgentLexer
from grammar.AgentParser import AgentParser
from parsing.agent_walker import AgentWalker
from agent.contexts.beliefs.beliefs_ctx_service import BeliefsContextService
from pyswip import *
from agent.contexts.plans import plan, action, plans_ctx_service
from mcs.bridge_rules import *


class AgentDefinition:

    def __init__(self, file: str, contexts = [], sensors = [], encoding='utf-8'):
        input_stream = FileStream(
        file, encoding=encoding)
        lexer = AgentLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = AgentParser(stream)

        tree = parser.agent()
        self.agent_walker = AgentWalker()
        walker = ParseTreeWalker()

        walker.walk(self.agent_walker, tree)
        self.agent = Agent(custom_ctxs=contexts, sensors=sensors)        

    def run(self):
        self.agent.run(self.agent_walker)    

    
  

