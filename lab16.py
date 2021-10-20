from fuzzypy.variables import *

# Create a fuzzy variable
dirtyness_of_cloth = FuzzyVariable()# dirtyness

# Define the membership functions
dirty = TriFunc(20, 25, 50)
norm = TriFunc(15, 20, 25)
clean = TrapecFunc(0, 5, 10, 20)

# Determine the fuzzy terms
spin_speed_high = dirtyness_of_cloth.is_(dirty)  # The cloth is dirty
spin_speed_normal = dirtyness_of_cloth.is_(norm)  # The cloth is normal
spin_speed_low = dirtyness_of_cloth.is_(clean)  # The cloth is clean

# Create an output fuzzy variable
fuzzy_spin = FuzzyVariable()  # The speed of the fan

# and its membership functions
slow = TriFunc(0, 0, 750)
fast = TriFunc(250, 1000, 1000)

# Determine the rules
spin_slow = FuzzyRule(spin_speed_low | spin_speed_normal, fuzzy_spin, slow)  # If the dirtyness is clean or normal then spin speed is slow
spin_fast = FuzzyRule(spin_speed_high, fuzzy_spin, fast)  # If the dirtyness is dirty then fan speed is fast

# dirty
dirtyness_of_cloth.value = 30

# Lets find the limits of the variables
print("dirtyness lower limit is {}".format(dirtyness_of_cloth.low_limit))
print("dirtyness upper limit is {}".format(dirtyness_of_cloth.upp_limit))
print("spin speed lower limit is {}".format(fuzzy_spin.low_limit))
print("spin speed upper limit is {}".format(fuzzy_spin.upp_limit))

print("The dirtyness is {}".format(dirtyness_of_cloth.value))
fan_speed = apply_defuzzyfy_COG([spin_slow, spin_fast])  # then the fan speed is
print("Defuzzyfied values are {}".format(fan_speed))  # it could be more then one value
print("Or defuzzyfied fan speed is {}".format(fuzzy_spin.value))  # and we can check the value of the fan sin directly

dirtyness_of_cloth.value = 10
apply_defuzzyfy_COG([spin_slow, spin_fast])
print("Now the dirtyness is {}, and the spin speed is {}".format(dirtyness_of_cloth.value, fuzzy_spin.value))  # and print it
