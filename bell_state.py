from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

def create_bell_state():
    # Create quantum circuit with 2 qubits and 2 classical bits
    circuit = QuantumCircuit(2, 2)
    
    # Create Bell State (|00⟩ + |11⟩)/√2
    circuit.h(0)    # Apply Hadamard gate to first qubit
    circuit.cx(0, 1)  # Apply CNOT gate with control=0 and target=1
    
    # Measure both qubits
    circuit.measure([0, 1], [0, 1])
    
    return circuit

def main():
    # Create the Bell State circuit
    bell_circuit = create_bell_state()
    
    # Print the circuit
    print("Bell State Circuit:")
    print(bell_circuit)
    
    # Execute the circuit on simulator
    simulator = AerSimulator()
    job = simulator.run(bell_circuit, shots=1000)
    result = job.result()
    
    # Get the counts of measurement results
    counts = result.get_counts(bell_circuit)
    
    # Plot the results
    fig = plot_histogram(counts)
    plt.show()
    
    print("\nMeasurement Results:")
    for state, count in counts.items():
        print(f"State |{state}⟩: {count} shots")

if __name__ == "__main__":
    main() 