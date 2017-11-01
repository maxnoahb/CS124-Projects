import math 
import random

MAX_ITER = 25000

def T(i): 
	return (10**10) * ((0.8) ** math.floor(i / 300))

# runs the karmarkarp algorithm as seen from pseudocode in class
def karmarkar_karp(num_list):
	
	# make a copy of the list, as not to edit it as we go
	list_copy = list(num_list)

	# run the loop until there is only one element remaining
	while(len(list_copy) > 1):

		# find the max element in the list and set it to 0
		v1 = max(list_copy)
		v1index = list_copy.index(v1)
		list_copy[v1index] = 0

		# find the second largest element in the list, and then set it
		# to the difference between it and the initial max element
		v2 = max(list_copy)
		list_copy[v1index] = v1 - v2
		list_copy.remove(v2)

	return list_copy[0]

# generates an array of size n of random +1 and -1s
def standard_representation(n):
	solution = []
	for i in range(n):
		if random.random() < 0.5:
			solution.append(1)
		else: 
			solution.append(-1)
	return solution

# finds the residue, given an array of numbers and the array of random +1s and -1s
def residue(num_list, std_rep):
	
	# initialize residue to 0 
	res = 0

	# add up the residue and return the absolute value
	for i in range(len(num_list)):
		res += (int(num_list[i]) * std_rep[i])

	return math.fabs(res)

# returns a neighbor solution, given a solution
def random_neighbor(std_rep):
	
	# find 2 random indices
	ind = random.sample(range(0,len(std_rep)), 2)

	# negate one of the two values
	std_rep[ind[0]] *= -1

	# negate the other of the two with probability 1/2
	if (random.random() < 0.5):
		std_rep[ind[1]] *= -1

	return std_rep

def repeated_random(num_list):

	# start with a random solution and give its residue
	rand_solution = standard_representation(len(num_list))
	rand_residue = residue(num_list, rand_solution)

	# for 25,000 iterations
	for i in range(1, MAX_ITER):

		# check a new random solution and give its residue
		new_solution = standard_representation(len(num_list))
		new_residue = residue(num_list, new_solution)

		# if the test solution is less than the best solution so far, then
		# update the best solution (rand_solution)
		if new_residue < rand_residue:
			rand_solution = new_solution
			rand_residue = new_residue

	return rand_residue


def hill_climbing(num_list):

	# start with a random solution and give its residue
	rand_solution = standard_representation(len(num_list))
	rand_residue = residue(num_list, rand_solution)

	# for 25,000 iterations
	for i in range(1, MAX_ITER):

		# check a new random neighbor's solution and give its residue
		new_solution = random_neighbor(rand_solution)
		new_residue = residue(num_list, new_solution)

		# if the test solution is less than the best solution so far, then
		# update the best solution (rand_solution)
		if new_residue < rand_residue:
			rand_solution = new_solution
			rand_residue = new_residue

	return rand_residue

def simulated_annealing(num_list):
	
	# start with a random solution and give its residue
	rand_solution = standard_representation(len(num_list))
	rand_residue = residue(num_list, rand_solution)

	# in order to keep track of the best solution so far (S'' in the assignment spec)
	best_solution = rand_solution
	best_residue = rand_residue

	# for 25,000 iterations
	for i in range(1, MAX_ITER):

		# check a new random neighbor's solution and give its residue
		new_solution = random_neighbor(rand_solution)
		new_residue = residue(num_list, new_solution)

		if new_residue < rand_residue:
			rand_solution = new_solution
			rand_residue = new_residue
		elif (random.random() < math.exp(-(new_residue - rand_residue)/T(i))):
			rand_solution = new_solution
			rand_residue = new_residue
		if rand_residue < best_residue:
			best_solution = rand_solution
			best_residue = new_residue

	return best_residue
