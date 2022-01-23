import unittest 
from src.Signer import *
from src.DataStructure import *

class TestMerkleTree(unittest.TestCase):

    def test_data_structure(self):
        # given 
        dataStructure  = DataStructure()
        data = dataStructure.data('foo')
        #assert 
        self.assertEqual(['foo'], data)
    
    def test_encrypt_data(self):
        # given 
        dataStructure = DataStructure()
        data = dataStructure.data('foo')

        # encrypt message foo within list
        encryption = ""


if __name__ == '__main__':
    unittest.main()