from sigonAgent import AgentDefinition
from sensors.DefaultSensor import DefaultSensor


agent = AgentDefinition('example.on')
agent.run()

read_rensor = DefaultSensor('defaultSensor')
read_rensor.perceive("start")

