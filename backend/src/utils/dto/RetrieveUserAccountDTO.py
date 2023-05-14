from src.domain.entities.BankAccount import BankAccount
from src.domain.entities.CreditCard import CreditCard
from src.domain.entities.Account import Account

class RetrieveUserAccountDTO:
    def __init__(self) -> None:
        pass

    def make(self, accounts: list[Account]):
        aux_list = []
        
        for account in accounts:
            if isinstance(account, BankAccount):
                aux = {
                    "Name": account.name,
                    "Description": account.description,
                    "Fees": account.fees,
                    "Color": account.color,
                    "Balance": account.balance
                    # BANK: ACCOUNT.BANK_NAME
                    # TODO: TRAZER O NOME DO BANCO AQUI
                }
            else:
                aux = {
                    "Name": account.name,
                    "Description": account.description,
                    "Fees": account.fees,
                    "Color": account.color,
                    "Balance": account.balance,
                    "Closure": account.closure_day, # type: ignore
                    "Deadline": account.payment_deadline, # type: ignore
                    "Bill Month": account.current_bill # type: ignore
                }
            
            aux_list.append(aux)

        return {
            "Accounts": aux_list
        }

