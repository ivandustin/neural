import numpy

def to_wave(txt, max_char=100):
	waves = []
	if len(txt) > max_char:
		raise Exception("input is greater than maximum")
	for i in range(0, len(txt)):
		ch = txt[i]
		v = ord(ch)
		if v > 127:
			raise Exception("invalid character")
		wave = [0] * 128
		wave[v] = 1
		waves = waves + wave
	x = max_char - len(txt)
	y = x * 128
	z = [0] * y
	waves = waves + z
	return numpy.array(waves)
