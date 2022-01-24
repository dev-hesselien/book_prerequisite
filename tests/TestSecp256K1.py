import unittest 
from src.Encryption import *
class TestSecp256K1c(unittest.TestCase):
    
    def test_generate_private_key(self) :
        keyClass = Secp256k1()
        privateKey = keyClass.get_private_key()
        test = keyClass.get_signature_from_private_key(privateKey, b"hello")
        self.assertIsInstance(test, bytes)
    
    def test_get_public_key(self):
        keyClass = Secp256k1()
        # private key
        private_key = keyClass.get_private_key()
        # signature 
        signature = keyClass.get_signature_from_private_key(private_key, b'hello')
        public_key = keyClass.get_public_key(private_key)
    
    def test_get_private_key(self):
        keyClass = Secp256k1()
        private_key = keyClass.get_private_key()
        number = private_key