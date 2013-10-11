from __future__ import division

__all__ = ["xy", "rth"]

from math import sqrt, pi, sin, cos, atan2
from physics.mathutils import pow_signed
from physics.angles import asdeg

class Coords:
	def __init__(self, x, y, r, th):
		self.x = x
		self.y = y
		self.r = r
		self.th = ((th+pi) % (2*pi))-pi
	def __neg__(self): return self * -1
	def __sub__(self, other): return self + -other
	def __truediv__(self, a): return self * (1/a)
	def __rmul__(self, a): return self * a
	def __repr__(self): return str(self)

class CoordsXY(Coords):
	def __str__(self): return '(x=%r, y=%r)' % (self.x, self.y)

	@property
	def xy(self): return self
	
	@property
	def rth(self): return CoordsRTh(self.x, self.y, self.r, self.th)

	def __add__(self, other): return xy(self.x+other.x, self.y+other.y)

	def __mul__(self, a): return xy(self.x*a, self.y*a)

	def __rtruediv__(self, a): return xy(1/self.x*a, 1/self.y*a)

	def __pow__(self, e): return xy(pow_signed(self.x, e), pow_signed(self.y, e))

class CoordsRTh(Coords):
	def __str__(self): return '(r=%r, th=%r)' % (self.r, self.th)

	@property
	def xy(self): return CoordsXY(self.x, self.y, self.r, self.th)
	
	@property
	def rth(self): return self

	def __add__(self, other): return xy(self.x+other.x, self.y+other.y).rth

	def __mul__(self, a): return rth(self.r*a, self.th)

	def __rtruediv__(self, a): return rth(1/self.r*a, self.th)

	def __pow__(self, e): return rth(pow_signed(self.r, e), self.th)


def xy(x,y):
	return CoordsXY(x, y, sqrt(x*x+y*y), asdeg(atan2(y, x)))

def rth(r, th):
	return CoordsRTh(r*cos(th), r*sin(th), r, th)

def _test():
	print(xy(2,1) + xy(3,4))

if __name__ == '__main__':
	_test()
