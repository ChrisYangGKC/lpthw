#!/usr/bin/env python
# -*- coding: utf-8 -*-

def use_print(*args):
	arg1, arg2, arg3, arg4 = args
	print_two(arg1, arg2)
	print_two_again(arg3, arg4)

def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)


def print_two_again(arg1, arg2="234234"):
	print "arg1: %r, arg2: %r" % (arg1, arg2)




# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
    print "I got nothin'."


print_two("Zed","Shaw")
print_two_again("Zed")

use_print("12324","23423","4564356","345467458")
print_one("First!")
print_none()