from __future__ import division
from math import pi

__all__ = ['angle', 'deg', 'rad', 'setdeg', 'setrad']

# This is the only actual math this module does

def todeg(th):
	return th * 180 / pi
def torad(th):
	return th * pi / 180


# Abstract superclass of all angle classes

class Angle(float): pass

def angle(th): return mode.interpret(th)
def asangle(th): return mode.fromrad(th)

# Radians

class Rad(Angle):
	def __str__(self): return '%.4f' % self
	def __repr__(self): return str(self)
	def __add__(*args): return Rad(float.__add__(*args))
	def __sub__(*args): return Rad(float.__sub__(*args))
	def __mul__(*args): return Rad(float.__mul__(*args))
	def __div__(*args): return Rad(float.__div__(*args))
	def __mod__(*args): return Rad(float.__mod__(*args))
	@property
	def rad(self): return self
	@property
	def deg(self): return Deg.fromrad(self)
	@staticmethod
	def fromrad(th): return Rad(th)
	@staticmethod
	def interpret(th):
		if isinstance(th, Angle): return th.rad
		else: return Rad(th)

RAD = Rad
def rad(th): return Rad.interpret(th)
def asrad(th): return Rad.fromrad(th)
def setrad():
	global mode
	mode = Rad


# Degrees

class Deg(Angle):
	def __str__(self): return '%.2fdeg' % todeg(self)
	def __repr__(self): return str(self)
	def __add__(*args): return Deg(float.__add__(*args))
	def __sub__(*args): return Deg(float.__sub__(*args))
	def __mul__(*args): return Deg(float.__mul__(*args))
	def __div__(*args): return Deg(float.__div__(*args))
	def __mod__(*args): return Deg(float.__mod__(*args))
	@property
	def rad(self): return Rad.fromrad(self)
	@property
	def deg(self): return self
	@staticmethod
	def fromrad(th): return Deg(th)
	@staticmethod
	def interpret(th):
		if isinstance(th, Angle): return th.deg
		else: return Deg(torad(th))

DEG = Deg
def deg(th): return Deg.interpret(th)
def asdeg(th): return Deg.fromrad(th)
def setdeg():
	global mode
	mode = Deg


# Set default mode

mode = None
setrad()
