import numpy as np
import matplotlib.pyplot as plt

def gaussmf(x, mean, sigma):
    """
    Gaussian fuzzy membership function.

    Parameters
    ----------
    x : 1d array or iterable
        Independent variable.
    mean : float
        Gaussian parameter for center (mean) value.
    sigma : float
        Gaussian parameter for standard deviation.

    Returns
    -------
    y : 1d array
        Gaussian membership function for x

    """
    return np.exp(-((x - mean) ** 2.) / float(sigma) ** 2.)


def gbellmf(x, a, b, c):
    """
    Generalized Bell function fuzzy membership generator.

    Parameters
    ----------
    x : 1d array
        Independent variable.
    a : float
        Bell function parameter controlling width. See Note for definition.
    b : float
        Bell function parameter controlling center. See Note for definition.
    c : float
        Bell function parameter controlling slope. See Note for definition.

    Returns
    -------
    y : 1d array
        Generalized Bell fuzzy membership function.

    Notes
    -----
    Definition of Generalized Bell function is:

        y(x) = 1 / (1 + abs([x - c] / a) ** [2 * b])

    """
    return 1. / (1. + np.abs((x - c) / a) ** (2 * b))

x = np.linspace(-1, 10)
plt.plot(x, gbellmf(x,1,3,5))
plt.show()