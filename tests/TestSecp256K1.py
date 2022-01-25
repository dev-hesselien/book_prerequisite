import unittest
from src.Encryption import *
class TestSecp256K1c(unittest.TestCase):
    
    def test_generate_signature_for_private_key(self) :
        keyClass = Secp256k1()
        privateKey = keyClass.get_private_key()
        test = keyClass.define_signature_from_private_key(privateKey, b"hello")
        self.assertIsInstance(test, bytes)
    
    def test_get_public_key(self):
        keyClass = Secp256k1()
        # private key
        private_key = keyClass.get_private_key()
        # signature 
        signature = keyClass.define_signature_from_private_key(private_key, b'hello')
        public_key = keyClass.get_public_key(private_key)
        self.assertIsInstance(public_key, bytes)
    
    def test_get_private_key(self):
        keyClass = Secp256k1()
        private_key = keyClass.get_private_key()
        self.assertIsInstance(private_key, EllipticCurvePrivateKey)
    

    def test_generate_address_from_public_key(self):
        keyClass = Secp256k1()
        private_key = keyClass.get_private_key()
        public_key = keyClass.get_public_key(private_key)
        test_generate_bitcoin_address = keyClass.generate_bitcoin_address(public_key)
        self.assertEqual('test', test_generate_bitcoin_address)


