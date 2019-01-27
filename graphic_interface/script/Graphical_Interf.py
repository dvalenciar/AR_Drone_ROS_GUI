#!/usr/bin/env python

"""
Author: David Valencia
Date  : 25/01/2019

Description: 

"""
from PyQt4 import QtCore, QtGui

import GUI
import rospy 
import math
import sys

from   std_msgs.msg 	     import Empty
from   nav_msgs.msg          import Odometry
from   geometry_msgs.msg     import Twist
from   ardrone_autonomy.msg  import Navdata

class MainUiClass(QtGui.QMainWindow, GUI.Ui_MainWindow):


	def __init__(self, parent = None):

		super(MainUiClass, self).__init__(parent) 
		self.setupUi(self)
		self.threadClass = ThreadClass()
		self.threadClass.start()

		self.TakeOffPub1 = rospy.Publisher('ardrone/takeoff' , Empty, queue_size=1)
		self.LandPub1    = rospy.Publisher('ardrone/land'    , Empty, queue_size=1)
		self.movePub1    = rospy.Publisher('cmd_vel'         , Twist, queue_size=1)
		self.setvelSet   = 0.0

		self.connect(self.threadClass, QtCore.SIGNAL('altitude')  , self.updateProgressAltitudeDrone)
		self.connect(self.threadClass, QtCore.SIGNAL('position_x'), self.updateProgressPosition_X)
		self.connect(self.threadClass, QtCore.SIGNAL('position_y'), self.updateProgressPosition_Y)
		self.connect(self.threadClass, QtCore.SIGNAL('yaw')       , self.updateProgressPosition_Yaw)



		self.Stop_Button.clicked.  connect(self.stop)
		self.Up_Button.clicked.    connect(self.moverArriba)
		self.Down_Button.clicked.  connect(self.moverAbajo)
		self.Left_Button.clicked.  connect(self.moverIzquierda)
		self.Right_Button.clicked. connect(self.moverDerecha)

		self.Front_Button.clicked.        connect(self.moverAdelante)
		self.Back_Button.clicked.         connect(self.moverAtras)
		self.Rotate_Left_Button.clicked.  connect(self.rotarIzquierda)
		self.Rotate_Right_Button.clicked. connect(self.rotarDerecha)


		self.Land_Button.clicked.          connect (self.Aterrizar)
		self.Take_Off_Button.clicked.      connect (self.Despegar)
		self.Velocity_Slider.valueChanged. connect (self.setVelocidad)



	def setVelocidad(self):

		self.setvel = self.Velocity_Slider.value()
		self.setvelSet= ( self.setvel * 0.1 )
		print self.setvelSet
		

	def moverAdelante(self):
		print "adelante"
		twist = Twist()
		twist.linear.x = self.setvelSet
		self.movePub1.publish(twist)		

	def moverAtras(self):
		print "atras"
		twist = Twist()
		twist.linear.x = -self.setvelSet
		self.movePub1.publish(twist)	

	def rotarDerecha(self):
		print "rotar Derecha"
		twist = Twist()
		twist.angular.z = -self.setvelSet
		self.movePub1.publish(twist)	
	
	def rotarIzquierda(self):
		print "rotar izquieda"
		twist = Twist()
		twist.angular.z =  self.setvelSet
		self.movePub1.publish(twist)	

	def moverArriba(self):
		print "arriba"		
		twist = Twist()
		twist.linear.z = self.setvelSet
		self.movePub1.publish(twist)	

	def moverAbajo(self):
		print "abajo"
		twist = Twist()
		twist.linear.z = -self.setvelSet
		self.movePub1.publish(twist)	

	def moverIzquierda(self):
		print "Izquierda"
		twist = Twist()
		twist.linear.y = self.setvelSet
		self.movePub1.publish(twist)	
	
	def moverDerecha(self):
		print "derecha"
		twist = Twist()
		twist.linear.y = -self.setvelSet
		self.movePub1.publish(twist)	


	def stop(self):
		print "stop"
		twist = Twist()
		twist.linear.x  = 0.0
		twist.linear.y  = 0.0
		twist.linear.z  = 0.0
		twist.angular.z = 0.0
		self.movePub1.publish(twist)	

	def Despegar(self):
		print "despegar"
		empty=Empty()
		self.TakeOffPub1.publish(empty)

	def  Aterrizar (self):
		print "aterrizar"
		empty=Empty()
		self.LandPub1.publish(empty)


	def updateProgressPosition_X(self,val):
		self.lineEdit_X.setText(str(val))

	def updateProgressPosition_Y(self,val):
		self.lineEdit_Y.setText(str(val))

	def updateProgressPosition_Yaw(self,val):
		self.lineEdit_Yaw.setText(str(val))


	def updateProgressAltitudeDrone(self,val):
		self.lcd_Altitude.display(val)  




class ThreadClass(QtCore.QThread):

	def __init__(self, parent = None):

		super(ThreadClass, self).__init__(parent) 



		rospy.Subscriber("ardrone/navdata"            , Navdata   ,self.ang_callback)
		rospy.Subscriber("ground_truth/state" , Odometry  ,self.atitude_callback)


		
	def ang_callback(self,ang_data):

		self.yaw_dron   = ang_data.rotZ  # angulo yaw del dron en degranes
		self.emit(QtCore.SIGNAL('yaw'),self.yaw_dron)

	def atitude_callback(self,pose_data):

		self.altitude_dron  = pose_data.pose.pose.position.z
		self.emit(QtCore.SIGNAL('altitude'),self.altitude_dron)

		self.pos_x_dron  = pose_data.pose.pose.position.x
		self.emit(QtCore.SIGNAL('position_x'),self.pos_x_dron)

		self.pos_y_dron  = pose_data.pose.pose.position.y
		self.emit(QtCore.SIGNAL('position_y'),self.pos_y_dron)


if __name__ == '__main__':
	
	rospy.init_node('node_ar_drone',anonymous=True)

	a   = QtGui.QApplication(sys.argv)
	app = MainUiClass()
	app.show()
	a.exec_()
	rospy.spin()
