

class Control :
	Direction = 0
	Speed = 0


	@staticmethod
	def lefter ():
		Control.Direction+=10

	@staticmethod
	def righter ():
		Control.Direction-=10

	@staticmethod
	def center():
		Control.Direction/=2

	@staticmethod
	def speedup(val):
		Control.Speed += val

	@staticmethod
	def speeddown(val):
		Control.Speed -= val