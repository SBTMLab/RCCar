#-*- coding:utf-8 -*-
from RPIO import PWM

servo = PWM.Servo()
RPIO.setup(27, RPIO.OUT)
dcen = 27
RPIO.setup(22, RPIO.OUT)
dcdr = 22

PWM.setup()
PWM.init_channel(10)


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
		Control.setspeed()

	@staticmethod
	def speeddown(val):
		Control.Speed -= val
		Control.setspeed()

	@staticmethod
	def setdirection():
		servo.set_servo(8,1400 + Control.Direction)


	@staticmethod
	def setspeed():
		RPIO.output(dcen, False)
		RPIO.output(dcdr, False)
		PWM.add_channel_pulse(0, 10, 100, 50)


