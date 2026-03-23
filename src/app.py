# src/app.py

from models.account import Account


def main():
    account = Account("Main Account", 1000)

    print("Account created!")
    print(account)

    account.add_transaction(500, "income")
    account.add_transaction(200, "expense")

    print("Updated Balance:", account.get_balance())


if __name__ == "__main__":
    main()