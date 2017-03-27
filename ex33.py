#!/usr/bin/env python
# -*- coding: utf-8 -*-


numbers = []

def get_the_numbers_list(j):
	print "at the top i is %d" % j
	the_numbers = []#change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
#	i = 0

	start_set = range(j)
	for i in range(j):
		print "At the top i is %d" % i
		the_numbers.append(i)
#		i+=1

		print "numbers now:", the_numbers
		print "At the bottom is is %d" % i

	return the_numbers


numbers = get_the_numbers_list(3)

print "The numbers:"

for num in numbers:
	print num