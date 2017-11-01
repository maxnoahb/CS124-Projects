#!/usr/bin/env python

import math 
import random
import prepartition_solution
import standard_solution
import time
from sys import argv

MAX_ITER = 25000

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

# run the tests and time
def tests():

	# open the test file of numbers and write them into a list
	with open(argv[1]) as f:
		num_list = f.readlines()
	num_list = [x.strip('\n') for x in num_list]
	num_list = [int(x) for x in num_list]

	# run each of the 7 algorithms to find the residue, and time each
	t0 = time.time()
	kk = str(karmarkar_karp(num_list))
	kk_time = str(time.time() - t0)

	# t1 = time.time()
	# std_RR = str(standard_solution.repeated_random(num_list))
	# std_RR_time = str(time.time() - t1)

	# t2 = time.time()
	# std_HC = str(standard_solution.hill_climbing(num_list))
	# std_HC_time = str(time.time() - t2)

	# t3 = time.time()
	# std_SA = str(standard_solution.simulated_annealing(num_list))
	# std_SA_time = str(time.time() - t3)

	# t4 = time.time()
	# prepart_RR = str(prepartition_solution.repeated_random(num_list))
	# prepart_RR_time = str(time.time() - t4)

	# t5 = time.time()
	# prepart_HC = str(prepartition_solution.hill_climbing(num_list))
	# prepart_HC_time = str(time.time() - t5)

	# t6 = time.time()
	# prepart_SA = str(prepartition_solution.simulated_annealing(num_list))
	# prepart_SA_time = str(time.time() - t6)

	print "Karmarkar-Karp Result: " + kk + ", " + "Runtime: " + kk_time
	# print "Standard Repeated Random Result: " + std_RR + ", " + "Runtime: " + std_RR_time
	# print "Standard Hill Climbing Result: " + std_HC + ", " + "Runtime: " + std_HC_time
	# print "Standard Simulated Annealing Result: " + std_SA + ", " + "Runtime: " + std_SA_time
	# print "Prepartition Repeated Random Result: " + prepart_RR +  ", " +"Runtime: " + prepart_RR_time
	# print "Prepartition Hill Climbing Result: " + prepart_HC +  ", " +"Runtime: " + prepart_HC_time
	# print "Prepartition Simulated Annealing Result: " + prepart_SA + ", " + "Runtime: " + prepart_SA_time
	
	

tests()