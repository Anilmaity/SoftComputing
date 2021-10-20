
import matplotlib.pyplot as plt

import numpy as np


def identy(x):
        return x

def binary(x):
    y=[]
    for mem in x:
        if mem > 0:
            y.append(1)
        else:
            y.append(0)

    return y

def bipolar(x):
    y=[]
    for mem in x:
        if mem > 0:
            y.append(1)
        else:
            y.append(-1)

    return y

def sigmoid_bipolar(x):
    if x >= 0:
        return 1
    else:
        return -1

def linear(x):
    y = 2.5
    return y*x



def bell_shaped(x):

    mean = np.mean(x)
    std = np.std(x)
    y_out = 1 / (std * np.sqrt(2 * np.pi)) * np.exp(- (x - mean) ** 2 / (2 * std ** 2))
    return y_out




x = np.linspace(-10, 10)
plt.plot(x, bell_shaped(x))

plt.title('Activation Function :bellshaped')
plt.show()


x = np.linspace(-10, 10)
plt.plot(x, linear(x))

plt.title('Activation Function : linear')
plt.show()


x = np.linspace(-10, 10)
plt.plot(x, identy(x))

plt.title('Activation Function :identy')
plt.show()


x = np.linspace(-10, 10)
print(len(binary(x)))
plt.plot(x, binary(x))
plt.title('Activation Function : binary')
plt.show()


x = np.linspace(-10, 10)
plt.plot(x, bipolar(x))
plt.title('Activation Function : bipolar')
plt.show()
