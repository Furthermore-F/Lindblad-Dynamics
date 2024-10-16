import numpy as np
import qiskit
import re 
from qiskit.circuit.library import EfficientSU2
from qiskit.quantum_info import SparsePauliOp
from qiskit.circuit import QuantumCircuit, ParameterVector

# SciPy minimizer routine
from scipy.optimize import minimize

# Plotting functions
import matplotlib.pyplot as plt

if __name__ == '__main__':


    def parse_gate(circuit, command):
        if re.match(r"H\((.*)\)", command):
            qubit = int(command[2])
            circuit.h(qubit)
        elif re.match(r"X\((.*)\)", command):
            qubit = int(command[2])
            circuit.x(qubit)
        elif re.match(r"R\((.*),(.*)\)", command):
            params = re.findall(r"R\((.*),(.*)\)", command)[0]
            angle = float(params[0])  
            qubit = int(params[1])   
            circuit.rx(angle, qubit)  
        elif re.match(r"CX\((.*),(.*)\)", command):
            params = re.findall(r"CX\((.*),(.*)\)", command)[0]
            control_qubit = int(params[0])
            target_qubit = int(params[1])
            circuit.cx(control_qubit, target_qubit)
        elif re.match(r"M\((.*)\)", command):
            qubit = int(re.findall(r"M\((.*)\)", command)[0])
            circuit.measure(qubit, qubit)
        else:
            raise ValueError(f"Not Found: {command}")

    def create_circuit_from_string(input_str, qubit_num, bit_num):
        circuit = QuantumCircuit(qubit_num, bit_num)
        commands = input_str.split(',')
        for command in commands:
            parse_gate(circuit, command.strip())
        
        return circuit

    input_str = "H(0), X(1), X(1), X(2)"
    param_num = 4
    circuit = create_circuit_from_string(input_str, 4, 0)

    print(circuit.draw())

    delta = 12
    omega = 1
    hamiltonian = SparsePauliOp.from_list(
    [("Z", omega/2), ("X", -delta/2)]
    )

    layer_number = 2
    theta_list = ParameterVector('θ', length=3*layer_number)

    circ = QuantumCircuit(1)

    for i in range(layer_number):
        circ.rx(theta_list[i*3], 0)
        circ.ry(theta_list[i*3+1], 0)
        circ.rz(theta_list[i*3+2], 0)
    circ.draw("mpl", style="iqp")
    plt.show()


    def m_matrix(param_num, ):
        m = np.identity(n=param_num)

        for i in range(param_num):
            for j in range(i, param_num):
                0




        return 0
    
    def v_vector():


        return 0



    num_params = circ.num_parameters
    print(num_params)