#!/usr/bin/env python

import sys
import rospy
import math
import numpy as np
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from turtlesim.msg import Pose as TurtlePose
from tf.transformations import euler_from_quaternion
from std_msgs.msg import Float64

def upload(msg):
	pass

if __name__ == '__main__':
	# initializes node
	rospy.init_node("hospital_broker", anonymous=False)
	# starts subscribers and publishers
	rospy.Subscriber("/R1/vital_signal", String, upload)
	print('subscribers on!')
	signal_pub = rospy.Publisher("/hospital/vital_signal", String, queue_size=10)
	# aramis_athos = rospy.Publisher("/aramis_athos", Float64, queue_size=10)
	# athos_porthos = rospy.Publisher("/athos_porthos", Float64, queue_size=10)
	# porthos_aramis = rospy.Publisher("/porthos_aramis", Float64, queue_size=10)
	# print('publishers on!')

	rate = rospy.Rate(10)

	signal = String()
	signal.data = "Its alive!"

	while not rospy.is_shutdown():

		signal_pub.publish(signal)

		rate.sleep()
