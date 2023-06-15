from src.domain.value_objects.DefaultColor import DefaultColor

class Account:
    def __init__(self, 
                 name: str, 
                 description: str, 
                 id: int  = 0, 
                 fees: float = 0,
                 color: str = DefaultColor.code, 
                 balance: float = 0.0,
                 cpf_user: str = "") -> None:
        self.id = id
        self.name = name
        self.description = description
        self.color = color
        self.fees = fees
        self.balance = balance
        self.cpf_user = cpf_user