from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, SparsePauliOp
from qiskit.visualization import plot_histogram
import numpy as np
import random

# 1. Prepare the Bell state
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

# 2. Copy circuit and rotate qubit 1 to X basis
meas_qc = qc.copy()
meas_qc.h(0)        # Rotate qubit 1 to X basis
meas_qc.measure_all()

# 3. Get statevector and simulate 30 measurements manually
psi = Statevector.from_instruction(meas_qc.remove_final_measurements(inplace=False))
samples = psi.sample_counts(shots=30)

# 4. Reformat the results
def bit_to_eigenvalue(bitstring):
    # bitstring: qubit 1 is leftmost, qubit 2 is rightmost
    # Qubit 1: measured in X basis, values '0' -> +1, '1' -> -1
    # Qubit 2: measured in Z basis, values '0' -> +1, '1' -> -1
    x = 1 if bitstring[0] == '0' else -1
    z = 1 if bitstring[1] == '0' else -1
    return x * z

# Expand the counts into individual samples
measurements = []
for bitstring, count in samples.items():
    for _ in range(count):
        measurements.append((bitstring, bit_to_eigenvalue(bitstring)))

# 5. Print each measurement
print("Individual measurements:")
for b, val in measurements:
    print(f"{b} → value: {val}")

# 6. Compute stats
values = [val for _, val in measurements]
avg = np.mean(values)
std = np.std(values)

print(f"\nEstimated average value: {avg}")
print(f"Estimated standard deviation: {std}")
