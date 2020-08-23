#!/usr/bin/env python  
import roslib
import rospy

import tf
from geometry_msgs.msg import PoseStamped

def handle_turtle_pose(msg, turtlename):
    br = tf.TransformBroadcaster()
    br.sendTransform((msg.pose.position.x, msg.pose.position.y, msg.pose.position.z),
                     [msg.pose.orientation.x, msg.pose.orientation.y, msg.pose.orientation.z, msg.pose.orientation.w],
                     rospy.Time.now(),
                     turtlename + "/odom",
                     "map")

if __name__ == '__main__':
    rospy.init_node('turtle_tf_broadcaster')
    turtlename = rospy.get_param('~turtle')
    rospy.Subscriber('/%s/pose' % turtlename,
                     PoseStamped,
                     handle_turtle_pose,
                     turtlename)
    rospy.spin()