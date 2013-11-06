from __future__ import division
from math import pi

__all__ = ['fromrad', 'angle', 'todeg', 'torad', 'deg', 'rad']

def todeg(th):
	return th * 180 / pi
def torad(th):
	return th * pi / 180

class Angle(float): pass

def fromrad(th):
	return mode.fromrad(th)

def angle(th):
	return mode.interpret(th)


class Rad(Angle):
	def __str__(self): return '%.4f' % self
	def __repr__(self): return str(self)
	def __add__(*args): return Rad(float.__add__(*args))
	def __sub__(*args): return Rad(float.__sub__(*args))
	def __mul__(*args): return Rad(float.__mul__(*args))
	def __div__(*args): return Rad(float.__div__(*args))
	def __mod__(*args): return Rad(float.__mod__(*args))
	@staticmethod
	def fromrad(th): return asrad(th)
	@staticmethod
	def interpret(th): return rad(th)

def rad(th): return Rad(th)
def asrad(th): return Rad(th)
RAD = Rad


class Deg(Angle):
	def __str__(self): return '%.2fdeg' % todeg(self)
	def __repr__(self): return str(self)
	def __add__(*args): return Deg(float.__add__(*args))
	def __sub__(*args): return Deg(float.__sub__(*args))
	def __mul__(*args): return Deg(float.__mul__(*args))
	def __div__(*args): return Deg(float.__div__(*args))
	def __mod__(*args): return Deg(float.__mod__(*args))
	@staticmethod
	def fromrad(th): return asdeg(th)
	@staticmethod
	def interpret(th): return deg(th)

def deg(th): return Deg(torad(th))
def asdeg(th): return Deg(th)
DEG = Deg


mode = DEG
