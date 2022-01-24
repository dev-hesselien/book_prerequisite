import unittest 
from src.Encryption import *
class TestMerkleTree(unittest.TestCase):
    
    def test_generate_private_key(self) :
        keyClass = Secp256k1()
        test = keyClass.create_private_key(b"hello")
        self.assertIsInstance(test, bytes)