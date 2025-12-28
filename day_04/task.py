import random

friends = ['Alice','Bob','Charlie','David','Emanuel']

#print(len(friends))

#print(random.randint(0,4))

random_number = random.randint(0,4)

if random_number == 0:
    print(friends[0])
elif random_number == 1:
    print(friends[1])
elif random_number == 2:
    print(friends[2])
elif random_number == 3:
    print(friends[3])
else:
    print(friends[4])

#2nd option
print(random.choice(friends))
