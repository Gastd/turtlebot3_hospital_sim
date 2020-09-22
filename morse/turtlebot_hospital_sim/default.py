#! /usr/bin/env morseexec

# Morse simulation for hospital with a turtlebot
# Run with morse run turtlebot_hospital_sim after starting ros with roscore

from morse.builder import *
from turtlebot_hospital_sim.Turtlebot import Turtlebot


PATH = "/".join(__file__.split("/")[:-1])

robot1 = Turtlebot(name='turtlebot1')
robot1.add_to_simulation()

# Clock
clock = Clock()
robot1.append(clock)
clock.add_interface('ros', topic="/clock")

robot2 = Turtlebot(name='turtlebot2')
robot2.add_to_simulation(x=-25)

# Charging Zone
charging_zone = Zone(type='Charging')
charging_zone.size=[5 for x in range(3)]
charging_zone.translate(x=-19, y=-3, z=0)

# set 'fastmode' to True to switch to wireframe mode
env = Environment(f'{PATH}/models/cic.blend', fastmode=False)
env.set_horizon_color(color=(0.65, 0.65, 0.65))
env.set_camera_location([-30.0, -10, 5.0])
env.set_camera_rotation([1.09, 0, -0.7])
