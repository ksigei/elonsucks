from django.shortcuts import render
from django.http import JsonResponse
from .models import Wallet, Transaction, Block
from .blockchain import Blockchain
from .utils import proof_of_work
import json
from django.db import transaction

# Instantiate the blockchain
blockchain = Blockchain()

def home(request):
    return render(request, 'home.html')

def create_transaction(request):
    if request.method == 'POST':
        sender_id = request.POST.get('sender_id')
        recipient_id = request.POST.get('recipient_id')
        amount = float(request.POST.get('amount'))

        sender_wallet = Wallet.objects.get(id=sender_id)
        recipient_wallet = Wallet.objects.get(id=recipient_id)

        # Create a new transaction
        transaction = Transaction.objects.create(sender_wallet=sender_wallet, recipient_wallet=recipient_wallet, amount=amount, transaction_type='TRANSFER')

        # Add the transaction to the current transactions of the blockchain
        blockchain.current_transactions.append({
            'sender': sender_wallet.public_key,
            'recipient': recipient_wallet.public_key,
            'amount': amount,
        })

        response = {
            'message': 'Transaction created successfully'
        }
        return JsonResponse(response)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'})

@transaction.atomic
def mine_block(request):
    # Get the last proof
    last_block = blockchain.last_block
    # last_proof = last_block['proof']
    last_proof = last_block.proof


    # Find the proof for the new block
    proof = proof_of_work(last_proof)

    # Get the previous block hash
    previous_hash = blockchain.hash_block(last_block)  # Pass last_block as an argument

    # Create the new block
    block = Block.objects.create(previous_block_hash=previous_hash, nonce=proof)

    # Add transactions to the new block
    for transaction_data in blockchain.current_transactions:
        sender_wallet = Wallet.objects.get(public_key=transaction_data['sender'])
        recipient_wallet = Wallet.objects.get(public_key=transaction_data['recipient'])
        amount = transaction_data['amount']  # No need to convert amount to string
        transaction = Transaction.objects.create(sender_wallet=sender_wallet, recipient_wallet=recipient_wallet, amount=amount, transaction_type='TRANSFER')
        block.transactions.add(transaction)

        # Update sender's balance
        sender_wallet.balance -= amount
        sender_wallet.save()

        # Update recipient's balance
        recipient_wallet.balance += amount
        recipient_wallet.save()

    # Clear current transactions
    blockchain.current_transactions = []

    # Update block hash
    block.block_hash = blockchain.hash_block(block)
    block.save()

    response = {
        'message': 'New block mined successfully',
        'block': {
            'id': block.id,
            'nonce': block.nonce,
            'previous_block_hash': block.previous_block_hash,
            'timestamp': block.timestamp,
            'block_hash': block.block_hash,  # Include block hash in the response
            'transactions': [transaction.id for transaction in block.transactions.all()]
        }
    }
    return JsonResponse(response)

def chain(request):
    blocks = Block.objects.all()
    chain = []
    for block in blocks:
        chain.append({
            'id': block.id,
            'nonce': block.nonce,
            'previous_block_hash': block.previous_block_hash,
            'timestamp': block.timestamp,
            'transactions': [transaction.id for transaction in block.transactions.all()]
        })
    
    response = {
        'chain': chain,
        'length': len(chain)
    }
    return JsonResponse(response)
