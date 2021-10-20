
from sklearn.neural_network import MLPClassifier
import numpy as np

X = np.array([[1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0],
          [1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0]])

y = [1,2,0,3]
'''

1 0 0 0 1      0 1 1 1 0
0 1 0 1 0      1 0 0 0 1
0 0 1 0 0      1 0 0 0 1
0 1 0 1 0      1 0 0 0 1
1 0 0 0 1      0 1 1 1 0

Letter X       Letter O
    1               0


1 0 0 0 1      1 1 1 1 0
0 1 0 1 0      1 0 0 0 1
0 0 1 0 0      1 0 0 0 1
0 1 0 0 0      1 0 0 0 1
1 0 0 0 0      1 1 1 1 0

Letter  Y       Letter D
    2               3
'''

print("4 Class problem to recogonize 4 different letter" )

# Finally for the MLP- Multilayer Perceptron
print("perceptron model with 2 hidden layyer ")
mlp = MLPClassifier(hidden_layer_sizes=(25,4), max_iter=500)
mlp.fit(X, y)


predictions = mlp.predict(X)


print("The same input is given" + str(X))
print(" for prediction and the output is  ")

print(" 0 FOR 0 , 1 FOR X , 2 FOR Y , 3 FOR Z "+ str(predictions))


