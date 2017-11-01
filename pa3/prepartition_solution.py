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

# gives a random partition of length n
def random_partition(n):
	rp = [random.randint(0,n-1) for i in range(0,n)]
	return rp

# given a list of numbers and solution, properly give the partition
def calculate_partition(num_list, solution):
	
	# copy the solution as to not change it
	p = list(solution)
	a_prime = []

	# populate the A' list with 0s 
	for i in range(0,len(num_list)):
		a_prime.append(0)

	# add to the A' list, giving the partition
	for j in range(0,len(num_list)):
		a_prime[p[j]] += int(num_list[j])

	return a_prime

# gives the residue after giving a partitioned array
def residue(num_list, solution):
	res = karmarkar_karp(calculate_partition(num_list, solution))
	return res

# given a solution, gives the solution of a random neighbor
def random_neighbor(solution):
	
	# choose a random index to swap
	indices = range(len(solution))
	to_swap = random.choice(indices)

	# per the spec, ensure j is picked so that p_i =/= j, and swap
	indices.remove(solution[to_swap])
	new_set = random.choice(indices)
	solution[to_swap] = new_set
	
	return solution

def repeated_random(num_list):

	# start with a random solution and give its residue
	rand_solution = random_partition(len(num_list))
	rand_residue = residue(num_list, rand_solution)

	# for 25,000 iterations
	for i in range(1, MAX_ITER):

		# check a new random solution and give its residue
		new_solution = random_partition(len(num_list))
		new_residue = residue(num_list, new_solution)

		# if the test solution is less than the best solution so far, then
		# update the best solution (rand_solution)
		if new_residue < rand_residue:
			rand_solution = new_solution
			rand_residue = new_residue

	return rand_residue


def hill_climbing(num_list):

	# start with a random solution and give its residue
	rand_solution = random_partition(len(num_list))
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
	rand_solution = random_partition(len(num_list))
	rand_residue = residue(num_list, rand_solution)

	# in order to keep track of the best solution so far (S'' in the assignment spec)
	best_solution = rand_solution
	best_residue = rand_residue

	# for 25,000 iterations
	for i in range(0, MAX_ITER):

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
			best_residue = rand_residue

	return best_residue
