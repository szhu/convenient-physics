from __future__ import division
from math import pi

__all__ = ['angle', 'todeg', 'torad', 'deg', 'rad']

def todeg(th):
	return th * 180 / pi
def torad(th):
	return th * pi / 180

class Angle(float): pass

def angle(th):
	return mode(th)

class Rad(Angle):
	def __str__(self): return '%.4f' % self
	def __repr__(self): return str(self)
	def __add__(*args): return Rad(float.__add__(*args))
	def __sub__(*args): return Rad(float.__sub__(*args))
	def __mul__(*args): return Rad(float.__mul__(*args))
	def __div__(*args): return Rad(float.__div__(*args))
	def __mod__(*args): return Rad(float.__mod__(*args))

def rad(th): return Rad(th)
def asrad(th): return Rad(th)


class Deg(Angle):
	def __str__(self): return '%.2fdeg' % todeg(self)
	def __repr__(self): return str(self)
	def __add__(*args): return Deg(float.__add__(*args))
	def __sub__(*args): return Deg(float.__sub__(*args))
	def __mul__(*args): return Deg(float.__mul__(*args))
	def __div__(*args): return Deg(float.__div__(*args))
	def __mod__(*args): return Deg(float.__mod__(*args))

def deg(th): return Deg(torad(th))
def asdeg(th): return Deg(th)

mode = asdeg