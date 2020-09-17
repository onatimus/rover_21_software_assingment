#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32


def callback(data):

	rospy.loginfo("Our data is: " + str(data.data))


def listen():


	rospy.init_node('listener', anonymous=False) 

	rospy.Subscriber('big_listener', String, callback)

	rospy.spin()


if __name__ == "__main__":
	listen()