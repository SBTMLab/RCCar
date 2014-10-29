#-*- coding:utf-8 -*-
from RPIO import PWM

servo = PWM.Servo()

class Control :
	Direction = 0
	Speed = 0


	@staticmethod
	def lefter ():
		if Control.Direction <1400 :
			Control.Direction= 700#+=200
			Control.setdirection()

	@staticmethod
	def righter ():
		if Control.Direction >-1400 :
			Control.Direction= -700#-=200
			Control.setdirection()

	@staticmethod
	def center():
		Control.Direction = 0
		Control.setdirection()

	@staticmethod
	def speedup(val):
		Control.Speed += val

	@staticmethod
	def speeddown(val):
		Control.Speed -= val

	@staticmethod
	def setdirection():
		servo.set_servo(9,1400 + Control.Direction)
