#-*- coding:utf-8 -*-
import RPIO
from RPIO import PWM

RPIO.cleanup()

servo = PWM.Servo()
RPIO.setup(27, RPIO.OUT)
dcen = 27
RPIO.setup(22, RPIO.OUT)
dcdr = 22

PWM.setup()
PWM.init_channel(3)


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
	def speedzero():
		Control.Speed =0
		Control.setspeed()

	@staticmethod
	def setdirection():
		servo.set_servo(9,1400 + Control.Direction)


	@staticmethod
	def setspeed():

		if (Control.Speed == 0) :
			RPIO.output(dcen, True)
		else :
			RPIO.output(dcen, False)

		if (Control.Speed < 0 ) :
			RPIO.output(dcdr, True)
		else:
			RPIO.output(dcdr, True)
		

		PWM.add_channel_pulse(3, 10, 0, Control.Speed)

