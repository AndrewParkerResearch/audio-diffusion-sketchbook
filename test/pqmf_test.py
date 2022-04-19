import torch

from RAVE.rave.pqmf import PQMF

import unittest

class TestPqmf(unittest.TestCase):

    def test_pqmf_shapes_equal(self):
        signal = torch.randn([1, 1, 131072])
        pqmf = PQMF(100, 128)
        encoded = pqmf(signal)
        decoded = pqmf.inverse(encoded)
        
        #the inverse has the same shape as the original
        self.assertEqual(list(signal.shape), list(decoded.shape))
        

if __name__ == '__main__':
    unittest.main()