


import numpy as np
from neupy import algorithms


inputs = [[1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
              [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0]]

'''

1 0 0 0 1      0 1 1 1 0
0 1 0 1 0      1 0 0 0 1
0 0 1 0 0      1 0 0 0 1
0 1 0 1 0      1 0 0 0 1
1 0 0 0 1      0 1 1 1 0

Letter X       Letter O
    1               0
'''

hebbnet = algorithms.HebbRule(
    n_inputs=25,
    n_outputs=1,
    n_unconditioned=1,
    step=0.1,
    decay_rate=0.8,
    verbose=False)
hebbnet.train(inputs, epochs=25)
print("Predict for input" + str(inputs) + " whis is X and O")
print("Pridict value 1 equal X and 0 imply 0 " + str(hebbnet.predict(inputs)))

