#!/usr/bin/env python  
import roslib
import rospy

import tf
# from tf import listener
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry
import numpy as np
import tf2_ros

map_trans = [0, 0, 0]
map_rot = (0, 0, 0, 1)

pub = None
def handle_turtle_pose(msg, turtlename):
    new_msg = Odometry()
    new_msg.header = msg.header
    new_msg.header.frame = "map"
    new_msg.child_frame_id = "base_footprint"
    new_msg.pose.pose = msg.pose
    pub.publish(new_msg)
    

if __name__ == '__main__':
    rospy.init_node('turtle_tf_broadcaster')
    # listener = tf.TransformListener()
    # br = tf.TransformBroadcaster()
    turtlename = 'turtlebot1'
    # turtlename = rospy.get_param('~turtle')
    rospy.Subscriber('/%s/pose' % turtlename, PoseStamped, handle_turtle_pose, turtlename)
    pub = rospy.Publisher('base_pose_ground_truth', Odometry, queue_size=1)
    rospy.spin()
    # rate = rospy.Rate(10.0)
    # while not rospy.is_shutdown():
    #     try:
    #         (trans,rot) = listener.lookupTransform('/turtlebot1/odom', '/turtlebot1/base_footprint', rospy.Time(0))
    #         rospy.loginfo(trans)
    #         rospy.loginfo(rot)
    #         # br.sendTransform((msg.pose.position.x, msg.pose.position.y, 0),
    #         #                  [msg.pose.orientation.x, msg.pose.orientation.y, msg.pose.orientation.z, msg.pose.orientation.w],
    #         #                  rospy.Time.now(),
    #         #                  turtlename + "/odom",
    #         #                  "map")
    #         new_trans = np.matmul(map_trans, np.linalg.inv(trans))
    #         br.sendTransform(new_trans,
    #                      [msg.pose.orientation.x, msg.pose.orientation.y, msg.pose.orientation.z, msg.pose.orientation.w],
    #                      rospy.Time.now(),
    #                      turtlename + "/odom",
    #                      "map")
    #     except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
    #         pass

    #     rate.sleep()