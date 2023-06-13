from src.domain.entities.Category import Category
from ..gates.ISql import ISql

class RetrieveCategories():
    def __init__(self, db: ISql) -> None:
        self.db = db

    def make(self, user_id: str) -> list[Category]:

        res = self.db.RetrieveCategoriesFromUser(user_cpf=user_id)

        return res