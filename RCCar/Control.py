#-*- coding:utf-8 -*-
import RPIO
from RPIO import PWM

RPIO.cleanup()

PWM.setup()

servo = PWM.Servo()
RPIO.setup(27, RPIO.OUT)
dcen = 27
RPIO.setup(22, RPIO.OUT)
dcdr = 22



PWM.init_channel(3)


class Control :
	Direction = 0
	Speed = 0


	@staticmethod
	def lefter ():
		Control.Direction= 1700
		Control.setdirection()

	@staticmethod
	def righter ():
		Control.Direction= 700
		Control.setdirection()

	@staticmethod
	def center():
		Control.Direction = 1000
		Control.setdirection()

	@staticmethod
	def speedup(val):
		Control.Speed += val

		if Control.Speed > 700 :
			Control.Speed = 700

		Control.setspeed()

	@staticmethod
	def speeddown(val):
		if Control.Speed < -700 :
			Control.Speed = -700
		Control.Speed -= val
		Control.setspeed()

	@staticmethod
	def speedzero():
		Control.Speed = 0
		Control.setspeed()

	@staticmethod
	def setdirection():
		print Control.Direction
		servo.set_servo(9,Control.Direction)


	@staticmethod
	def setspeed():
		RPIO.output(dcen, False)

		if (Control.Speed < 0 ) :
			RPIO.output(dcdr, True)
			spd = - Control.Speed
		else:
			RPIO.output(dcdr, False)
			spd = Control.Speed	

		PWM.add_channel_pulse(3, 10, 0, spd)

