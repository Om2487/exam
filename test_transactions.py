import unittest
from transactions import *

class TestTransactions(unittest.TestCase):
    def setUp(self):
        # Initialize some sample data for testing
        self.test_data = [
            {"id": 1, "amount": 100, "description": "Test transaction 1"},
            {"id": 2, "amount": 200, "description": "Test transaction 2"},
            {"id": 3, "amount": 300, "description": "Test transaction 3"}
        ]
        with open(TRANSACTIONS_FILE, "w") as file:
            json.dump(self.test_data, file)

    def test_create_transaction(self):
        initial_count = len(read_transactions())
        new_transaction = {"id": 4, "amount": 400, "description": "Test transaction 4"}
        create_transaction(new_transaction)
        updated_count = len(read_transactions())
        self.assertEqual(updated_count, initial_count + 1)

    def test_get_transaction(self):
        transaction_id = 1
        transaction = get_transaction(transaction_id)
        self.assertIsNotNone(transaction)
        self.assertEqual(transaction["id"], transaction_id)

    def test_update_transaction(self):
        transaction_id = 2
        updated_transaction = {"id": 2, "amount": 250, "description": "Updated transaction"}
        update_result = update_transaction(transaction_id, updated_transaction)
        self.assertTrue(update_result)
        transaction = get_transaction(transaction_id)
        self.assertEqual(transaction, updated_transaction)

    def test_delete_transaction(self):
        transaction_id = 3
        delete_result = delete_transaction(transaction_id)
        self.assertTrue(delete_result)
        transaction = get_transaction(transaction_id)
        self.assertIsNone(transaction)

if __name__ == "__main__":
    unittest.main()