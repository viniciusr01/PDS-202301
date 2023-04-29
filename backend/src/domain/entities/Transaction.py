from src.utils.ValidDateTime import ValidDateTime

class Transaction:
    def __init__(self, 
                 description: str, 
                 value: float, 
                 reference_date, 
                 id_category: int
                 ) -> None:
        
        if(not ValidDateTime(reference_date)):
            raise Exception("It isn't a valid datetime")
        
        self.reference_date = reference_date
        self.description = description
        self.value = value
        self.id_category = id_category

