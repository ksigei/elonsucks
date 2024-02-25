# views.py
from django.http import HttpResponse
from .blockchain import Blockchain

def mine_block(request):
    blockchain = Blockchain()
    last_block = blockchain.last_block

    last_proof = last_block.proof
    proof = blockchain.proof_of_work(last_proof)
    previous_hash = blockchain.hash_block(last_block)  # You need to implement hash_block method
    nonce = 0  # Replace with actual nonce value or generate dynamically
    new_block = blockchain.new_block(proof=proof, previous_hash=previous_hash, nonce=nonce)
    return HttpResponse("Block mined successfully.")

def transfer(request):
    sender_id = request.POST.get('sender_id')
    recipient_id = request.POST.get('recipient_id')
    amount = request.POST.get('amount')

    blockchain = Blockchain()
    blockchain.new_transaction(sender=sender_id, recipient=recipient_id, amount=amount)

    return HttpResponse("Transaction successful.")
