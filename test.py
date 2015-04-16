#!/usr/bin/python

from __future__ import print_function

import os
import sys

import matrix

s1 = matrix.Source()
s1.load('test')
s1.pprint('qa')

t1 = matrix.Transition(s1)
t1.pprint('qa')

s2 = matrix.Source()
s2.addtext('book.txt')
s2.pprint('qa')

quit()

s1 = matrix.Source()
s1.load('test')
s1.pprint('a ')
s1.addtext('book.txt')
s1.pprint('a ')

s2 = matrix.Source()
s2.addtext('book.txt')
s2.pprint('a ')

#trans = matrix.Transition(source)
#source.pprint('a ')

#trans = matrix.Transition(source)
#source.pprint()
#source.pprint('q a')
#source.pprint('+')
#trans.pprint('a')

#source.save('test')

#s = list('thefaa')

#print(s)
#p = m.transition.walk_probability(s)
#print(math.exp(p))
#print('Update transition matrix ...',)
#self.update()
#print('Completed!')
