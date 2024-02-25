import uuid
from django.db import models
from django.contrib.auth.models import User

class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    public_key = models.CharField(max_length=512)  # Public key of the wallet
    private_key = models.CharField(max_length=512)  # Private key of the wallet
    balance = models.DecimalField(max_digits=20, decimal_places=10, default=0)  # Current balance in the wallet

    def __str__(self):
        return f"Wallet for {self.user.username}"

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('PURCHASE', 'Purchase'),
        ('TRANSFER', 'Transfer'),
        ('REWARD', 'Reward'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender_wallet = models.ForeignKey(Wallet, related_name='sender_transactions', on_delete=models.CASCADE)
    recipient_wallet = models.ForeignKey(Wallet, related_name='recipient_transactions', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=10)
    description = models.CharField(max_length=255, null=True, blank=True)
    transaction_type = models.CharField(max_length=50, choices=TRANSACTION_TYPES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.id}"

class Block(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    transactions = models.ManyToManyField(Transaction)  # List of transactions in the block
    nonce = models.IntegerField()  # Nonce value used in proof of work
    previous_block_hash = models.CharField(max_length=64)  # Hash of the previous block
    proof = models.IntegerField()  # Proof of work for the block
    timestamp = models.DateTimeField(auto_now_add=True)  # Timestamp of when the block was created
    block_hash = models.CharField(max_length=64, blank=True)  # Hash of the current block

    def __str__(self):
        return f"Block {self.id}"

class Node(models.Model):
    url = models.URLField(unique=True)  # URL of the node
    last_seen = models.DateTimeField(auto_now=True)  # Timestamp of when the node was last seen

    def __str__(self):
        return f"Node {self.url}"
