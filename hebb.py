import numpy


def binary(z, theata):
    if z >= theata:
        return 1
    else:
        return 0


Input = [[0, 0],
         [1, 0],
         [0, 1],
         [1, 1]]

output = [0, 0, 0, 1]

Weights = [[1, 1],
           [1, 1],
           [1, 1],
           [1, 1]]

theata = 2


def fire(input, output, theata, Weights):
    for x in range(4):
        yin = input[x][0] * Weights[x] + input[x][1] * Weights[x]
        print(binary(yin, theata))


#        print(output[x])


def learn(Weights, input):
    for x in range(4):
        yin = input[x][0] * Weights[x][0] + input[x][1] * Weights[x][1]

        Weights[x][0] = Weights[x][0] + yin * (input[x][0] + input[x][1])
        Weights[x][1] = Weights[x][1] + yin * (input[x][0] + input[x][1])

    print(Weights)



learn(Weights,Input)
