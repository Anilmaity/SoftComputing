''' Use gatool to maximize the function 𝑓(𝑥1, 𝑥2
) = 4𝑥1 + 5𝑥2, within the range 1 to 2.
'''

from random import random
import random
def mutation(member):
    mutate_member = []
    for mem in member:
        mutate = round(random.uniform(1,2),4)
        mutate_side = round(random.uniform(-1,1),0)
        #print(mutate,mutate_side)

        if (mem[0]+(mutate*mutate_side) < 1 and mem[0]+(mutate*mutate_side) > 2):
            mem1 = mem[0] + (mutate*mutate_side)
        else:
            mem1 = mem[0]

        if (mem[1]+(mutate*mutate_side) < 1 and mem[1]+(mutate*mutate_side) > 2):
            mem2 = mem[1] + (mutate*mutate_side)
        else:
            mem2 = mem[1]

        m_member = [mem1,mem2]

        mutate_member.append(m_member)




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
        performance = function(mem[0],mem[1])
        fitvalue.append(performance)
    return fitvalue

def function(x1,x2):
    return 4*x1 + 5*x2



member = [[round(random.uniform(1,2),4),round(random.uniform(1,2),4)],
          [round(random.uniform(1, 2),4), round(random.uniform(1, 2),4)],
          [round(random.uniform(1,2),4),round(random.uniform(1,2),4)],
          [round(random.uniform(1,2),4),round(random.uniform(1,2),4)],
          [round(random.uniform(1,2),4),round(random.uniform(1,2),4)]]
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


print("Highest value  " + str((max(fitness(member)))))




