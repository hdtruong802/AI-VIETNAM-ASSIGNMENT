import math

# Sigmoid
def sigmoid(x):
	return 1 / (1 + math.e ** (-x))

# Tanh
def tanh(x):
	return (math.e ** x - math.e ** (-x)) / (math.e ** x + math.e ** (-x))

# Softplus
def softplus(x):
	return math.log(1 + math.e ** x)

# ReLU
def relu(x):
	if x <= 0:
		return 0
	else:
		return x

# Leaky ReLU
def leaky_relu(x):
	if x <= 0:
		return 0.01 * x
	else:
		return x

# PReLU
def prelu(x, alpha):
	if x <= 0:
		return alpha * x
	else:
		return x

# Swish
def swish(x, beta):
	return x / (1 + math.e ** (-beta * x))

def activate(function_name, x, alpha = None, beta = None):
	if function_name == "sigmoid":
		return sigmoid(x)
	elif function_name == "tanh":
		return tanh(x)
	elif function_name == "softplus":
		return softplus(x)
	elif function_name == "relu":
		return relu(x)
	elif function_name == "leaky_relu":
		return leaky_relu(x)
	elif function_name == "prelu":
		return prelu(x, alpha)
	elif function_name == "swish":
		return swish(x, beta)
	else:
		raise ValueError("Unknow activation function")

print(activate("sigmoid", math.e))
print(activate("softplus", 5))
print(activate("prelu", 2, 0.1))
print(activate("swish", 2, None, 1))
