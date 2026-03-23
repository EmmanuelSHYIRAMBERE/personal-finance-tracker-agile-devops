class Account:
    def __init__(self, name: str, initial_balance: float = 0.0):
        self.name = name
        self._balance = initial_balance
        self._transactions = []

    def add_transaction(self, amount: float, transaction_type: str):
        if transaction_type not in ["income", "expense"]:
            raise ValueError("Invalid transaction type")

        if transaction_type == "expense":
            amount = -abs(amount)

        self._transactions.append(amount)
        self._balance += amount

    def get_balance(self) -> float:
        return self._balance

    def get_transactions(self):
        return self._transactions

    def __str__(self):
        return f"Account({self.name}, Balance={self._balance})"