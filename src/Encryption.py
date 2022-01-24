from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePrivateKey
from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurveSignatureAlgorithm
class Secp256k1:
    #         print(str(private_key.public_key().verify())) 
    def get_signature_from_private_key(self, private_key: EllipticCurvePrivateKey, mnemonic: str)-> bytes:
        signature = private_key.sign(mnemonic, ec.ECDSA(hashes.SHA256()))
        return signature
    def get_private_key(self) -> EllipticCurvePrivateKey:
        private_key = ec.generate_private_key(
            ec.SECP256K1()
        )
        return private_key
    def get_public_key(self, private_key: EllipticCurvePrivateKey, signature: bytes, data: bytes, signature_algorithm: EllipticCurveSignatureAlgorithm):
        public_key = private_key.public_key().verify(signature, data, signature_algorithm)
        return public_key
    