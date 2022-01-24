from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
class Secp256k1:
    def create_private_key(self, mnemonic):
        private_key = ec.generate_private_key(
            ec.SECP256K1()
        )
        signature = private_key.sign(mnemonic, ec.ECDSA(hashes.SHA256()))
        return signature
