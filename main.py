from sigonAgent import AgentDefinition
from sensors.DefaultSensor import DefaultSensor


agent = AgentDefinition('example.on')
agent.run()

read_sensor = DefaultSensor('defaultSensor')
read_sensor.perceive("start")

