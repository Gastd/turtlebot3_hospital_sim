#! /usr/bin/env morseexec

# Morse simulation for hospital with a turtlebot
# Run with morse run turtlebot_hospital_sim after starting ros with roscore

from morse.builder import *
from turtlebot_hospital_sim.Turtlebot import Turtlebot

PATH = "/".join(__file__.split("/")[:-1])

robot = Turtlebot()
robot.add_to_simulation()

robot2 = Turtlebot(name='turtlebot2')
robot2.add_to_simulation(x=-25)

# set 'fastmode' to True to switch to wireframe mode
env = Environment(f'{PATH}/models/cic.blend', fastmode=False)
env.set_horizon_color(color=(0.65, 0.65, 0.65))
env.set_camera_location([-30.0, -10, 5.0])
env.set_camera_rotation([1.09, 0, -0.7])
