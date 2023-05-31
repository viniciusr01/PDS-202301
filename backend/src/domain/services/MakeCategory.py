from ..gates.ISql import ISql
from ..entities.Category import Category

class MakeCategory:
    def __init__(self, db: ISql) -> None:
        self.db = db

    def make(self, category: Category) -> str:
        print("Adding a category... ")
        
        self.db.AddCategory({
            "name": category.name,
            "description": category.description,
            "color": category.color,
            "user_cpf": category.user_cpf
        })

        return "The category was successfully added."