from src.domain.value_objects.DefaultColor import DefaultColor

class Account:
    def __init__(self, 
                 id: str, 
                 name: str, 
                 description: str, 
                 fees: float = 0,
                 color: str = DefaultColor.code, 
                 balance: float = 0.0) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.color = color
        self.fees = fees
        self.balance = balance