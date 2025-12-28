#DATA STRUCTURE - ORGANISE AND STORE DATA
#fruits = [item1,item2]

state1 = 'Delaware'
state2 = 'Pennsylvania'

states_of_america = ['Delaware','Pennsylvania','New Jersey','Georgia','Connecticut','Arizona','Alaska','Hawaii'] #ordered
print(states_of_america[0])
print(states_of_america[-1])

states_of_america[1] = 'Pencilvania'
print(states_of_america)

#51st state baby
states_of_america.append('Canada')
print(states_of_america)

states_of_america.extend(['Mexico','Greenland'])
print(states_of_america)


#indexerror 
print(len(states_of_america))
print(states_of_america[10])

num_of_states = len(states_of_america)

#nested lists
fruits = ['mango', 'apple', 'banana']
veg = ['tomato','brinjal']

dirty_dozen = [fruits,veg]
print(dirty_dozen)
