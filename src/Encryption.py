from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePrivateKey
from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurveSignatureAlgorithm
from cryptography.hazmat.primitives.serialization import Encoding
from cryptography.hazmat.primitives.serialization import PublicFormat
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

    def generate_bitcoin_address():
        pass
    