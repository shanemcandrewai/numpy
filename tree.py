t3 = np.zeros(48, np.int16).reshape(6, 2, 4)
t3[:,:,0] = np.transpose([[6, 4, 3, 9, 1, 7], [0, 0, 1, 2, 3, 2]])
t3[:,1,1] = t3[t3[:,1,0],1,0]
t3[:,1,2] = t3[t3[:,1,1],1,0]
t3[:,1,3] = t3[t3[:,1,2],1,0]

import numpy as np
from numpy.random import default_rng
rng = default_rng()

a = np.empty(100, np.int32)
with np.nditer(a, flags=['c_index'], op_flags=['readwrite']) as it:
    for x in it:
        if it.index == 0:
            x[...] = 0
        elif it.index < 10:       
            x[...] = rng.integers(it.index)
        else: 
            x[...] = it.index - rng.integers(10) - 1
print(a)
from scipy import stats
np.histogram(a, bins=100, range=[0, 100])
