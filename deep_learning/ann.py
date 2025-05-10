import numpy as np 

SEED = 1
rng = np.random.default_rng(seed=SEED)

class Linear():
    def __init__(self, n_int, n_out):
        self.mat = rng.random(size = (n_int, n_out))

class Network():
    def __init__(self, )