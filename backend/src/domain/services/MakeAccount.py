from ..gates.ISql import ISql
from ..entities.Account import Account

class MakeAccount:
    def __init__(self, db: ISql) -> None:
        self.db = db

    def make(self, account: Account) -> str:
        print("Adding a account... ")

        res = self.db.AddAccount({
            "name": account.name,
            "description": account.description,
            "color": account.color,
            "user_cpf": account.cpf_user,
            "fees": account.fees,
            "balance": account.balance
        })

        return res