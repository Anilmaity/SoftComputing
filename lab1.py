#ACHYUT SAPARIYA(180110120048)
import numpy as np
import matplotlib.pyplot as plt
import math

def sigmoid_binary(x):
    ''' It returns 1/(1+exp(-x)). where the values lies between zero and one '''

    return 1/(1+np.exp(-x))

def sigmoid_bipolar(x):
    ''' It returns (1-np.exp(-x))/(1+np.exp(-x)). where the values lies between -1 and 1 '''

    return (1-np.exp(-x))/(1+np.exp(-x))

def bell_shaped(x):

    mean = np.mean(x)
    std = np.std(x)
    y_out = 1 / (std * np.sqrt(2 * np.pi)) * np.exp(- (x - mean) ** 2 / (2 * std ** 2))
    return y_out

def RELU(x):
    ''' It returns zero if the input is less than zero otherwise it returns the given input. '''
    x1=[]
    for i in x:
        if i<0:
            x1.append(0)
        else:
            x1.append(i)

    return x1

def ramp(x):

    ramp = []
    for sample in x:
        if sample < 0:
            ramp.append(0)
        else:
            ramp.append(sample)
    return ramp

x = np.linspace(-10, 10)
plt.plot(x, ramp(x))       #call function from above as per your req.

plt.axis('tight')
plt.title('Activation Function :RAMP')
plt.title("Achyut",
             loc='right',
             rotation=45)
plt.show()