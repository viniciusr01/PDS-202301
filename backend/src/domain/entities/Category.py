from src.domain.value_objects.DefaultColor import DefaultColor

class Category:
    def __init__(self, 
                 name: str, 
                 description: str,
                 user_cpf: str,
                 color: str = DefaultColor.code) -> None:
        self.name = name
        self.description = description
        self.user_cpf = user_cpf
        self.color = color