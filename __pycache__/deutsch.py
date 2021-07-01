import numpy as np 
from qiskit import QuantumCircuit, execute, IBMQ, BasicAer
from qiskit.providers.ibmq import least_busy
from qiskit.tools.jupyter import *

from qiskit.visualization import plot_histogram

def dj_oracle(case, n):
    # to return the output, the oracle needs to create it's own quantum circuit
    oracle_circuit = QuantumCircuit(n+1) # i create a quantum circuit with n+1 (control one) qubits all set to 0
    
    if case == 'balanced': # this gate will work on each of the qubits one by one, and make sure 
        # it always evens them. so if there is an even 
        for i in range(n):
            oracle_circuit.cx(i,n)

    if case == 'constant':
        output = np.random.randint(2)
        if output == 1: #randomize the output
            oracle_circuit.x(n)
    
    oracle_gate = oracle_circuit.to_gate()
    oracle_gate.name = 'Oracle'
    return oracle_gate

def dj_algorithm(n, case = 'balanced'):
    '''
    building the circuit, preparing the qubits, going through the oracle and running the algorithm
    deutsch algorithm 
    '''

    # n + 1 qubits, and n bits
    dj_circuit = QuantumCircuit(n+1, n) 
    
    # preparing qubits
    for qubit in range(n):
        dj_circuit.h(qubit)

    # controlled qubit
    dj_circuit.x(n)
    dj_circuit.h(n)

    # apply the oracle 
    oracle = dj_oracle(case, n)
    dj_circuit.append(oracle, range(n+1))

    # measurements
    for i in range(n):
        dj_circuit.h(i)
        dj_circuit.measure(i,i)
    return dj_circuit

def main():
    # choose how many qubits to enter 
    n = 5
    # choose what case is the oracle
    case = 'constant' 
    # build the circuit
    circuit = dj_algorithm(n, case)
    # and draw it
    print(circuit)
    # get a backend to run the algorithm
    backend = BasicAer.get_backend('qasm_simulator')
    # execute the algorithm
    results = execute(circuit, backend = backend).result()
    print(results.get_counts())


if __name__ == '__main__':
    main()