# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 20:32:26 2022

@author: NeoChen
"""

import cirq as cq

qc = cq.LineQubit(0)

qc_simulator = cq.Simulator()

qcXGate = cq.X(qc)
qcMGate = cq.measure(qc)

qc_circuit = cq.Circuit(qcXGate,qcMGate)


print(qc_circuit)

qc = cq.LineQubit(2)

simulator = cq.Simulator()

qcXGate = cq.X(qc)
qcMGate = cq.measure(qc)

qc_circuit = cq.Circuit(qcXGate,qcMGate)
qcbit = qc_simulator.run(qc_circuit, repetitions=8)

print(qcbit)

# plot QC Circuit #
# =============================================================================
# for i in range(0, 8) :
#     qc = cq.LineQubit(i)
# 
#     simulator = cq.Simulator()
# 
#     qcXGate = cq.X(qc)
#     qcMGate = cq.measure(qc)
# 
#     qc_circuit = cq.Circuit(qcXGate,qcMGate)
#     print(qc_circuit)
# =============================================================================

# read resoult of bit by list #
# =============================================================================
# qcbit = qc_simulator.run(qc_circuit, repetitions=8)
# tmp = qcbit.data
# print(tmp["2"][5])
# =============================================================================

qcbit = qc_simulator.run(qc_circuit, repetitions=8)

for i in range(5, 20) :
    qc = cq.LineQubit(i)
    
    simulator = cq.Simulator()
    
    qcHGate = cq.H(qc)
    qcMGate = cq.measure(qc)
    
    qc_circuit = cq.Circuit(qcHGate,qcMGate)
    print(qc_circuit)
    
    qcbit = qc_simulator.run(qc_circuit, repetitions=8)
    print(qcbit)
    