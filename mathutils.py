def sign(x):
	if x == 0: return 0
	elif x < 0: return -1
	else: return 1

def pow_signed(x, e):
	return sign(x) * abs(x**e)

def int_if_possible(x):
	n = int(x)
	return n if n == x else x

def roundoff_error(x):
	return int_if_possible(round(x, 14))