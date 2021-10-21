
'''Write a program for maximizing 𝑓(𝑥) = 𝑥2 using GA, where 𝑥 is the range from 0 to 20.
Perform 5 iterations only
'''

from random import randint

def mutation(member):
    mutate_member = []
    for mem in member:
        mutate = randint(0,20)
        mutate_side = randint(-1,1)
        #print(mutate,mutate_side)
        if (mem+(mutate*mutate_side) < 20 and mem+(mutate*mutate_side) > 0):
            mutate_member.append(mem + (mutate*mutate_side))
        else:
            mutate_member.append(mem)


    return mutate_member


def selection(fitnessvalue):
    # Steady State Selection
    avg =sum(fitnessvalue)/5

    error = 0
    mem_val = [round(fitnessvalue[0]/avg+error) , round(fitnessvalue[1]/avg+error) , round(fitnessvalue[2]/avg+error) , round(fitnessvalue[3]/avg+error) ,int(fitnessvalue[4]/avg+error)]
    mem_sum = sum(mem_val)
    error = (5 - mem_sum)
    if error > 0:
        mem_val[0] += error
    else:
        if mem_val[0]>error:
            mem_val[0] -= error


    new_member = []
    for mem in range(5):
        for x in range(mem_val[mem]):
            new_member.append(member[mem])

    return new_member




def fitness(members):
    fitvalue = []
    for mem in members:
        performance = function(mem)
        fitvalue.append(performance)
    return fitvalue

def function(x):
    return x*x



member = [randint(0,20),randint(0,20),randint(0,20),randint(0,20),randint(0,20) ]
performance_gen =[]

# For 5 generation
for generation in range(5):
    print("generation : " +str(generation)+" members " + str(member))

    fitval = fitness(member)
    print("Fitness value "+ str(fitval))

    new_member = selection(fitval)
    print("Selected member for next gen "+ str(new_member))

    member = mutation(new_member)
    print("After Mutated " + str(member))

    performance_gen.append(max(fitness(member)))


print("Highest value " + str((max(fitness(member)))))




