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

def inter_r3(msg):
	pass


if __name__ == '__main__':

	# initializes node
	rospy.init_node("r1_publisher", anonymous=False)
	# starts subscribers and publishers
	rospy.Subscriber("/R3/intercom", String, inter_r3)
	print('subscribers on!')
	speaker_pub = rospy.Publisher("/R5/speaker", String, queue_size=10)
	batt_pub = rospy.Publisher("/R5/battery", BatteryState, queue_size=10)
	obj_pub = rospy.Publisher("/R5/objs", String, queue_size=10)
	heavy_obj_pub = rospy.Publisher("/R5/heavy_objs", String, queue_size=10)
	obj_pub = rospy.Publisher("/R5/intercom", String, queue_size=10)
	print('publishers on!')


	rate = rospy.Rate(10)

	spk = String()
	spk.data = "Hello World Hospital"

	batt = BatteryState()
	batt.voltage = 12.06

	obj = String()
	obj.data = "Box"

	heavy_obj = String()
	heavy_obj.data = "Large Box"

	while not rospy.is_shutdown():
		speaker_pub.publish(spk)
		batt_pub.publish(batt)
		obj_pub.publish(obj)
		heavy_obj_pub.publish(heavy_obj)

		rate.sleep()

				
