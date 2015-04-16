# -*- coding: utf-8 -*-

''' 2-Charactor Markov Chain for Documentation
..  module:: A Python module for 2-character markov chain using pykov.
    :platform: Unix, Windows, Mac
..  moduleauthor:: Jaehyeon Lee <bitpresso@gmail.com>
'''

from __future__ import print_function

import string, re
import math, random
import os
import sys

import six
import pykov

class Data:
    statelist = list('abcdefghijklmnoprstuvwxyz ')
    matrix = pykov.Matrix()

    def update(self, string):
        ''' Update a number of the state transition data matrix
        '''
        # let all characters move to lowercase and update only characters
        # in states list because uppercase and special characters are not
        # important feature to compose meaningful word in the sentence
        prev = None
        for curr in string.lower():
            if curr in self.statelist:
                if prev:
                    self.matrix[prev, curr] += 1
                prev = curr
            else:
                prev = None

    def add_files(self, filelist):
        ''' Update the state transition data matrix from files
        '''
        for filename in filelist:
            with open(filename) as f:
                print('Add text from', filename)
                count = 0
                for line in f:
                    self.update(line)
                    count += 1
                    print('\r  Add', count, 'lines ...', end='')
                    sys.stdout.flush()
                print('\nCompleted!')

    def add_sentences(self, sentences):
        ''' Update the state transition data matrix from sentences
        '''
        string = ' '.join(sentences)
        self.update(string)

    def view(self):
        ''' Pretty print the state transition data matrix
        '''
        # set s1 and s2 indexes
        s1list = s2list = sorted(self.matrix.states())
        s2indexes = len(s2list) + 1

        # print table header
        print('-------- ' * s2indexes)
        print(' s1 -->  ', end='')
        for s2 in s2list:
            print(' s2 \'%s\' ' % s2, end=' ')
        print()
        print('-------- ' * s2indexes)
        # print table body
        for s1 in s1list:
            print(' num \'%s\' ' % s1, end='')
            for s2 in s2list:
                print('%8d' % self.matrix[s1, s2], end=' ')
            print('sum=%d' % self.matrix.succ(s1).sum())
            print('-------- ' * s2indexes)
        # print table footer
        print()


class Probability:
    def __init__(self, data=None):
        ''' Initialize the state transition probability matrix of markov chain

            This matrix use a data matrix made by data class or load matrix file
            to compose a probability matrix.
        '''
        # if data matrix loaded, normalize the matrix to convert probability
        # matrix
        if data:
            self.matrix = pykov.Chain(data.matrix)
            self.stochastic()
        # if not, create new empty matrix
        else:
            self.matrix = pykov.Chain()

    def stochastic(self):
        ''' Normalize the state transition probability matrix
        '''
        # when the matrix is normalized, raise exception from pykov if state
        # transition value of a specific character is 0
        try:
            self.matrix.stochastic()
        except pykov.PykovError:
            t, e = sys.exc_info()[:2]
            sys.stderr.write('ERROR: pykov.Matrix.stochastic(): %s\n' % e)
            sys.stderr.write('ERROR: not enough sentences to make matrix!\n')
            sys.exit(1)

    def check(self, sentences):
        ''' Check if sentence is awkward using the state transition probability
            matrix
        '''
        print('----------' * 8);
        string = ' '.join(sentences)
        print('%s' % string)
        print('----------' * 8);
        string = re.sub('[^a-zA-Z\ ]', ' ', string)
        string = string.lower()
        #print('%s' % string)
        #print('----------' * 8);
        p = self.matrix.walk_probability(list(string))
        probability = math.exp(p)
        if probability == 0:
            print('This sentence is [awkward]!\n')
        else:
            print('This sentence is natural!\n')

    def feeling_lucky(self):
        # generate random sentence
        steps = random.randint(10, 70)
        string = ''.join(self.matrix.walk(steps))
        print('[I\'m Feeling Lucky] What about the following sentence to use?')
        print('----------' * 7);
        print('%s.' % string)
        print('----------' * 7);

    def save(self, filename):
        ''' Save the state transition probability matrix to file.
        '''
        print('Save matrix to', filename)
        with open(filename, mode='w') as f:
            count = 0
            for key, value in six.iteritems(self.matrix):
                tmp = format("%c|%c|%f\n" %
                        (key[0], key[1], value))
                f.write(tmp)
                count += 1
                print('\r  Store', count, 'items ...', end='')
                sys.stdout.flush()
        print('\nCompleted!')

    def load(self, filename):
        ''' Load the state transition probability matrix from file
        '''
        print('Load matrix from', filename)
        with open(filename) as f:
            count = 0
            for line in f:
                tmp = line.split('|')
                self.matrix[tmp[0], tmp[1]] = float(tmp[2])
                count += 1
                print('\r  Restore', count, 'items ...', end='')
                sys.stdout.flush()
        print('\nCompleted!')

    def view(self):
        ''' Pretty print the state transition probability matrix
        '''
        # set s1 and s2 indexes
        s1list = s2list = sorted(self.matrix.states())
        s2indexes = len(s2list) + 1

        # print table header
        print('-------- ' * s2indexes)
        print(' s1 -->  ', end='')
        for s2 in s2list:
            print(' s2 \'%s\' ' % s2, end=' ')
        print()
        print('-------- ' * s2indexes)
        # print table body
        for s1 in s1list:
            print(' num \'%s\' ' % s1, end='')
            for s2 in s2list:
                print('%f' % self.matrix[s1, s2], end=' ')
            print()
            print('-------- ' * s2indexes)
        # print table footer
        print()
