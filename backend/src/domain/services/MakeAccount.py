from ..gates.ISql import ISql
from ..entities.Account import Account

class MakeAccount:
    def __init__(self, db: ISql) -> None:
        self.db = db

    def make(self, account: Account) -> str:
        print("Adding a account... ")

        self.db.AddAccount({
            "name": account.name,
            "description": account.description,
            "color": account.color,
            "user_cpf": account.user_cpf,
            "fees": account.fees,
            "balance": account.balance
        })

        return "The category was successfully added."