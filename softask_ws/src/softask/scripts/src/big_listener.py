#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32


def split(list, index):
	if list[0] == "A" and list[index-1] == "B": 
		new_list = []
		list_len = len(list)
		data_str = ''
		
		for i in range(2, index, 4):
			if list[i-1] == '1':
				new_list.append(100*int(list[i]) + 10*int(list[i+1]) + int(list[i+2]))
			else:
				new_list.append(-1*(100*int(list[i]) + 10*int(list[i+1]) + int(list[i+2])))
			
		for j in range(0,(index-2)/4):
			if new_list[j] > 255:
				new_list[j] = 255
			elif new_list[j] < -255:
				new_list[j] = -255
			new_list[j] = str(new_list[j])
			data_str = data_str + new_list[j] + " "

		rospy.loginfo(data_str)
		return data_str
	
	else:
		rospy.loginfo("Invalid Data!")
		return "Invalid Data!"

def store(String):
	data_list = list(String)
	return data_list

def callback_r_arm(data):
	pub = rospy.Publisher('big_listener', String, queue_size = 10)
	rospy.loginfo("Our message is: " + 	str(data.data))
	msg  = split(store(data.data), 26)
	pub.publish(msg)

def callback_drive(data):

	pub = rospy.Publisher('big_listener', String, queue_size = 10)
	rospy.loginfo("Our message is: " + 	str(data.data))
	msg = split(store(data.data), 18)
	pub.publish(msg)

def subs():
	
	rospy.init_node('big_subs', anonymous=False) 
	rospy.Subscriber('/serial/robotic_arm', String, callback_r_arm)
	rospy.Subscriber('/serial/drive', String, callback_drive)
	rospy.spin()

if __name__ == "__main__":
	subs()