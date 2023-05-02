from src.domain.value_objects.DefaultColor import DefaultColor

class Account:
    def __init__(self, 
                 id: str, 
                 name: str, 
                 description: str, 
                 id_bank: str, 
                 balance: float,
                 color: str = DefaultColor.code, 
                 fees: float = 0 ) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.id_bank = id_bank
        self.color = color
        self.fees = fees
        self.balance = balance