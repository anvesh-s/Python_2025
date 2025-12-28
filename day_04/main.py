import random
import my_module

#random integer
random_integer = random.randint(1,10)
print(random_integer)

#random floating point number
random_number_0_to_1 = random.random()*10
print(random_number_0_to_1)

#random float
random_float = random.uniform(1,10)
print(random_float)

#heads or tail
h_t = random.randint(1,2)
if h_t == 1:
    print("heads")
else:
    print("tails")

#indexerror 
