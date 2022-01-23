import unittest 
from Signer import *
from DataStructure import *

class TestMerkleTree(unittest.TestCase):

    def test_data_structure(self):
        dataStructure  = DataStructure()
        data = dataStructure.data('foo')
        
        self.assertEqual(['foo'], data)

if __name__ == '__main__':
    unittest.main()