import hashlib
import json
import time
from .models import Block, Transaction

class Blockchain:
    def __init__(self):
        self.current_transactions = []

        # Create the genesis block if the blockchain is empty
        if not Block.objects.exists():
            self.new_block(previous_hash='1', proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        Create a new Block in the Blockchain
        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <Block> New Block object
        """
        block = Block.objects.create(proof=proof, previous_block_hash=previous_hash)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined Block
        :param sender: <str> Address of the Sender (public key)
        :param recipient: <str> Address of the Recipient (public key)
        :param amount: <decimal> Amount
        :return: <Transaction> The newly created Transaction object
        """
        transaction = Transaction.objects.create(sender_wallet_id=sender, recipient_wallet_id=recipient, amount=amount, transaction_type='TRANSFER')
        return transaction

    @staticmethod
    def hash_block(block):
        """
        Creates a SHA-256 hash of a Block
        :param block: <Block> Block object
        :return: <str> Hash of the block
        """
        block_data = {
            'index': block.id,
            'timestamp': block.timestamp.timestamp(),
            'transactions': [transaction.id for transaction in block.transactions.all()],
            'proof': block.proof,
            'previous_hash': block.previous_block_hash,
        }
        block_string = json.dumps(block_data, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        """
        Returns the last block in the blockchain
        :return: <Block> Last Block object
        """
        return Block.objects.last()
