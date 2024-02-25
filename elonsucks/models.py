# models.py
from django.db import models

class Block(models.Model):
    proof = models.IntegerField()
    previous_block_hash = models.CharField(max_length=255)
    nonce = models.IntegerField()

class Transaction(models.Model):
    sender_wallet_id = models.CharField(max_length=255)
    recipient_wallet_id = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=255)

class Wallet(models.Model):
    user_id = models.IntegerField()  # Assuming user ID for simplicity
    balance = models.DecimalField(max_digits=10, decimal_places=2)
