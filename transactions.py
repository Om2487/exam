import json

TRANSACTIONS_FILE = "x.json"

def read_transactions():
    with open(TRANSACTIONS_FILE, "r") as file:
        return json.load(file)

def write_transactions(transactions):
    with open(TRANSACTIONS_FILE, "w") as file:
        json.dump(transactions, file, indent=4)

def get_transaction(transaction_id):
    transactions = read_transactions()
    for transaction in transactions:
        if transaction["id"] == transaction_id:
            return transaction
    return None

def create_transaction(new_transaction):
    transactions = read_transactions()
    transactions.append(new_transaction)
    write_transactions(transactions)

def update_transaction(transaction_id, updated_transaction):
    transactions = read_transactions()
    for i, transaction in enumerate(transactions):
        if transaction["id"] == transaction_id:
            transactions[i] = updated_transaction
            write_transactions(transactions)
            return True
    return False

def delete_transaction(transaction_id):
    transactions = read_transactions()
    for i, transaction in enumerate(transactions):
        if transaction["id"] == transaction_id:
            del transactions[i]
            write_transactions(transactions)
            return True
    return False