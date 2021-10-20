
import numpy as np
from matplotlib import pyplot as plt

# the features for the or model , here we have
# taken the possible values for combination of
# two inputs
features = np.array(
    [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ])

# labels for the or model, here the output for
# the features is taken as an array
labels = np.array([0, 0, 0, 1])

# to print the features and the labels for
# which the model has to be trained
print(features, labels)

# initialise weights, bias , learning rate, epoch
weight = [0.5, 0.5]
bias = 0.05
learning_rate = 0.1
epoch = 5

sum_error_list = []
for i in range(epoch):

    # epoch is the number of the the model is trained
    # with the same data
    print("epoch :", i + 1)

    # variable to check if there is no change in previous
    # weight and present calculated weight
    # initial error is kept as 0
    sum_squared_error = 0.0

    # for each of the possible input given in the features
    for j in range(features.shape[0]):
        # actual output to be obtained
        actual = labels[j]

        # the value of two features as given in the features
        # array
        x1 = features[j][0]
        x2 = features[j][1]

        # net unit value computation performed to obtain the
        # sum of features multiplied with thier weights
        unit = (x1 * weight[0]) + (x2 * weight[1]) + bias

        # error is computed so as to update the weights
        error = actual - unit

        # print statement to print the actual value , predicted
        # value and the error
        print("error =", error)

        # summation of squared error is calculated
        sum_squared_error += error * error

        # updation of weights, summing up of product of learning rate ,
        # sum of squared error and feature value
        weight[0] += learning_rate * error * x1
        weight[1] += learning_rate * error * x2

        # updation of bias, summing up of product of learning rate and
        # sum of squared error
        bias += learning_rate * error

    print("sum of squared error = ", sum_squared_error / 4, "\n\n")

    sum_error_list.append(sum_squared_error/4)


    testx1 = 1
    testx2 = 0
    unit = (testx1 * weight[0]) + (x2 * weight[1]) + bias
    print("test:[1,0] " '\r')
    print(' Output '+ str(unit))


plt.figure()
plt.plot(sum_error_list)
plt.xlabel("epoch")
plt.ylabel("error")
plt.title(" adaline network binary input")
plt.show()

