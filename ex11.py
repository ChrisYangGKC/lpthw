#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "How old are you"
age = int(raw_input())

print "How tall are you"
height = raw_input()

print "How much do you weight"
weight = raw_input()

print "So, you're %r old, and %d years old 5 years later,  %r tall and %r heavey." % (
	age, age+5, height, weight)
