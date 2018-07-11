INCENTIVE = 10

genesis_block = {
    'previous_hash': 'Micky Ds Hashbrowns',
    'index': '-0',
    'transactions': ['Black African Power!!!']
    }
blockchain = [genesis_block]
open_transactions = []
owner = 'NaCl Confi'
participants = {'NaCl Confi'}

def get_balance(participant):
    #Looks through entire blockchain and blocks in a nested 4loop, if the sender is found, tx_sender list holds the amount sent from each transactions
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender']==participants] for block in blockchain]
    open_tx_sender = [tx['sender'] for tx in open_transactions if tx['sender']== participants]
    amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]
    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient']==participants] for block in blockchain]
    amount_taken = 0
    for tx in tx_recipient:
        amount_taken += tx[0]
    return amount_sent - amount_taken

def checkdat_xchange(transaction):
    sender_balance = get_balance(transaction['sender'])
    return transaction['amount'] <= sender_balance
        

def hashbrown_skillet(block):
    #This hashbrown skillet allows you to hash the block
    return '_'.join([str(block[key]) for key in block])

def insert_trans_amount():
    """ Allows you to insert data values"""
    trx_recipient = input('Type the name of the sender')
    trx_amount= float(input('How much would you like to send???'))
    return (trx_recipient, trx_amount)


def get_BC_val():
    if len(blockchain) == 0:
        return 'Bruhhh... There\'s nothing in here. Sorry...'
    return blockchain[-1]

def get_choices():
    user_input= input('What\'s it gonna be???')
    return user_input

def add_transaction_data(amount, recipient, sender = owner):

    """" Arguments:
        sender: the one who sent the coins
        recipient: the one who recieves the coins
        amount: The amount of coins sent"""
    transaction = {'amount': amount, 'recipient': recipient, 'sender': sender }
    if checkdat_xchange(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
    else:
        return False
def mine_block():
    if len(blockchain) == 0:
        last_block = genesis_block
    else:
        last_block = blockchain[-1]
    for key in last_block:
        hashbrowns = hashbrown_skillet(last_block)

    incentive_tx = {'sender': 'The Black Community', 'recipient': owner, 'reward': INCENTIVE}
    print(hashbrowns)
    open_transactions.append(incentive_tx)
    block = {'previous hash': hashbrowns,
             'index': len(blockchain),
             'transactions': open_transactions
             }
    
    blockchain.append(block)
    return True

def print_elements():
    for block in blockchain: 
            print("Here's the output to the block fool")
            print("Block")
            print(block)
            print("Current Transaction list")
            print(open_transactions)
    else:
        print('♪♫'*10)
def verify():
    validity = True
    for (i, block) in enumerate(blockchain):
        if i == 0:
            continue
        if block['previous hash'] != hashbrown_skillet(blockchain[i-1]):
            validity = False
            print("       ")
            print("       ")
            print('Nah you aint slick homie...')
            print("Invalid Blockchain!!!!!!")
            print("       ")
            print("       ")
    return validity
waiting4input = True
while waiting4input:
    print('Would you like to enter a transaction or see the status of the blocks')
    print('   ')
    print('   ')
    print('Type "1" to add a new transaction value')
    print("       ")
    print('Type "2" to print the transactions')
    print("       ")
    print('Type "3" to mine a new block')
    print("       ")
    print('Type "4" to display the participants')
    print("       ")
    print('Type "runit" to manipulate the chain')
    print("       ")
    print('Type "q" (lowercase) to quit blockchain addition')
    decision = get_choices()
    if decision =='1':

        
       trx_input = insert_trans_amount()
       recipient, amount = trx_input
       add_transaction_data(amount, recipient)

    elif decision=='runit':
        newblockinfo = float(input("What should the genesis block be???"))
        blockchain[0]=[newblockinfo]
        
    elif decision =='2':
        print_elements()

    elif decision == '3':
        if mine_block():
            open_transactions = []
        
    elif decision == '4':
        print("These are the participants")
        print(participants)
    
    elif decision == 'q':
        waiting4input= False
    else: 
        print('Invalid answer my guy, but go ahead try it again')
else:
    print("This blockchain is done!!!!")
    print('This choice has been received')
verify()    
print('Finished Mom, Hasta Mañana!')
