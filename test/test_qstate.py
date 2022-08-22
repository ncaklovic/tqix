# from tqix import *
# import numpy as np
# from tqix.pis import *

# N = 3

# print('test circuit')
# qc = circuit(N)
# state = qc.state
# print(state)
# print(typex(state))

# print('test gate with initial state')
# qc.RZ(np.pi/3)
# print(qc.state)

from tqix import *
from tqix.pis import *
import numpy as np
N = 20 #qubits
theta=0.4
phi=0.3
qc = circuit(N,use_gpu=True)
omega = N*theta
qc.TNT(theta,omega=omega,gate_type="ZX")
prob = qc.measure(num_shots=1000)
#to get state information
# psi = qc.state #sparse matrix
# psi = qc.state.toarray() #full matrix
print(prob.sum())