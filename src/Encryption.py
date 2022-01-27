from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePrivateKey
from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurveSignatureAlgorithm
from cryptography.hazmat.primitives.serialization import Encoding
from cryptography.hazmat.primitives.serialization import PublicFormat
from Crypto.Hash import RIPEMD160
import base58
import crypt
import hashlib
class Secp256k1:
    
    def define_signature_from_private_key(self, private_key: EllipticCurvePrivateKey, mnemonic: bytes)-> bytes:
        signature = private_key.sign(mnemonic, ec.ECDSA(hashes.SHA256()))
        return signature
    
    def get_private_key(self) -> EllipticCurvePrivateKey:
        private_key = ec.generate_private_key(
            ec.SECP256K1()
        )
        return private_key
    
    def get_public_key(self, private_key: EllipticCurvePrivateKey) -> bytes:
        public_key = private_key.public_key().public_bytes(Encoding.PEM, PublicFormat.SubjectPublicKeyInfo)
        return public_key

    # need to be a one way hash function 
    # address is derived from public key
    # the public key is hashed thanks to sha256 then RIPEMD160 one way hash function
    def hash_public_key_in_sha256_(self, public_key: bytes) -> str:
        str_public_key = public_key.decode("utf-8")
        sha256 =  crypt.crypt(str_public_key, crypt.METHOD_SHA256)
        return sha256
    # replaced ripemd160 by md5 because module import issue 
    def hash_derived_hashed_public_key_in_ripemd160(self, hash: str) -> str:
        double_hashed_public_key = RIPEMD160.new(bytes(hash, 'utf-8')).hexdigest()
        return double_hashed_public_key


    # we apply a bitcoin's standard that encode a base58 encoding to the double hashed public key
    def base_58_encode_public_key(self, double_hashed_public_key: str) -> bytes:
        base_58_encoded_public_key = base58.b58encode(double_hashed_public_key)
        return base_58_encoded_public_key