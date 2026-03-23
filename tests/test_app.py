from src.models.account import Account


def test_account_creation():
    acc = Account("Test", 100)
    assert acc.get_balance() == 100


def test_add_income():
    acc = Account("Test", 0)
    acc.add_transaction(200, "income")
    assert acc.get_balance() == 200


def test_add_expense():
    acc = Account("Test", 500)
    acc.add_transaction(100, "expense")
    assert acc.get_balance() == 400