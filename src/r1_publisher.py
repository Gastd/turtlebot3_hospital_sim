#!/usr/bin/env python

import sys
import rospy
import math
import numpy as np
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from std_msgs.msg import String
from std_msgs.msg import Bool
from sensor_msgs.msg import BatteryState
from turtlesim.msg import Pose as TurtlePose
from tf.transformations import euler_from_quaternion

def upload(msg):
	pass

if __name__ == '__main__':

	# initializes node
	rospy.init_node("r1_publisher", anonymous=False)
	# starts subscribers and publishers
	rospy.Subscriber("/hospital/vital_signal", String, upload)
	# rospy.Subscriber("/aramis/pose", Odometry, update_pose1)
	print('subscribers on!')
	speaker_pub = rospy.Publisher("/R1/speaker", String, queue_size=10)
	batt_pub = rospy.Publisher("/R1/battery", BatteryState, queue_size=10)
	signal_pub = rospy.Publisher("/R1/vital_signal", String, queue_size=10)
	signal_pub = rospy.Publisher("/R1/vital_signal", String, queue_size=10)
	print('publishers on!')


	rate = rospy.Rate(10)

	spk = String()
	spk.data = "Hello World Hospital"

	batt = BatteryState()
	batt.voltage = 12.06

	signal = String()
	signal.data = "Its alive!"

	while not rospy.is_shutdown():
		speaker_pub.publish(spk)
		batt_pub.publish(batt)
		signal_pub.publish(signal)

		rate.sleep()

				
