from django.shortcuts import render, redirect
from .models import Wallet, Transaction
from django.contrib.auth.decorators import login_required

@login_required
def initiate_transaction(request):
    if request.method == 'POST':
        sender_wallet = Wallet.objects.get(user=request.user)
        recipient_username = request.POST.get('recipient_username')
        recipient_wallet = Wallet.objects.get(user__username=recipient_username)
        amount = float(request.POST.get('amount'))

        if sender_wallet.balance >= amount:
            # Create transaction
            Transaction.objects.create(
                sender=sender_wallet,
                recipient=recipient_wallet,
                amount=amount,
                transaction_type='TRANSFER'
            )
            # Update sender and recipient balances
            sender_wallet.balance -= amount
            sender_wallet.save()
            recipient_wallet.balance += amount
            recipient_wallet.save()

            return redirect('transaction_success')
        else:
            return render(request, 'insufficient_funds.html')

    return render(request, 'initiate_transaction.html')

@login_required
def transaction_success(request):
    return render(request, 'transaction_success.html')
