from src.utils.ValidObject import ValidObject
from src.domain.entities.Category import Category   

class CategoryFactory:
    def __init__(self) -> None:
        pass

    def make(self, obj: dict) -> Category:
        if not ValidObject().make(obj, [
            'name', 
            'description', 
            'user_cpf'
        ]):
            raise TypeError("Bad Request: Some key for a Category is missing.")
        
        return Category(
            name=obj['name'],
            description=obj['description'],
            color=obj['color'],
            user_cpf=obj['user_cpf'],
            id=0
        )
