#!/usr/bin/env python
# -*- coding: utf-8 -*-

age = int(raw_input("How old are you? "))
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, and 3 years later, %r old, %r tall and %r heavy." % (
    age, age+3, height, weight)