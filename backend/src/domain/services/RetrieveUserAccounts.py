from datetime import date
from ..gates.ISql import ISql

from src.domain.entities.Account import Account
from src.domain.services.RetrieveBillBalance import RetrieveBillBalance
from src.domain.services.RetrieveUserBankAccounts import RetrieveUserBankAccounts
from src.domain.services.RetrieveAccountBalence import RetrieveAccountBalence
from src.domain.services.RetrieveUserCreditCards import RetrieveUserCreditCards

class RetrieveUserAccounts:
    def __init__(self, db: ISql) -> None:
        self.db = db
        self.retrieveAccount = RetrieveUserBankAccounts(self.db)
        self.retrieveCreditCards = RetrieveUserCreditCards(self.db)
        self.retrieveBalance = RetrieveAccountBalence(self.db)
        self.retrieveBillBalance = RetrieveBillBalance(self.db)

    def make(self, user_cpf: int) -> list[Account]:
        res = []
        credit_cards = self.retrieveCreditCards.make(user_cpf)
        bank_accounts = self.retrieveAccount.make(user_cpf)

        for credit_card in credit_cards:
            credit_card.current_bill.value = self.retrieveBillBalance.make(credit_card)
            res.append(credit_card)

        for bank_account in bank_accounts:
            bank_account.balance = self.retrieveBalance.make(bank_account)
            res.append(bank_account)

        return res
