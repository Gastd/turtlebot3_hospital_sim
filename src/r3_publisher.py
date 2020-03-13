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

def inter_r5(msg):
	pass


if __name__ == '__main__':

	# initializes node
	rospy.init_node("r1_publisher", anonymous=False)
	# starts subscribers and publishers
	rospy.Subscriber("/R5/intercom", String, inter_r5)
	print('subscribers on!')
	speaker_pub = rospy.Publisher("/R3/speaker", String, queue_size=10)
	batt_pub = rospy.Publisher("/R3/battery", BatteryState, queue_size=10)
	med_pub = rospy.Publisher("/R3/medicine", String, queue_size=10)
	obj_pub = rospy.Publisher("/R3/objs", String, queue_size=10)
	obj_pub = rospy.Publisher("/R3/intercom", String, queue_size=10)
	print('publishers on!')


	rate = rospy.Rate(10)

	spk = String()
	spk.data = "Hello World Hospital"

	batt = BatteryState()
	batt.voltage = 12.06

	med = String()
	med.data = "Aspirin"

	obj = String()
	obj.data = "Box"

	while not rospy.is_shutdown():
		speaker_pub.publish(spk)
		batt_pub.publish(batt)
		med_pub.publish(med)
		obj_pub.publish(obj)

		rate.sleep()

				
