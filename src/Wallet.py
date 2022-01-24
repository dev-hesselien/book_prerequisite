
# it must generate a bitcoin adress
# the wallet need to recognize transactions and be able to send funds to the mentionned adress
# the wallet need to recognize transactions and process bitcoin bitcoin transaction being received from other adresses
# the wallet must store transaction's history and be able to show it when needed
# the wallets needs to be able to handle the impacts of the blockchain database reorganisation and other conflictions resolutions actions
# transactions fees vary -> see proof of work
# must be able to build and sign bitcoin transactions
# need to broadcast transaction to the blockchain

# the wallet contains the private key and various transactions metadata it's stored in private app
 
class Wallet:
    def __init__(self) -> None:
        pass
    
    def verify_signature(self, signature: str) -> bool:
        pass

    def generate_ledger_adress(private_key: str) -> str:
        pass
    # should return the public key after the encryption of the wallet-> should be conform with blockchain requirement
    def get_public_wallet_adress() -> str:
        pass
