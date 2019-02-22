#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-02-22 10:38
# @Author  : ZD Liu

# Written by *** and Eric Martin for COMP9021


'''
See https://en.wikipedia.org/wiki/Deterministic_finite_automaton

We consider as alphabet a set of digits.

We accept partial transition functions (that is, there might be no transition
for a given state and symbol).

With the accepts() function, we will deal with a single accept state rather than
a set of accept states.

In the test cases below, transitions_2 is the wikipedia example
(with 'S1' and 'S2' renamed as 'state_1' and 'state_2', respectively),
so the automaton that with 'state_1' as both initial and unique accept state,
accepts words with an even number of occurrences of 0's.

'''


def describe_automaton(transitions):
    '''
    The output is produced with the print() function.

    # >>> transitions_1 = {('q0', 0): 'q1', ('q1', 1): 'q0'}
    # >>> describe_automaton(transitions_1)
    When in state "q0" and processing "0", automaton's state becomes "q1".
    When in state "q1" and processing "1", automaton's state becomes "q0".

    # >>> transitions_2 = {('state_1', 0): 'state_2', ('state_1', 1): 'state_1',\
    #                      ('state_2', 0): 'state_1', ('state_2', 1): 'state_2'}
    # >>> describe_automaton(transitions_2)
    When in state "state_1" and processing "0", automaton's state becomes "state_2".
    When in state "state_1" and processing "1", automaton's state becomes "state_1".
    When in state "state_2" and processing "0", automaton's state becomes "state_1".
    When in state "state_2" and processing "1", automaton's state becomes "state_2".
    '''
    for e in transitions.keys():
        print('When in state "'+e[0]+'" and processing "'+str(e[1])+'", automaton\'s state becomes "'+transitions[e]+'".')

    pass
    # REPLACE pass ABOVE WITH YOUR CODE
# transitions_2 = {('state_1', 0): 'state_2', ('state_1', 1): 'state_1', ('state_2', 0): 'state_1', ('state_2', 1): 'state_2'}
# describe_automaton(transitions_2)


def transitions_as_dict(transitions_as_list):
    '''
    transitions_as_list is a list of strings of the form 'state_1,symbol:state_2'
    where 'state_1' and 'state_2' are words and 'symbol' is one of the 10 digits.
    We assume that there is at most one 'state_2' for given 'state_1' and 'symbol'.

    # >>> transitions_as_dict(['q0,0:q1', 'q1,1:q0'])
    # {('q0', 0): 'q1', ('q1', 1): 'q0'}
    # >>> transitions_as_dict(['state_1,0:state_2', 'state_1,1:state_1',\
    #                          'state_2,0:state_1', 'state_2,1:state_2'])
    {('state_1', 0): 'state_2', ('state_1', 1): 'state_1', \
('state_2', 0): 'state_1', ('state_2', 1): 'state_2'}
    '''
    transitions = {}
    for e in transitions_as_list:
        l = e.split(':')
        state1_list = l[0].split(',')
        tra_key = (state1_list[0],int(state1_list[1]))
        transitions[tra_key] = l[1]
    # INSERT YOUR CODE HERE
    return transitions
# transitions_as_dict(['state_1,0:state_2', 'state_1,1:state_1','state_2,0:state_1', 'state_2,1:state_2'])

def accepts(transitions, word, initial_state, accept_state):
    '''
    Starting in 'initial_state', if the automaton can process with 'transitions'
    all symbols in 'word' and eventually reach 'accept_state', then the function
    returns True; otherwise it returns False.

    # >>> transitions_1 = {('q0', 0): 'q1', ('q1', 1): 'q0'}
    # >>> accepts(transitions_1, '00', 'q0', 'q1')
    # False
    # >>> accepts(transitions_1, '2', 'q0', 'q0')
    # False
    # >>> accepts(transitions_1, '0101010', 'q0', 'q0')
    # False
    # >>> accepts(transitions_1, '01010101', 'q0', 'q0')
    # True
    # >>> not accepts(transitions_1, '01', 'q0', 'q1') and\
    #     accepts(transitions_1, '010', 'q0', 'q1')
    # True
    #
    # >>> transitions_2 = {('state_1', 0): 'state_2', ('state_1', 1): 'state_1',\
    #                      ('state_2', 0): 'state_1', ('state_2', 1): 'state_2'}
    # >>> accepts(transitions_2, '011', 'state_1', 'state_1')
    # False
    # >>> accepts(transitions_2, '001110000', 'state_1', 'state_1')
    # True
    # >>> accepts(transitions_2, '1011100101', 'state_1', 'state_1')
    # True
    # >>> accepts(transitions_2, '10111000101', 'state_1', 'state_1')
    # False
    '''
    word_list = list(word)
    current_state = initial_state
    for w in word_list:
        tra_key = (current_state,int(w))
        if tra_key in transitions.keys():
            get_state = transitions[tra_key]
            current_state = get_state
        else:
            get_state = False
            break
    if get_state == accept_state:
        print(True)
    else:
        print (False)
    pass
    # REPLACE pass ABOVE WITH YOUR CODE
# transitions_1 = {('q0', 0): 'q1', ('q1', 1): 'q0'}
# accepts(transitions_1, '00', 'q0', 'q1')
# accepts(transitions_1, '2', 'q0', 'q0')
# accepts(transitions_1, '0101010', 'q0', 'q0')
# accepts(transitions_1, '01010101', 'q0', 'q0')
# not accepts(transitions_1, '01', 'q0', 'q1') and accepts(transitions_1, '010', 'q0', 'q1')

transitions_2 = {('state_1', 0): 'state_2', ('state_1', 1): 'state_1', ('state_2', 0): 'state_1', ('state_2', 1): 'state_2'}
accepts(transitions_2, '011', 'state_1', 'state_1')
accepts(transitions_2, '001110000', 'state_1', 'state_1')
accepts(transitions_2, '1011100101', 'state_1', 'state_1')
accepts(transitions_2, '10111000101', 'state_1', 'state_1')
# if __name__ == '__main__':
    # import doctest
    #
    # doctest.testmod()