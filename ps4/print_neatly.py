# CS 124 Problem Set 4, Question 4
# HARVARD ID: 10939860
# March 3, 2017

import math
import sys

M = 40

# open the file
file = open('buffy.txt', 'r').read()

# obtain a list of all words in the file and find the number of words
word_list = file.split()
word_count = len(word_list)

def chars_on_line(words,i,j):
	sum = 0
	for a in xrange(i, j):
		sum += len(words[a])
	return sum

def penalty(words,i,j):
	return (abs((M - j + i -chars_on_line(words,i,j))) ** 3)

def line_cost(words,cost,j):
	new_cost = []
	new_cost.append(0)
	i = 1
	while (i < j):
		new_cost.append(new_cost[i-1] + penalty(words,i,j))
		i += 1
	return new_cost

# find the minimum i to start the line that ends at j
def min_line_start(words, cost, j):
	new_cost = line_cost(words,cost,j)
	i = new_cost.index(min(new_cost))
	return i

# choose which start indices to use from existing array
def find_opt_breaks(starts, p):
	i = p[starts[len(starts)-2]-1]
	if i > M:
		starts.append(p[starts[len(starts)-2]-1])
		find_opt_breaks(starts, p)
	else:
		starts.append(0)
		return starts


def pretty_print(excerpt):
	cost = []
	p = []
	i = word_count
	j = word_count

	for i in xrange(0, j+1):
		cost.append(float('inf'))
		p.append(0)

	for i in xrange(0, j+1):
		if M >= chars_on_line(word_list, word_count - i, word_count):
			cost[i] = 0
	
	while j > 0:
		cost[j] = penalty(word_list, min_line_start(word_list, cost, j), j)
		p[j] = min_line_start(word_list, cost, j)
		j -= 1

	starts = [p[word_count]]
	find_opt_breaks(starts,p)
	starts = list(reversed(starts))

	# add up all penalties and print
	final_penalty = 0
	counter = 0
	while (counter < (len(starts) - 1)):
		final_penalty += penalty(word_list, starts[counter], starts[counter+1]-1)
		for i in xrange(starts[counter], starts[counter+1]-1):
			print word_list[i],
		counter += 1
	for i in xrange(starts[len(starts) - 1], word_count):
		print word_list[i],
	print ' '
	print final_penalty

pretty_print(file)