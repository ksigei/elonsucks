from django.db import models
from django.contrib.auth.models import User

class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    def __str__(self):
        return f"Wallet for {self.user.username}"

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('PURCHASE', 'Purchase'),
        ('TRANSFER', 'Transfer'),
        ('REWARD', 'Reward'),
    ]

    sender = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='sender_transactions')
    recipient = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='recipient_transactions')
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.CharField(max_length=255, null=True, blank=True)
    transaction_type = models.CharField(max_length=50, choices=TRANSACTION_TYPES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction from {self.sender.user.username} to {self.recipient.user.username}"
