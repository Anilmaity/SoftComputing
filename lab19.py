

from random import randint

def mutation(member):
    mutate_member = []
    for mem in member:
        mutate = randint(-6,0)
        mutate_side = randint(-1,1)
        #print(mutate,mutate_side)
        if (mem+(mutate*mutate_side) < 0 and mem+(mutate*mutate_side) > -6):
            mutate_member.append(mem + (mutate*mutate_side))
        else:
            mutate_member.append(mem)


    return mutate_member






def selection(fitnessvalue):
    # Roulette Wheel Selection
    new_member = []
    for mem in range(len(fitnessvalue)):
        if fitnessvalue[mem] == min(fitnessvalue):
            new_member_type =  member[mem]
            new_member = [new_member_type,new_member_type,new_member_type,new_member_type,new_member_type]


    return new_member




def fitness(members):
    fitvalue = []
    for mem in members:
        performance = function(mem)
        fitvalue.append(performance)
    return fitvalue

def function(x):
    return x*x + 3*x + 2



member = [randint(-6,0),randint(-6,0),randint(-6,0),randint(-6,0),randint(-6,0) ]
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


print("Lowest value " + str((min(fitness(member)))))




