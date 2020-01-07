from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense, Activation, LeakyReLU
from neural import text

def dataset(path, input):
	dataset = loadtxt(path, delimiter=",")
	return dataset[:, 0:input], dataset[:, input:]

def network(input, layers, output):
	activation = LeakyReLU(alpha=0.1)
	model = Sequential()
	model.add(Dense(layers.pop(0),
		input_dim=input,
		kernel_initializer="he_uniform"))
	model.add(activation)
	for n in layers:
		model.add(Dense(n))
		model.add(activation)
	model.add(Dense(output))
	model.add(activation)
	model.compile(optimizer="sgd", loss="mean_squared_error", metrics=["accuracy"])
	return model
