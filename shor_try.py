import math
import random
# import sys
from fractions import Fraction
from builtins import input
import math

def initialize_qubits(given_circuit, n, m):
    ''' initialize the qubits in the circuit. put the first n qubits into superposition with the hadamard
    gate and turn the last qubit into a controlled qubit, being at |1>'''
    given_circuit.h(range(n))
    given_circuit.x(n+m-1)


def find_period(a, N):
    ''' find the period of a^r%N=1
    this replaces the quantum part of shor's algorithm because quantum computers are weak for now
    '''
    i = 2
    while (a**i)%N!=1:
        i+=1
    return i
    


def shor(N, attempts = 1):
    
    # build compilation engine list
    # rule_set = DecompositionRuleSet(modules=[projectq.libs.math,
    #                                          projectq.setups.decompositions])
    # compilerengines = [AutoReplacer(rule_set),
    #                    InstructionFilter(high_level_gates),
    #                    TagRemover(),
    #                    LocalOptimizer(3),
    #                    AutoReplacer(rule_set),
    #                    TagRemover(),
    #                    LocalOptimizer(3)]

    # # make the compiler and run the circuit on the simulator backend
    # eng = MainEngine(Simulator(), compilerengines)
    


    for attempt in range(attempts):
        print("-----------------------------------")
        print("\nAttempt #" + str(attempt))
        
        a = random.randint(0, N)
        print("Random x between 0 and N-1 --> ", str(a))
        
        '''If the GCD is not 1, x is a nontrivial factor of N, so we're done'''
        if (math.gcd(a, N) != 1):
            print("\nFactors found classically, re-attempt...")
            continue
        
        '''Otherwise it means that x and N are coprime
        Here the quantum part starts: Shor's algorithm tries to find r, the period of x^a mod n, where n is 
        the number to be factored and x is an integer coprime to n.
        It is important to underline the r  is the smallest positive integer such that x^r = 1 mod N
        '''
        r = find_period(a, N)
        
        '''If r is odd or if x^r/2 = -1 (mod N), choose another x
        EXPLANATION: we already know that x^r/2 is NOT congruent to 1 (mod N), otherwise the order of x would be r/2,
        instead of r. So we have to check only that x^r/2 is NOT congruent to -1 (mod N)
        '''
        if ((r % 2 != 0) or (pow(a, int(r/2), N) == -1)): 
            print("r is odd or x^r/2 = -1 (mod N), re-attempt...")
            continue
            
        print("\nPeriod found: " + str(r))
        
        p = math.gcd(a**int(r / 2) + 1, N)
        q = math.gcd(a**int(r / 2) - 1, N)
        
        if ((not p * q == N) and p * q > 1 and int(1. * N / (p * q)) * p * q == N):
            p, q = p * q, int(N / (p * q))
        if p * q == N and p > 1 and q > 1:
            print("\nFactors found: {} * {} = {}.".format(p, q, N))
            return (p, q)
        else:
            print("\nBad luck: Found {} and {}".format(p, q))




print(shor(35))