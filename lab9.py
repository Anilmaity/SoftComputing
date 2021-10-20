import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def step_function(x):
    if x < 0:
        return -1
    else:
        return 1


def perceptron(X, y, lr, epochs):
    # X --> Inputs.
    # y --> labels/target.
    # lr --> learning rate.
    # epochs --> Number of iterations.

    # m-> number of training examples
    # n-> number of features
    m, n = X.shape
    print("Shape of input "+ str(X.shape))

    # Initializing parapeters(theta) to zeros.
    # +1 in n+1 for the bias term.
    theta = np.zeros((n + 1, 1))

    # Empty list to store how many examples were
    # misclassified at every iteration.
    n_miss_list = []

    # Training.
    for epoch in range(epochs):

        # variable to store #misclassified.
        n_miss = 0

        # looping for every example.
        for idx, x_i in enumerate(X):

            # Insering 1 for bias, X0 = 1.
            x_i = np.insert(x_i, -1, 1).reshape(-1, 1)

            # Calculating prediction/hypothesis.
            y_hat = step_function(np.dot(x_i.T, theta))

            print("Prdicted output " +str(y_hat) + " for input" + str(x_i.T))



            # Updating if the example is misclassified.
            if (np.squeeze(y_hat) - y[idx]) != 0:
                theta += lr * ((y[idx] - y_hat) * x_i)

                # Incrementing by 1.
                n_miss += 1

        # Appending number of misclassified examples
        # at every iteration.
        n_miss_list.append(n_miss)

    return theta, n_miss_list


data = np.array([[1,-1,1,-1,1,-1,-1,1,-1],[1,-1,1,1,1,1,1,-1,1]])

Target = [1 , -1]

theta , miss = perceptron(data,Target,0.1,10)



