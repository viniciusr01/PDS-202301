from src.domain.value_objects.DefaultColor import DefaultColor
from src.domain.entities.Account import Account

class BankAccount(Account):
    def __init__(self, 
                 id: str, 
                 name: str, 
                 description: str, 
                 id_bank: str, 
                 fees: float = 0,
                 color: str = DefaultColor.code, 
                 balance: float = 0.0) -> None:
        super().__init__(id, name, description, fees, color, balance)
        self.id_bank = id_bank