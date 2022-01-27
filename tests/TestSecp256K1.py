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
        hash_class = Secp256k1()
        private_key = hash_class.get_private_key()
        public_key = hash_class.get_public_key(private_key)
        test_hash_public_key_in_sha256_address = hash_class.hash_public_key_in_sha256_(public_key)
        self.assertIsInstance(test_hash_public_key_in_sha256_address, str)


    def test_hash_derived_hashed_publick_key_in_ripemd160(self):
        hash_class = Secp256k1()
        test_hash_derivied_hashed_public_key_in_ripemd160 = hash_class.hash_derived_hashed_public_key_in_ripemd160('str²')
        self.assertIsInstance(test_hash_derivied_hashed_public_key_in_ripemd160, str)

    def test_base_58_encode_public_key(self):
        hash_class = Secp256k1()
        private_key = hash_class.get_private_key()
        public_key = hash_class.get_public_key(private_key)
        hash = hash_class.hash_public_key_in_sha256_(public_key)
        double_hashed_public_key = hash_class.hash_derived_hashed_public_key_in_ripemd160(hash)
        test_base_58_encode_public_key = hash_class.base_58_encode_public_key(double_hashed_public_key)
        self.assertIsInstance(test_base_58_encode_public_key, bytes)