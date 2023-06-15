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
                    "Balance": account.balance,
                    "Id": account.id
                    # BANK: ACCOUNT.BANK_NAME
                    # TODO: TRAZER O NOME DO BANCO AQUI
                }
            else:
                aux = {
                    "Name": account.name,
                    "Description": account.description,
                    "Id": account.id,
                    "Fees": account.fees,
                    "Color": account.color,
                    "Closure": account.closure_day, # type: ignore
                    "Deadline": account.payment_deadline, # type: ignore
                    "Bill": {
                        "Balance": account.current_bill.value, # type: ignore
                        "MonthYear": account.current_bill.moth_year, # type: ignore
                        "Id": account.current_bill.id, # type: ignore
                    } 
                }
            
            aux_list.append(aux)

        return {
            "Accounts": aux_list
        }

